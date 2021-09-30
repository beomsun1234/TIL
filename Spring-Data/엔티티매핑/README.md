# 엔티티 매핑

JPA를 사용하는 데 가장 중요한 일은 엔티티와 테이블을 정확하게 매핑하는 것이다.
따라서 매핑 어노테이션을 숙지하고 사용해야 합니다. JPA는 다양한 매핑 어노테이션을 지원하는데 크게 4가지로 분류할 수 있다.

## 객체와 테이블 매핑

###	@Entity
    
- JPA를 사용해서 테이블과 매핑할 클래스는 @Entity 어노테이션을 필수로 붙여야 한다. 
- @Entity 어노테이션을 클래스에 선언하면 그 클래스는 JPA가 관리한다


 ```@Entity가 붙은 클래스에는 다음 제약사항이 필요하다.```

- 필드에 final, enum, interface, class를 사용할 수 없다.
- 생성자중 기본 생성자가 반드시 필요하다.(파라미터가 없는 public 또는 protected 생성자)


 @Entity의 속성
 
	 name : 엔티티 이름을 지정합니다. 기본값으로 클래스 이름을 그대로 사용한다.



### @Table

- @Table 어노테이션은 맵핑할 테이블을 지정한다. 생략시 매핑한 엔티티 이름을 테이블 이름으로 사용한다.

@Table의 속성

     name : 매핑할 테이블의 이름을 지정
     
     catalog : DB의 catalog를 맵핑
     
     schema : DB 스키마와 맵핑
     
     uniqueConstraint : DDL 쿼리를 작성할 때 제약 조건을 생성


---

### 데이터베이스 스키마 자동 생성

JPA는 데이터베이스 스키마를 자동으로 생성하는 기능을 지원한다. (애플리케이션 실행 시점에 자동 생성)

JPA는 데이터베이스 방언을 활용해서 데이터베이스에 맞는 적절한 DDL을 생성한다.
하지만 이렇게 생성된 DDL은 개발 장비에서만 사용해야 한다. 생성된 DDL은 운영서버에서는 사용하지 않거나, 적절히 다듬고 사용해야 한다.

#### hibernate.hbm2ddl.auto 속성

    create : 기존 테이블을 삭제하고 새로 생성한다. DROP + CREATE
    
    create-drop	: 속성에 추가로 애플리케이션을 종료할 때 생성한 DDL을 제거한다. DROP + CREATE + DROP
    
    update : 데이터베이스 테이블과 엔티티 매핑정보를 비교해서 변경 사항만 수정한다.
    
    validate : 데이터베이스 테이블과 엔티티 매핑정보를 비교해서 차이가 있으면 경고를 남기고 애플리케이션을 실행하지 않는다. 이 설정은 DDL을 수정하지 않는다.
    
    none : 자동 생성 기능을 사용하지 않으려면 hibernate.hbm2ddl.auto 속성 자체를 삭제하거나 유효하지 않은 옵션 값을 주면 된다(참고로 none은 유효하지 않은 옵션 값)



```주의```

-운영 장비에는 절대 create, create-drop, update를 사용하면 안된다!.이 옵션들은 운영 중인 데이터베이스의 테이블이나 컬럼을 삭제할 수 있기 때문!!

- 개발 초기 단계는 create 또는 update 사용
- 테스트 서버는 update 또는 validate 사용
- 스테이징과 운영 서버는 validate 또는 none 사용
profile 

---

## 기본키 매핑

- 직접 할당: 기본 키를 애플리케이션에서 직접 할당, @Id만 사용
- 자동 생성(GeneratedValue): 대리 키 사용 방식


          IDENTITY: 기본 키 생성을 데이터베이스에 위임한다, MySQL -> Auto_Increment
      
          SEQUENCE: 데이터베이스 시퀀스 오브젝트 사용(ORACLE). @SequenceGenerator 필요
      
          TABLE: 키 생성 테이블을 사용한다. 모든 DB에서 사용. @TableGenerator 필요
      
          AUTO: 방언에 따라 자동 지정, 기본 값



### IDENTITY

- IDENTITY는 기본 키 생성을 데이터베이스에 위임하는 전략
- 주로 MySQL, PostgreSQL, SQL Server, DB2에서 사용된다. 
- 데이터베이스에 값을 저장하고 나서야 기본 키 값을 구할 수 있을 때 사용

@GeneratedValue(strategy = GenerationType.IDENTITY)



    @Entity
    public class Member{

     @Id
     @GeneratedValue(strategy = GenerationType.IDENTITY)
     private Long id;
     ...
     }

<br>

	private static void logic(EntityManager em) {
 	Member member = new Member();
 	em.persist(member);
 	System.out.println("member.id = " + member.getId());
	}
	// 출력: member.id = 1
    

##### 트랜잭션을 커밋하지 않았는데 자동생성된 기본키 값을 사용하지 못하나?? IDENTITY 사용시 영속성 컨텍스트는 어떻게 관리 되고 있을까??

우선 결론은 사용할 수 있다.


JPA 는 @GeneratedValue(strategy = GenerationType.IDENTITY) 에 한하여 플로우를 변경한다.

@GeneratedValue(strategy = GenerationType.IDENTITY) 사용했을 때,

    transaction.commit()을 호출할 때가 아니라 em.persist(member); 가 호출될 때 
    바로 DB에 insert 쿼리 를 날리고 JPA 내부에서 Insert 쿼리 실행 후 
    생성된 id 값을 리턴 받는다. 이후 Id 를 PK 로 영속성 컨텍스트에 저장한다.

