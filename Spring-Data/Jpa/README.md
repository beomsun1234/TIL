## JPA
- JPA란 자바 ORM 기술에 대한 API 표준 명세를 의미한다.
- 자바 진영의 ORM 기술 표준
- 이 JPA를 Spring에서 쓸수 있도록 한 것이 Spring Data JPA 이다.
- 자바 어플리케이션에서 관계형 데이터베이스를 사용하는 방식을 정의한 인터페이스이다.(특정 기능을 하는 라이브러리가 아니다)
- JPA를 사용하기 위해서는 JPA를 구현한 Hibernate, EclipseLink, DataNucleus 같은 ORM 프레임워크를 사용해야 한다.


![jpa](https://user-images.githubusercontent.com/68090443/135080272-0a7cdf92-91ad-4d53-b0c0-1551f261b2ce.PNG)



#### Hibernate란?

    하이버네이트는 JPA 구현체의 한 종류입니다. 

    JPA는 자바에서 제공하는 인터페이스로 ORM 기술에 대한 명세서라고 했습니다.

    이 JPA 인터페이스를 구현한 것이 하이버네이트입니다. 

#### spring-data-jpa란?

	Spring-Data-JPA는 JPA를 쉽게 사용하기 위해 스프링에서 제공하고 있는 모듈이다.
    
    이는 JPA를 한 단계 추상화시킨 Repository라는 인터페이스를 제공함으로써 이루어진다. 
    사용자가 Repository 인터페이스에 정해진 규칙대로 메소드를 입력하면, 
    Spring이 알아서 해당 메소드 이름에 적합한 쿼리를 날리는 구현체를 만들어서 Bean으로 등록해준다.
    
    
    
추상화 정도는 Spring-Data-JPA -> Hibernate -> JPA 이다.


## ORM (Object Relational Mapping)
ORM이란 객체와 DB의 테이블이 매핑을 이루는 것을 말합니다. 즉, 객체가 테이블이 되도록 매핑 시켜주는 것을 말합니다.

- 객체는 객체대로 설계하고 관계형 데이터베이스는 관계형 데이터베이스대로 설계한다
- ORM프레임워크가 중간에서 매핑해준다
- ORM은 객체와 RDB 두 기둥 위에 있는 기술이다.
- 대중적인 언어에는 대부분 ORM 기술이 존재


#### ORM의 장점
- 객체 지향적으로 데이터를 관리하기 때문에 비즈니스 로직에 집중할 수 있고, 객체지향 개발이 가능하다
- 유지보수성
- 벤더 독립성

#### ORM의 단점

- 학습 비용이 많다. 어렵다.
- 제대로 사용하지 않으면 성능 이슈가 발생하고 데이터 손실이 발생할 수 있다.

---


## JPA 동작 과정


![동작과정](https://user-images.githubusercontent.com/68090443/135084318-5d46c485-29ef-4cfc-b52d-a5a76ce6ebec.PNG)


JPA는 애플리케이션과 JDBC 사이에서 동작한다.
개발자가 JPA를 사용하면 JPA내부에서 JDBC API를 사용하여 SQL을 호출하여 DB와 통신한다.
개발자가 직접 JDBC API를 쓰는 것이 아니다.

```JPA가 SQL을 직접 작성하지 않는다고 해서 JDBC API를 사용하지 않는다는 것은 아닙니다 Hibernate가 지원하는 메서드 내부에서는 JDBC API가 동작하고 있으며, 단지 개발자가 직접 SQL을 직접 작성하지 않을 뿐입니다```





### - 저장

![과계](https://user-images.githubusercontent.com/68090443/135084467-dc25c4a0-6486-4a95-8b25-9f17f58137d1.PNG)


위의 상속관계에서 Album 객체를 저장한다고 생각해보자. INSERT 쿼리가 두번 만들어져서 날라간다.

    INSERT INTO ITEM ...

    INSERT INTO ALBUM ...

<br>

    jpa.persist(album); 
    
 JPA persistant 객체에 Album 객체 저장하면. 알아서 INSERT 쿼리 두개 만들어서 넣는다. 단순하게 INSERT 쿼리 두벌 만들어서 DB에 넣는게 아니라 패러다임의 불일치 자체를 해결한다.알아서 두개 클래스에 다 넣어준다.
 
 
 ![저장](https://user-images.githubusercontent.com/68090443/135084513-9a1e195e-e190-4122-824f-163980d87b52.PNG)


- Member 엔티티를 분석한다.
- INSERT SQL을 생성한다.
- JDBC API를 사용하여 SQL을 DB에 날린다.
 


### - 조회

    jpa.find(Album.class, albumId);

JPA를 통해서 Album 객체를 조회하게 되면, Item과 Album객체를 이쁘게 조인 쿼리를 날려서 가져오고, Album 객체를 반환한다.


![조회](https://user-images.githubusercontent.com/68090443/135084695-4fc70f11-18ea-4bb2-8356-b2b2f9e1b18f.PNG)



- JPA에게 PK값으로 find 요청
- JPA는 SELECT query 생성
- JDBC API를 통해 DB에 보내고 결과를 받음
- ResultSet 매핑
- 패러다임 불일치 해결



## JPA를 왜 사용해야 하는가?

- SQL 중심적인 개발에서 객체 중심으로 개발
- 생산성

JPA를 사용하는것은 마치 Java Collection에 데이터를 넣었다 빼는 것처럼 사용할 수 있게 만드는 것이다.


      간단한 CRUD

      저장 : jpa.persist(member)
      조회 : Member member = jpa.find(memberId)
      수정 : member.setName("변경할 이름")
      삭제 : jpa.remove(member)


- 유지보수

기존 : 필드 변경시 모든 SQL을 수정해야 한다.

        CRUD의 반복
        자바객체를 SQL로 , SQL을 자바 객체로 
        변환하는 과정의 반복
        예를들어 회원의 나이정보를 추가하고자
        한다. Member클래스에 나이 필드 추가와 
        insert,select, update등 모든 쿼리에 나이 
        정보를 추가한다.
        
```JPA는 필드만 추가하면 된다. SQL은 JPA가 처리하기 때문에 손댈 것이 없다.```

- Object와 RDB간의 패러다임 불일치 해결

쿼리를 JPA가 만들어 주기 때문에 Object와 RDB간의 패러다임 불일치를 해결할 수 있다.
