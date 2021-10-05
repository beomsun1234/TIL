# 다양한 연관관계

## 다중성
데이터베이스를 기준으로 다중성을 결정한다.


연관 관계는 대칭성을 갖는다.

일대다 ↔ 다대일

일대일 ↔ 일대일

다대다 ↔ 다대다


    다대일(@ManyToOne)
    일대다(@OneToMany)
    일대일(@OneToOne)
    다대다(@ManyToMany)
    
보통 다대일과 일대다 관계를 가장 많이 사용하고 다대다 관계는 실무에서 거의 사용하지 않는다!!

---

## 다대일(N:1)


- 다대일 관계의 방향은 항상 일대다 관계고 일대다 관계의 반대 방향은 항상 다대일 관계이다.
- 데이터베이스 테이블의 일(1), 다(N) 관계에서 외래 키는 항상 다쪽에 있다. 
 
``객체 양방향 관계에서 연관관계의 주인은 항상 다쪽``

### 다대일(N:1) 단방향
Member와 Team의 관계
- 하나의 Team에는 여러 Member가 있다.
- Member와 Team은 다대일 관계를 갖는다.

[사진]

외래키는 다 쪽인 Member가 관리한다.(연관관계 주인 = Member)


 Member class

    @Entity 
    public class Member {
    
    @Id 
    @GeneratedValue 
    private Long id; 
    
    private String username;
    
    @ManyToOne 
    @JoinColumn(name = "team_id") 
    private Team team;
    
    //... getter, setter
    }
    
Team class  
    

    @Entity 
    public class Team {
    
    @Id 
    @GeneratedValue 
    private Long id; 
    
  	private String name;
    
 
    //... getter, setter
    }
    
다 쪽인 Member에 @ManyToOne 만 추가
반대로 Team에서는 참조하지 않는다. (단방향이기 때문)


### 다대일(N:1) 양방향 [N:1, 1:N]

[사진]

 Member class

    @Entity 
    public class Member {
    
    @Id 
    @GeneratedValue 
    private Long id; 
    
    private String username;
    
    @ManyToOne 
    @JoinColumn(name = "team_id") 
    private Team team;
    
    //... getter, setter
    }
    
Team class  
    

    @Entity 
    public class Team {
    
    @Id 
    @GeneratedValue 
    private Long id; 
    
  	private String name;
    
 	@OneToMany(mappedBy = "team")
    List<Member> members = new ArrayList<>();

    //... getter, setter
    }

다대일 양방향으로 만드려면 일(1) 쪽에 @OneToMany 를 추가하고 양방향 매핑을 사용했으니 연관 관계의 주인을 mappedBy 로 지정해준다. (연간관계 주인 = Member)

mappedBy로 지정할 때 값은 대상이 되는 변수명을 따라 지정하면 된다. 여기서는 Member 객체(대상)의 team라는 이름의 변수이기 때문에 team로 지정

    양방향 연관관계는 항상 서로 참조 
    어느 한 쪽만 참조하면 양방향 연관관계가 성립하지 않는다. 
    항상 서로 참조하게 하려면 연관관계 편의 메서드를 만드는 것이 좋다.
	
    ex) Memeber
    
    public class Member{
  
  	private Team team;
  
  	public void setTeam(Team team) {
    	if(this.team != null) {	
        	// this.team이 null이 아니면 이 member객체는 team이 있음을 의미
   			this.team.getMembers().remove(this);		// 해당 팀의 멤버에서 삭제
 		 }
    	this.team = team;
    	team.getMembers().add(this);
  	   }
  	// ...
	}
    
    
 ---
 
## 일대다(1:N)

일대다는 다대일에서 반대 입장인데 정리할 필요가 있나? 생각할 수 있지만 앞서 다대일의 기준은 연관관계의 주인 다(N)쪽에 둔 것이고 이번에 언급할 일대다의 기준은 연관관계의 주인을 일(1)쪽에 둔 것이다.

※ 참고로 실무에서는 일대다(1:N) 단방향은 거의 쓰지 않도록 한다.

### 일대다(1:N) 단방향

[사진]

데이터베이스 입장에서는 무조건 다(N)쪽에서 외래키를 관리합니다.

일대다 단방향은 일(1)쪽 객체에서 다(N) 쪽 객체를 조작(생성,수정,삭제)하는 방법입니다.


Member class

    @Entity 
    public class Member {
    
    @Id 
    @GeneratedValue 
    private Long id; 
    
    private String username;
  
    
    //... getter, setter
    }
    
Team class  
    

    @Entity 
    public class Team {
    
    @Id 
    @GeneratedValue 
    private Long id; 
    
  	private String name;
    
 	@OneToMany
    @JoinColumn(name = "member_id") //일대다 단방향을 @JoinColumn필수
    List<Member> members = new ArrayList<>();

    //... getter, setter
    }

