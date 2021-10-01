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

 
 
 ![저장](https://user-images.githubusercontent.com/68090443/135084513-9a1e195e-e190-4122-824f-163980d87b52.PNG)


- Member 엔티티를 분석한다.
- INSERT SQL을 생성한다.
- JDBC API를 사용하여 SQL을 DB에 날린다.
 


### - 조회

  

![조회](https://user-images.githubusercontent.com/68090443/135084695-4fc70f11-18ea-4bb2-8356-b2b2f9e1b18f.PNG)



- JPA에게 PK값으로 find 요청
- JPA는 SELECT query 생성
- JDBC API를 통해 DB에 보내고 결과를 받음
- ResultSet 매핑
- 패러다임 불일치 해결



## JPA를 왜 사용해야 하는가?

####  - SQL 중심적인 개발에서 객체 중심으로 개발
#### - 생산성

JPA를 사용하는것은 마치 Java Collection에 데이터를 넣었다 빼는 것처럼 사용할 수 있게 만드는 것이다.


      간단한 CRUD

      저장 : jpa.persist(member)
      조회 : Member member = jpa.find(memberId)
      수정 : member.setName("변경할 이름")
      삭제 : jpa.remove(member)


#### - 유지보수

기존 : 필드 변경시 모든 SQL을 수정해야 한다.

        - CRUD의 반복
         
        자바객체를 SQL로 , SQL을 자바 객체로 
        변환하는 과정의 반복
        예를들어 회원의 나이정보를 추가하고자
        한다. Member클래스에 나이 필드 추가와 
        insert,select, update등 모든 쿼리에 나이 
        정보를 추가한다.
        
        - 패러다임의 불일치
        
		객체는 필드와 메서드를 잘 캡슐화해서 사용하는 것이, RDBMS는 데이터를 잘 정규화 해서 저장하는 것이 목표다.
        즉 서로 다른 성격이기 때문에 사용하기가 힘들다. 
        결국 개발자가 SQL 매퍼의 일을 하게 된다.
        
```JPA는 필드만 추가하면 된다. SQL은 JPA가 처리하기 때문에 손댈 것이 없다.```

#### - Object와 RDB간의 패러다임 불일치 해결



![과계](https://user-images.githubusercontent.com/68090443/135084467-dc25c4a0-6486-4a95-8b25-9f17f58137d1.PNG)



#### 저장 

위의 상속관계에서 Album 객체를 저장한다고 생각해보자. INSERT 쿼리가 두번 만들어져서 날라간다.

    INSERT INTO ITEM ...

    INSERT INTO ALBUM ...

<br>

    jpa.persist(album); 
    
 JPA persistant 객체에 Album 객체 저장하면. 알아서 INSERT 쿼리 두개 만들어서 넣는다. 단순하게 INSERT 쿼리 두벌 만들어서 DB에 넣는게 아니라 패러다임의 불일치 자체를 해결한다.알아서 두개 클래스에 다 넣어준다.
 
 
 
#### 조회

	jpa.find(Album.class, albumId);

JPA를 통해서 Album 객체를 조회하게 되면, Item과 Album객체를 이쁘게 조인 쿼리를 날려서 가져오고, Album 객체를 반환한다.


```쿼리를 JPA가 만들어 주기 때문에 Object와 RDB간의 패러다임 불일치를 해결할 수 있다.```


## JPA와 연관관계, 객체 그래프 탐색

### 연관관계
- 객체는 참조를 사용해서 다른 객체와 연관관계를 가지고 참조에 접근해서 연관된 객체를 조회
- 테이블은 외래 키를 사용해서 다른 테이블과 연관관계를 가지고 조인을 사용해서 연관된 테이블을 조회

#### 객체를 테이블에 맞춰 모델링

- 관계형 데이터베이스 방식에 맞추면 Member 객체와 연관된 Team 객체를 참조를 통해서 조회할 수 없다.
- 좋은 객체 모델링은 기대하기 어렵고 결국 객체지향의 특징을 잃어버린다.


    class Member {

        String id;      // MEMBER_ID 컬럼 사용
        Long teamId;    // TEAM_ID FK 컬럼 사용
        String userName;
    }

    class Team {

        Long id;        // TEAM_ID PK 사용
        String name;
    }
    
#### 객체지향 모델링

- 객체지향 모델링을 사용하면 객체를 테이블에 저장하거나 조회하기는 쉽지 않다.
- 객체 모델은 외래 키가 필요 없고 단지 참조만 있으면 된다.
- 테이블은 참조가 필요 없고 외래 키만 있으면 된다.

결국, 개발자가 중간에서 변환 역활을 해야 한다.
관계형 데이터베이스 방식에 맞추면 Member 객체와 연관된 Team 객체를 참조를 통해서 조회할 수 없다.
좋은 객체 모델링은 기대하기 어렵고 결국 객체지향의 특징을 잃어버린다.


    // 참조를 사용하는 객체 모델
    class Member {
        String id;
        Team team;          // 참조로 연관관계를 맺는다.
        String username;

        Team getTeam() {
            return team;
        }
    }

    class Team {
        Long id;
        String name;
    }
    
#### JPA와 연관관계

JPA는 연관관계와 관련한 패러다임 불일치 문제 를 해결해준다.

    member.setTeam(team);   // 회원과 팀 연관관계 설정
    jap.persist(member);    // 회원과 연관관계 함께 저장
    
    객체를 조회할 때 외래 키를 참조로 변환하는 일도 JPA가 처리

    Member member = jpa.find(Member.class, memberId);
    Team team = member.getTeam();

#### 객체 그래프 탐색

객체에서 회원이 소속된 팀을 조회할 때 참조를 사용해서 연관된 팀을 찾으면 되는데 이것을 "객체 그래프 탐색"이라 한다.

JPA를 통해서 가져오는 경우
객체 그래프를 완전히 자유롭게 탐색할 수 있게 된다.

	Member member = jpa.find(Member.class, memberId);
	Team team = member.getTeam();
    
연관 관계를 저장하고, 가져올 때는 마치 java collection에 넣었던 것처럼 꺼내올 수 있다.



	 Member member1 = memberDAO.find(memberId);
     
     member1.getTeam(); // 엔티티를 신뢰할 수 없음 
     member1.getOrder().getDelivery(); 

내가 아닌 다른 개발자가 직접 구현한 DAO에서 가져오는 경우
DAO에서 직접 어떤 쿼리를 날렸는지 확인하지 않는 이상, 그래프 형태의 관련된 객체들을 모두 잘 가져왔는지 알 수가 없다.
즉, 반환한 엔티티를 신뢰하고 사용할 수 없다.


## 지연 로딩과 즉시 로딩

#### 지연로딩(Lazy Loading)


![지연ㄴ로딩](https://user-images.githubusercontent.com/68090443/135256067-e9dccb3c-f97c-4a90-8ee9-93770eb310e2.PNG)


- 객체가 실제 사용될 때 로딩






    memberDAO.find(memberId)에서는 Member 객체에 대한 SELECT 쿼리만 날린다.

    Team team = member.getTeam()로 Team 객체를 가져온 후에 team.getName()처럼 값이 실제로 필요한 시점에 JPA가 Team에 대한 SELECT 쿼리를 날린다.
    
    Member를 사용하는 경우에 대부분 Team도 같이 필요하다면 즉시 로딩을 사용한다.
    

```즉,필요한 시점에 쿼리를 날려 값을 가져온다.```

#### 즉시로딩


![즉시로딩](https://user-images.githubusercontent.com/68090443/135256087-faa327d6-f94f-4091-a943-62942ac94664.PNG)



- JOIN SQL로 한번에 연관된 객체까지 미리 조회

- Join을 통해 항상 연관된 모든 객체를 같이 가져온다.

- member를 조회 했을 때, member와 연관된 객체까지 모두 가져온다.


애플리케이션 개발할 때는 모두 지연 로딩으로 설정한 후에, 성능 최적화가 필요할 때에 옵션을 변경하는 것을 추천한다.

