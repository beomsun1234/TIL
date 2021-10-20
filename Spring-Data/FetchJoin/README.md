## Fetch Join

- 조회의 주체가 되는 Entity 이외에 Fetch Join이 걸린 연관 Entity도 함께 SELECT 하여 모두 영속화 해준다.

- Fetch Join이 걸린 Entity 모두 영속화하기 때문에 FetchType이 Lazy인 Entity를 참조하더라도
	이미 영속성 컨텍스트에 들어있기 때문에 따로 쿼리가 실행되지 않은 채로 N+1문제가 해결됨
	
	
### TEST를 위한 Cart, CartItem Entity

Cart

	@Entity
	@Getter
	@NoArgsConstructor(access = AccessLevel.PROTECTED)
	public class Cart {
		@Id
		@GeneratedValue(strategy = GenerationType.IDENTITY)
		private Long id;

		@OneToOne(fetch = FetchType.LAZY)
		@JoinColumn(name = "member_id")
		private Member member;

		@OneToMany(mappedBy = "cart", cascade = CascadeType.ALL)
		private List<CartItem> cartItems = new ArrayList<>();

		............... 생략

	}

CartItem	
	
	@Entity
	@NoArgsConstructor(access = AccessLevel.PROTECTED)
	@Getter
	public class CartItem {
		@Id
		@GeneratedValue(strategy = GenerationType.IDENTITY)
		private Long id;

		private String productName;

		private int productPrice;

		private int quantity;

		@ManyToOne(fetch = FetchType.LAZY)
		@JoinColumn(name = "cart_id")
		private Cart cart;
		
		@ManyToOne(fetch = FetchType.LAZY)
		@JoinColumn(name = "product_id")
		private Product product;
		
		...... 생략
		
	}
	
### 일반 Join

쿼리

	public Optional<Cart> findByMemberIdV1(Long id){
			return Optional.ofNullable(queryFactory.selectFrom(cart)
					.leftJoin(cart.cartItems, cartItem)
					.where(cart.member.id.eq(id))
					.fetchOne());
		}

카트 조회(CartService)

	 Cart cart = cartQueryRepository.findByMemberIdV1(memberId)
					.orElseGet(()-> Cart.builder().member(memberRepository.findById(memberId)
					.orElseThrow(()->new IllegalArgumentException("맴버가 없습니다"))).build());
			return TestDto.builder().cartInfos(cart.getCartItems()
				.stream()
				.map(cartItem -> CartInfo.builder().cartItem(cartItem).build())
				.collect(Collectors.toList())).build();
			

이제 카트를 조회해 보자!

	Hibernate: 
		select
			cart0_.id as id1_0_,
			cart0_.member_id as member_i2_0_ 
		from
			cart cart0_ 
		left outer join
			cart_item cartitems1_ 
				on cart0_.id=cartitems1_.cart_id 
		where
			cart0_.member_id=?
	Hibernate: 
		select
			cartitems0_.cart_id as cart_id5_1_1_,
			cartitems0_.id as id1_1_1_,
			cartitems0_.id as id1_1_0_,
			cartitems0_.cart_id as cart_id5_1_0_,
			cartitems0_.product_id as product_6_1_0_,
			cartitems0_.product_name as product_2_1_0_,
			cartitems0_.product_price as product_3_1_0_,
			cartitems0_.quantity as quantity4_1_0_ 
		from
			cart_item cartitems0_ 
		where
			cartitems0_.cart_id=?
			
카트를 조회하고 카트에있는 cartItem을 사용할 경우 해당 cartitem을 영속화 하기 위해 select 쿼리가 발생한다. 

확인해 보니 일반 join은 실제 쿼리에 join을 걸어주기는 하지만 join대상에 대한 영속성까지는 관여하지 않고 영속성 컨텍스트에는 SELECT 대상(Cart)만을 담는다. 

이 때문에 cart에 cartItem을 사용 할 경우 cartitem을 영속화 하기 위해 select 쿼리가 발생 된다. 

이 문제를 해결 하기 위해 Fetch Join 사용해 보자!

### Fetch Join

쿼리

	public Optional<Cart> findByMemberIdV2(Long id){
			return Optional.ofNullable(queryFactory.selectFrom(cart)
							.distinct()
					.leftJoin(cart.cartItems, cartItem).fetchJoin()
					.where(cart.member.id.eq(id))
					.fetchOne());
		}

카트 조회(CartService)

	Cart cart = cartQueryRepository.findByMemberIdV2(memberId)
					.orElseGet(()-> Cart.builder().member(memberRepository.findById(memberId)
					.orElseThrow(()->new IllegalArgumentException("맴버가 없습니다"))).build());
			return TestDto.builder().cartInfos(cart.getCartItems()
				.stream()
				.map(cartItem -> CartInfo.builder().cartItem(cartItem).build())
				.collect(Collectors.toList())).build();


이제 카트를 조회해 보자

	Hibernate: 
		select
			distinct cart0_.id as id1_0_0_,
			cartitems1_.id as id1_1_1_,
			cart0_.member_id as member_i2_0_0_,
			cartitems1_.cart_id as cart_id5_1_1_,
			cartitems1_.product_id as product_6_1_1_,
			cartitems1_.product_name as product_2_1_1_,
			cartitems1_.product_price as product_3_1_1_,
			cartitems1_.quantity as quantity4_1_1_,
			cartitems1_.cart_id as cart_id5_1_0__,
			cartitems1_.id as id1_1_0__ 
		from
			cart cart0_ 
		left outer join
			cart_item cartitems1_ 
				on cart0_.id=cartitems1_.cart_id 
		where
			cart0_.member_id=?


일반 join을 사용할 경우와 차이가 있다.

일반 join일 경우 select 대상 entity컬럼만 조회하는 반면,
Fetch join은 select 대상 뿐만 아니라 join에 걸려있는 entity 까지 포함한 컬럼을 조회한다.

Fetch join 사용하면 쿼리 한번으로 cart에 포함된 cartItem들을 가져오고 영속성 컨텍스트에 cart와 cartItem을 담게 된다.

	cart.getCartItems()
					.stream()
					.map(cartItem -> CartInfo.builder().cartItem(cartItem).build())
					.collect(Collectors.toList())).build();
					
위 처럼 cart.getCartItems()을 해도 select 쿼리가 발생되지 않는다.


조회 결과

	"totalPrice": 150000,
		"cartInfos": [
			{
				"cartItemId": 12,
				"productName": "테스트3",
				"productPrice": 30000,
				"quantity": 2,
				"totalPrice": 60000
			},
			{
				"cartItemId": 33,
				"productName": "테스트2",
				"productPrice": 20000,
				"quantity": 3,
				"totalPrice": 60000
			},
			{
				"cartItemId": 34,
				"productName": "테스트1",
				"productPrice": 10000,
				"quantity": 3,
				"totalPrice": 30000
			}
		]