요약하자면 ```먼저 엔티티를 데이터베이스에 저장한 후에 식별자를 조회해서 엔티티의 식별자에 할당한다.```

### SEQUENCE

- 데이터베이스 시퀀스는 유일한 값을 순서대로 생성하는 특별한 데이터베이스 오브젝트이다. 
- SEQUENCE 전략은 이 시퀀스를 사용해서 기본 키를 생성. 
- 시퀀스를 지원하는 오라클, PostgreSQL, DB2, H2 데이터베이스에 사용된다.

 시퀀스 DDL

    CREATE TABLE MEMBER (
        ID BIGINT NOT NULL PRIMARY KEY,
       DATA VARCHAR(255)
    )

 시퀀스 생성
 
	CREATE SEQUENCE MEMBER_SEQ START WITH 1 INCREMENT BY 1;
    
 시퀀스 매핑 코드
 
    @Entity
    @SequenceGenerator(
     name = "MEMBER_SEQ_GENERATOR",
     sequenceName = "MEMBER_SEQ", //매핑할 데이터베이스 시퀀스 이름
     initialValue = 1, allocationSize = 1)
    public class Member{

     @Id
     @GeneratedValue(strategy = GenerationType.SEQUENCE,
                     generator = "MEMBER_SEQ_GENERATOR")
     private Long id;
     ...
     }
     
 시퀀스 사용 코드
 
    private static void logic(EntityManager em) {
     Member member = new Member();
     em.persist(member);
     System.out.println("member.id = " + member.getId());
    }
    // 출력: member.id = 1


- 시퀀스 사용 코드는 IDENTITY 전략과 같지만 내부 동작 방식은 다르다.
- SEQUENCE 전략
 
      -em.persist()를 호출할 때 먼저 데이터베이스 시퀀스를 사용해서 식별자를 조회한다.
      그리고 조회한 식별자를 엔티티에 할당한 후에 엔티티를 영속성 컨텍스트에 저장한다. 
      이후 트랜잭션을 커밋해서 플러시가 일어나면 엔티티를 데이터베이스에 저장한다.


@SequenceGenerator 속성

    name : 식별자 생성기 이름 -> 필수
    sequenceName : 데이터베이스에 등록되어 있는 시퀀스 이름	기본값 -> hibernate_sequence
    
    initialValue : DDL 생성 시에만 사용됨. 시퀀스 DDL을 생성할 때 처음 시작하는 수를 지정한다.	기본값 -> 1
    
    allocationSize : 시퀀스 한 번 호출에 증가하는 수(성능 최적화에 사용) 기본값 -> 50
    catalog, schema : 데이터베이스 catalog, schema 이름

---
## 필드와 컬럼 매핑

### @Column

- @Column 어노테이션은 객체 필드와 DB 테이블 컬럼을 맵핑한다.

@Column의 속성

   	name : 맵핑할 테이블의 컬럼 이름을 지정
    
    insertable : 엔티티 저장시 선언된 필드도 같이 저장
    
    updateable : 엔티티 수정시 이 필드를 함께 수정
    
    table : 지정한 필드를 다른 테이블에 맵핑
    
    nullable : NULL을 허용할지, 허용하지 않을지 결정
    
    unique : 제약조건을 걸 때 사용
    
    columnDefinition : DB 컬럼 정보를 직접적으로 지정할 때 사용
    
    length : varchar의 길이를 조정합니다. 기본값으로 255가 입력
    
    precsion, scale : BigInteger, BigDecimal 타입에서 사용, 각각 소수점 포함 자리수, 소수의 자리수를 의미
    
##### @Column을 생략한다면?

    컬럼 어노테이션을 생략하면 대부분 @Column 속성의 기본값이 적용되는데, 자바 기본 타입일 때는 nullable 속성에 예외가 있다.
    @Column 생략 시: 객체 타입일 때는 nullable이 기본값인 true가 되지만, 자바 기본 타입일 때는 JPA가 not null 제약조건을 추가한다.
    @Column 사용 시: 자바 기본 타입에 대해 not null 제약조건을 추가하지 않습니다. 따라서 자바 기본 타입에 @Column을 사용하면 nullable = false로 지정하는 것이 안전하다.
    

### @Enumerated

자바의 enum 타입을 매핑할 때 사용

|속성|기능|기본값|
|------|---|---|
|value|EnumType.ORDINAL: enum 순서를 데이터베이스에 저장, EnumType.STRING: enum 이름을 데이터베이스에 저장|EnumType.ORDINAL|

```기본값인 ORDINAL은 enum의 순서가 바뀌면 안되므로 EnumType.STRING을 권장한다.```


	 @Entity
     public class Member{
     
	   ...
       @Enumberated(EnumType.STRING) 
       @Column(nullable = false) 
       private Role role;
       ...
     
     }
    



Enum클래스 Role생성 


    public enum Role {
        GUEST("ROLE_GUEST", "손님"),
        USER("ROLE_USER", "일반사용자"); 

        private final String key; 
        private final String title; 
    }




### @Access

JPA가 엔티티 데이터에 접근하는 방식을 지정

    필드 접근: AccessType.FIELD는 필드에 직접 접근합니다. 필드 접근 권한이 private이어도 접근할 수 있다.

    프로퍼티 접근: AccessType.PROPERTY로 지정합니다. 접근자(getter)를 사용