일대다 단방향 관계를 매핑할 때는 @JoinColumn을 꼭 사용해야 한다. 그렇지 않으면 JPA는 연결 테이블을 중간에 두고 연관관계를 관리하는 조인 테이블 전략을 기본으로 사용해서 매핑한다.(중간에 테이블 하나 추가함)



- 일대다 단방향 매핑의 단점

	  매핑한 객체가 관리하는 외래 키가 다른 테이블에 있다.
      본인 테이블에 외래 키가 있으면 엔티티의 저장과 연관관계 처리를 INSERT SQL 한 번으로 끝낼 수 있지만,
      다른 테이블에 외래 키가 있으면 연관관계 처리를 위한 UPDATE SQL을 추가로 실행해야 합니다.
		
   
   즉, Team 엔티티는 Team 테이블에 매핑되기 때문에 Team 테이블에 직접 지정할 수 있으나, 
   Member 테이블의 FK(team_id)를 저장할 방법이 없기 때문에 조인 및 업데이트 쿼리를 날려야 하는 문제가 있습니다.



### 일대다 양방향
[사진]

일대다 양방향 매핑은 공식적으로 존재하지 않는다.
@JoinColumn(insertable=false, updatable=false)
읽기 전용 필드를 사용해서 양방향 처럼 사용하는 방법이다.

``일대다(1:N) 단방향, 양방향은 쓰지 말고 차라리 다대일(N:1) 양방향으로 쓰는 것이 맞다``


---

## 일대일(1:1)

주 테이블에 외래키를 넣을 수도 있고, 대상 테이블에 외래키를 넣을 수도 있습니다.

※ 일대일(1:1)이기 때문에 테이블 A, B가 있을 때, A가 주 테이블이면 B가 대상 테이블이고, B가 주 테이블이면 A가 대상 테이블입니다.


 회원과 사물함이 있다고 할 때, 회원은 하나의 사물함만 소유할 수 있고 사물함도 회원 한명에 의해서만 소유될 수 있다고 한다면 1 : 1 관계이다.


- 주 테이블에 외래 키

	- 주 객체가 대상 객체를 참조하는 것처럼 주 테이블에 외래 키를 두고 대상 테이블을 참조
	- 외래 키를 참조와 비슷하게 사용할 수 있어서 객체지향 개발자들이 선호.
	- 이 방법의 장점은 주 테이블이 외래 키를 가지고 있으므로 주 테이블만 확인해도 대상 테이블과 연관관계가 있는지 알 수 있다.

- 대상 테이블에 외래 키
	- 전통적인 데이터베이스 개발자들은 보통 대상 테이블에 외래 키를 두는 것을 선호
	- 이 방법의 장점은 테이블 관계를 일대일에서 일대다로 변경할 때 테이블 구조를 그대로 유지할 수 있다.

### 주 테이블에 외래 키

#### - 단방향

[사진]

- MEMBER가 주 테이블이고 LOCKER는 대상 테이블이다.
- 회원은 하나의 Locker만 가지고, Locker는 하나의 회원에 의해서만 사용되는 경우입니다.
- @OneToOne 어노테이션을 사용하고, 


Member class

  	@Entity
  	public class Member {

      @Id 
      @GeneratedValue
      private Long id;

      private String userName;

      @OneToOne
      @JoinColumn(name = "locker_id")
      private Locker locker;
      
      //... getter, setter
	}

Locker class

  	@Entity
  	public class Locker {

      @Id 
      @GeneratedValue
      private Long id;

      private String name;
      
      //... getter, setter
     }

 다대일 단방향(@ManyToOne)과 거의 비슷합니다.
 
 
 #### - 양방향
 
 [사진]
 
양방향이므로 연관관계의 주인을 정해야 합니다. MEMBER 테이블이 외래 키를 가지고 있으므로 Member가 연관관계 주인이다.
 
 
 Locker 에서 Member 를 참조하도록  Locker class 수정
 
 
  	@Entity
  	public class Locker {

      @Id 
      @GeneratedValue
      private Long id;

      private String name;

      @OneToOne(mappedBy = "locker")
      private Member member;
      
      //... getter, setter
 	}
    
 Member에 연관관계 편의 메서드 추가
 
	@Entity
  	public class Member {
    
      .....
   	  @OneToOne
      @JoinColumn(name = "locker_id")
      private Locker locker;
      
      // 연관관계 편의 메서드
      public void setLocker(Locker locker) {
	
      		if(this.locker != null) {
				this.locker.setUser(null);
			}
	
			this.locker = locker;
	
			if(locker != null) {
				locker.setUser(this);
			}
		}
        
      //... getter, setter
	}
 
 
 ### 대상 테이블에 외래키
 
 #### - 단방향

[사진]

