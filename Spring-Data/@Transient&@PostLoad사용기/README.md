## 좌충우돌 @Transient, @

프로젝트를 진행 중 프론트 쪽에서 상품에 관한 이미지(썸네일, 상품이미지)를 관리 하지 않았으면 좋겠다고 했다(db저장x).

엔티티 객체의 데이터와 테이블의 컬럼(column)과 매핑하고 있는 관계를 제외하기(테이블 관리x) 위해 @Transient 어노테이션을 사용해 보았다.

즉 @Transient 어노테이션을 사용한 필드나 메소드는 DB 테이블에 적용되지 않고  엔티티 클래스 내부에서만 동작하게 하는데 사용된다.

아래는 상품 엔티티이다.

    @NoArgsConstructor(access = AccessLevel.PROTECTED)
    @Entity
    @Getter
    public class Product extends BaseTimeEntity {
        @Id
        @GeneratedValue(strategy = GenerationType.IDENTITY)
        private Long id;
    
        private String name;

        private int price;

        @Transient
       테이블 매핑 x
        private String thumbnailImage;

        @Transient
        테이블 매핑 x
        private final List<String> productImage = new ArrayList<>();

        @ManyToOne(fetch = FetchType.LAZY)
        @JoinColumn(name = "product_category_id")
        private ProductCategory productCategory;

        @Builder
        public Product(String name, int price, ProductCategory productCategory){
            this.name = name;
            this.price = price;
            this.productCategory = productCategory;
        }

        //데이터 조회시 이미지 경로 저장(테이블 만들지 않기 위해 사용) but 나중에 이미지 테이블 만들어야함
        @PostLoad
        public void setProductImages(){
            for (int i = 1; i<=3; i++){
                this.productImage.add("ProductImage/"+getId()+"/"+i+".png");
            }
           this.thumbnailImage = "ProductImage/"+getId()+"/"+"thumbnail.png";
        }

    }

이렇게 하면 이미지 테이블을 만들어 관리 할 필요 없이 상품 id에 해당하는 폴더에 약속된 사진 이름만 넣어주면 

    도메인/images/ProductImage/상품id/이름.png 
    
를 통해 이미지를 화면에 출력할 수 있다.

---

## 문제 발생

상품조회시 thumbnailImage, productImage 값을 계속 계속 넣어 줘야했다....이러한 번거로움을 단번에 해결해주는 친구를 찾아냈다.

    @PostLoad : 해당 엔티티를 새로 불러오거나 refresh 한 이후
    @PrePersist : 해당 엔티티를 저장하기 이전
    @PostPersist: 해당 엔티티를 저장한 이후
    @PreUpdate : 해당 엔티티를 업데이트 하기 이전
    @PostUpdate : 해당 엔티티를 업데이트 한 이후
    @PreRemove : 해당 엔티티를 삭제하기 이전
    @PostRemove : 해당 엔티티를 삭제한 이후
    
바로 @PostLoad 어노테이션이다. image가 필요한 부분은 상품이 조회된 후 dto로 반환하여 프론트에게 api를 보낼때만 필요하기 때문에 @PostLoad를 통해
해당 엔티티가 조횔 될때 image 값들을 셋팅한다.

        @PostLoad
        public void setProductImages(){
            for (int i = 1; i<=3; i++){
                this.productImage.add("ProductImage/"+getId()+"/"+i+".png");
            }
           this.thumbnailImage = "ProductImage/"+getId()+"/"+"thumbnail.png";
        }

1.png-> 상단 이미지, 2.png-> 중단 이미지, 3.png-> 하단이미지 , thumbnail.png -> 썸네일로 설정해 주었다.


    @Cacheable(value = "products", key = "{#id,#pageable.pageNumber}", unless = "#result.size()<0")
    @Transactional(readOnly = true)
    public List<ProductInfo> findProductByCategoryId(String id, Pageable pageable){
        return productQueryRepository.findByCategoryId(pageable, id)
                .stream()
                .map(product -> ProductInfo.builder().product(product).build())
                .collect(Collectors.toList());
    }
    
findProductByCategoryId()실행 시 setProductImages()를 호출하지 않아도 자동으로 실행되며 


    @Builder
    public ProductInfo(Product product){
        this.id = product.getId();
        this.name = product.getName();
        this.price = product.getPrice();
        this.thumbnailImage = product.getThumbnailImage();
    }
    

product.getThumbnailImage()를 값을 가져오면 null이 아닌 ProductImage/상품id/thumbnail.png 값을 가진다.



