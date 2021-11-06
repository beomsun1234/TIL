# 좌충우돌 Redis 사용기

## Redis란?
Redis는 In-memory 기반의 NoSQL DBMS로서 Key-Value의 구조를 가지고있다. 또한 속도가 빠르고 사용이 간편하다. 캐싱,세션관리,pub/sub 메시징 처리등에 사용된다.

Spring에서 Redis를 사용하기위한 라이브러리는 2가지가있다.

- jedis
- lettuce

jedis는 thread-safe하지 않기 때문에 jedis-pool을 사용해야한다. 그러나 비용이 증가하기 때문에 lettuce를 많이 사용한다.

Lettuce는 별도의 설정없이 사용할 수 있으며 Jedis를 사용하고자 하시면 별도의 의존성이 필요함.

## sprngboot redis 설정법(gradle)

    implementation 'org.springframework.boot:spring-boot-starter-data-redis'



Spring Boot 에서 Redis 를 사용하는 방법 2가지
- RedisTemplate을 이용
- Redis Repository를 이용

RedisTemplate을 사용하겠다.

## Redis 사용을 위한 Configuration bean 적용



    @Bean
    public LettuceConnectionFactory redisConnectionFactory() {
        return new LettuceConnectionFactory("localhost", 6379);
    }

    @Bean
    public RedisTemplate<?, ?> redisTemplate() {
        RedisTemplate<byte[], byte[]> redisTemplate = new RedisTemplate<>();
        redisTemplate.setConnectionFactory(redisConnectionFactory());
        return redisTemplate;
    }

### RedisConnectionFactory

redis와 connection을 생성해주는 객체

    new LettuceConnectionFactory("localhost", 6379);

위 두 개의 인자가 필요하며, 처음은 host의 주소, 두번째는 포트 번호이다.

참고 
-   Redis를 설치하면서 port 설정을 6379로 하였으니, 로컬에서 실행하여 접속할때는 localhost:6379 로 접속하게 된다.



### RedisTemplate
- Redis는 RedisTemplate을 통해서 Redis 서버와 통신한다.

- RedisTemplate 을 사용하면 특정 Entity 뿐만 아니라 여러가지 원하는 타입을 넣을 수 있다.

- redisTemplate 을 주입받은 후에 원하는 Key, Value 타입에 맞게 Operations 을 선언해서 사용할 수 있다.

        ex)
        @Autowired
        private RedisTemplate redisTemplate;

        @Test
        public void testStrings() {
            final String key = "1";
            final String data = "success"

            final ValueOperations<String, String> stringStringValueOperations = redisTemplate.opsForValue();

            stringStringValueOperations.set(key, data); 

            final String ret = stringStringValueOperations.get(key); // redis get 명령어

            System.out.println("ret = " + ret);
        }
        -> ret = success


---

# Redis Cache 사용기

쇼핑몰 카테고리 정보를 redis cache에 저장해 보자

우선 캐쉬를 사용하기 위해

Springboot에 @EnableCaching 어노테이션을 등록해서 캐시를 사용하겠다고 알려주자

 	@EnableCaching
    @EnableJpaAuditing
    @SpringBootApplication
    public class OhouApplication {

	    public static void main(String[] args) {
		    SpringApplication.run(OhouApplication.class, args);
	    }

    }



Category entity

    @Entity
    @Getter
    @NoArgsConstructor(access = AccessLevel.PROTECTED)
    public class ProductCategory {
        @Id
        private String id;

        //카테고리 이름
        private String name;

        @ManyToOne(fetch = FetchType.LAZY)
        @JoinColumn(name = "parent_product_category_id")
        private ProductCategory parentCategory;


        @OneToMany(mappedBy = "parentCategory",cascade = CascadeType.ALL)
        private List<ProductCategory> subCategory = new ArrayList<>();
        
        @Builder
        public ProductCategory(String id, String name,ProductCategory parentCategory) {
            this.id = id;
            this.name = name;
            this.parentCategory = parentCategory;
        }
    }

주요어노테이션

