## Insert시 Select쿼리 발생 문제

현재 e-커머스 프로젝트를 진행하고 있는데 문제가 발생했었다. 

category entity

    @Id
    private String id;

    //카테고리 이름
    private String name;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "parent_product_category_id")
    private ProductCategory parentCategory;


    @BatchSize(size = 100)
    @OneToMany(mappedBy = "parentCategory",cascade = CascadeType.ALL)
    private List<ProductCategory> subCategory = new ArrayList<>();

    @Builder
    public ProductCategory(String id, String name,ProductCategory parentCategory) {
        this.id = id;
        this.name = name;
        this.parentCategory = parentCategory;
    }

    
위 코드는 기존에 카테고리 entity이다. 카테고리를 생성하고 저장시 카테고리를 조회하고 저장하는 쿼리가 나간다. 

productRepository.save(productCategory)가 실행되면 아래 쿼리가 실행된다.

    select product_category ...

    insert product_category ...
    
    
나는 분명 save()를 실행했는데 select쿼리가 왜 발생하지?.... 왜그러지??.. 해결하지 않으면

만약 100000개의 save가 있다면 select를 100000번 실행하고 하고 insert 쿼리를 실행하게 될 것이다...  



## Persist 와 Merge

jpa에서 save()시 어떻게 호출 되는지 알아보자

    @Transactional
    public <S extends T> S save(S entity) {
    
	    if (entityInformation.isNew(entity)) {
	    	em.persist(entity);
	    	return entity;
	    } else {
	    	return em.merge(entity);
	    }
    }
    

새로운 엔티티를 등록하는 거니 em.persist(entity)가 실행될 것이라 생각했다. 

하지만 em.merge(entity)가 샐행된다.

찾아보니 JpaRepository.save 호출 시 엔티티의 식별자(@Id, @EmbeddedId 어노테이션이 붙은 컬럼 등등)가 붙은 필드의 타입이 
primitive type이 아닐 때는 null이거나 숫자형일 때는 0이면 새로운 엔티티라고 판단하면서 persist 메서드가 호출되고, 
그게 아니면 merge 메서드가 호출된다.( 새로운 Entity일 경우 persist, 기존 Entity일 경우 merge)


즉 @Id 필드에 값이 이미 존해하기 때문에 db에 존재하는 데이터로 간주하여 (현재 카테고리리 생성시 id를 직접 입력한다.)

insert를 하지 않고 update할 항목이 있는지 확인하기 위해 select가 실행되지만 @Id값으로 select한 결과가 없기에 insert 쿼리를 실행한다.

- 참고

기존에 @GenerateValue 일 경우 save()호출 시점에는 식별자가 없기 때문에 새로운 엔티티로 인식해서 정상동작한다.

## 해결 방법

해결하기 위해 카테고리 저장시 새로운 엔티티라는 것을 판별할 수 있도록 설정해줘야한다. Persistable 인터페이스를 구현해보자.
현재 @Id필드인 id 값은 직접 입력하고 있기에 새로 생성한 것인지 판단하기 어렵다. 그래서 생성 날짜 필드를 추가했주었다(BaseTimeEntity이용).

    public class ProductCategory extends BaseTimeEntity implements Persistable<String> {
       
        .....
       
        @Override
        public boolean isNew() {
            return getCreatedDate() == null;
        }

    }

생성 일자가 없을 경우 새로운 엔티티로 판별하도록 구현하니 문제가 해결되었다.