- 위처럼 일대일 관계 중 대상 테이블에 외래 키가 있는 단방향 관계는 JPA에서 지원하지 않는다. 
- 단방향 관계를 Locker에서 Member 방향으로 수정하거나, 양방향 관계로 만들고 Locker를 연관관계의 주인으로 설정해야 합니다.

 
 #### - 양방향
 [사진]
 
 일대일 매핑에서 대상 테이블에 외래 키를 두고 싶으면 이렇게 양방향으로 매핑
 
 Member class
 
    @Entity
    public class Member {

      @Id 
      @GeneratedValue
      private Long id;

      private String username;

      @OneToOne(mappedBy ="member")
      private Locker locker
      
      //... getter, setter
      
    }
    
    
Locker class


   	@Entity
    public class Locker {
        @Id 
        @GeneratedValue
        private Long id;

        private String name;

        @OneToOne
        @JoinColumn(name = "MEMBER_ID")
        private Member member;
        
        //... getter, setter
     }
     
     
     
- 정리
	-	일대일 관계는 그 반대도 일대일 관계다.
	-	일대일 관계는 주 테이블이나 대상 테이블 둘중 어느곳이나 외래키를 가질 수 있다.
	-	일대일 관계중 대상 테이블에 외래 키가 있는 단방향 관계는 JPA에서 지원하지 않는다.


---


## 다대다(N:M)
관계형 데이터베이스는 정규화된 테이블 2개로 다대다를 표현할 수 없습니다.

``보통 다대다 관계를 일대다, 다대일 관계로 풀어내는 연결 테이블을 사용``

[사진]


예를들면 회원들은 상품을 주문한다. 반대로 상품들은 회원들에 의해 주문 된다.
둘은 대다대 관계입니다. 따라서 회원 테이블과 상품 테이블만으로 이 관계를 표현할 수 없다.
그래서 위 그림처럼 중간에 연결 테이블을 추가해야 합니다. 이 테이블을 사용해서 다대다 관계를 일대다, 다대일 관계로 풀어낼 수 있습니다.



객체는 테이블과 다르게 객체 2개로 다대다 관계를 만들 수 있습니다. 예를 들어, 회원 객체는 컬렉션을 사용해서 상품들을 참조하면 되고, 반대로 상품들도 컬렉션을 사용해서 회원들을 참조하면 됩니다.

``실무에서 사용 x``
- 중간 테이블이 숨겨져 있기 때문에 자기도 모르는 복잡한 조인의 쿼리(Query)가 발생하는 경우가 생길 수 있기 때문입니다.

- 다대다로 자동생성된 중간테이블은 두 객체의 테이블의 외래 키만 저장되기 때문에 문제가 될 확률이 높습니다. JPA를 해보면 중간 테이블에 외래 키 외에 다른 정보가 들어가는 경우가 많기 때문에 다대다를 일대다, 다대일로 풀어서 만드는 것(중간 테이블을 Entity로 만드는 것)이 추후 변경에도 유연하게 대처할 수 있습니다.


### 다대다 매핑의 한계

편리해 보이지만 실무에서 사용하기엔 한계가 있다.


예를 들어 회원이 상품을 주문하면 연결 테이블에 단순히 주문한 회원 아이디와 상품 아이디만 담고 끝나지 않습니다. 보통은 연결 테이블에 주문 수량 컬럼이나 주문한 날짜 같은 컬럼이 더 필요합니다. 

[사진]


위와 같이 연결 테이블에 주문 수량(ORDERAMOUNT)나 주문 날짜(ORDERDATE) 컬럼을 추가했습니다. 이렇게 컬럼을 추가하면 더는 @ManyToMany를 사용할 수 없다. 왜냐하면 주문 엔티티나 상품 엔티티에는 추가한 컬럼들을 매핑할 수 없기 때문이다.





### 다대다 한계 극복

- ``연결 테이블용 엔티티 추가(연결 테이블을 엔티티로 승격)``

- @ManyToMany -> @OneToMany, @ManyToOne 로 풀기

[사진]

연결용테이블인 MemberProduct를 Order 엔티티로 승격

  	@Entity
    public class Order {

     @Id 
     @GeneratedValue
     @Column(name = "ORDER_ID")
     private Long Id;

     @ManyToOne
     @JoinColumn(name = "member_id")
     private Member member;

     @ManyToOne
     @JoinColumn(name = "product_id")
     private Product product;

     private int orderAmount;

     ...
   	}


Member class(@OneToMany, @ManyToOne 로 풀기)

  	@Entity
  	public class Member {

    @Id 
    @GeneratedValue
    private Long id;

    @OneToMany(mappedBy = "member")
    private List<Order> orders = new ArrayList();
    ..   
  	}

Product class(@OneToMany, @ManyToOne 로 풀기)

	@Entity
  	public class Product {

    @Id 
    @Column(name = "PRODUCT_ID")
    private String id;

    private String name;

    ..   
  	}


----