|어노테이션|설명|
|------|---|
|@Cacheable|캐시가 있으면 캐시의 정보를 가져오고 없으면 등록한다.|
|@CachPut|무조건 캐시에 저장한다.|
|@CachEvict|캐시를 삭제한다.|


### 캐시등록및 조회

CategoryInfo class

    @Getter
    @NoArgsConstructor
    public class CategoryInfo implements Serializable{
        private String id;
        private String name;

        @Builder
        public CategoryInfo(ProductCategory entity){
            this.id=entity.getId();
            this.name = entity.getName();
        }
    }

Redis에 객체를 저장하면 내부적으로 직렬화되어 저장되는데, 이때 사용할 class에 Serializable을 선언해주지 않으면 오류가 발생할수 있습니다.


Category 조회 (부모카테고리가 가지는 하위 카테고리 조회 쿼리 즉 부모카테고리일 경우만 조회)

    @Cacheable(value = "category", key = "#id", unless = "#result < 0")
    @Transactional(readOnly = true)
    public List<CategoryInfo> findByCategoryId(String id){

        List<Category> categorys = queryFactory
        .selectFrom(category)
        .where(eqCategoryId(id))
        .fetch();

        return categorys
                .stream()
                .map(ctg -> CategoryInfo.builder().entity(ctg)
                .build())
                .collect(Collectors.toList())
    }

반환된 CategoryInfo리스트를 캐시에 저장한다(키값은 id) 한번더 조회 해보면 DB를 조회하지 않고 캐시를 조회해서 데이터를 가져올 것이다. 

    id 1을 조회할 경우
    부모 카테고리가 1인 데이터들이 캐시에 저장된다.

    category::1 

데이터를 추가해보자(부모 카테고리 추가시 parentId == null)

    @PostMapping("category")
    @Transactional
    public CategoryInfo create(@RequestParam String id, 
                               @RequestParam String name, 
                               @RequestParam(required = false) String parentId){

            log.info("id={}", id);

            if(parentId != null){
                Category parentCategory = categoryRepository.findByParentId(parentId).orElseThrow(() -> new IllegalArgumentException("에러"));
                log.info("부모id={}",parentCategory.getId());
                Category category = Category.builder()
                                    .id(id)
                                    .name(name)
                                    .parentCategory(parentCategory).build();

                return CategoryInfo.builder()
                        .entity(categoryRepository.save(category))
                        .build();

            }

            return CategoryInfo.builder()
                    .entity(categoryRepository
                    .save(Category
                            .builder()
                            .id(id)
                            .name(name)
                            .build()))
                    .build();
        }


이렇게 데이터를 추가하고 @Cacheable 어노테이션이 적용된 findByCategoryId(id)를 데이터를 조회하면 우리가 추가한 데이터가 나오지 않고 처음 findByCategoryId(id)에 의해 저장된 데이터만 있을 것이다. 이것 때문에 1시간정도 헤맨 것 같다. 당연하다. DB를 조회하지 않고 key가 id인 캐시를 조회하기 때문이다. 데이터가 추가 삭제 업데이트시 캐시를 삭제하고 다시 조회하면 저장된 값이 들어가 있을 것이다. 

위 create 메소드에 아래 어노테이션을 추가하자. 

    @CacheEvict(value = "category", key = "#parentId", condition = "#parentId!=null")

findByCategoryId(id) 메소드는 부모카테고리(루트)일 경우에만 동작하며 루트카테고리의 서브카테고리를 보여주기 위해 사용한다. 그렇게 때문에 루트카테고리(parentId=null)의 서브카테고리(parentId!=null)가 추가되면 키값이 parentId인 캐시가 삭제된다.

해당 어노테이션을 작성하면 아래와 같다.

    @CacheEvict(value = "category", key = "#parentId", condition = "#parentId!=null")
    @PostMapping("category")
    @Transactional
    public CategoryInfo create(@RequestParam String id, 
                               @RequestParam String name, 
                               @RequestParam(required = false) String parentId){

            .....

        }

등록 후 findByCategoryId(id)메소드가 실행되면 등록된 값도 포함해서 다시 캐시에 저장된다.
