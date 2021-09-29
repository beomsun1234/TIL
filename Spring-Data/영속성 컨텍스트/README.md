# 영속성 컨텍스트


## EntityManagerFactory와 EntityManager


![영속성컨텍스트](https://user-images.githubusercontent.com/68090443/135258699-b2fece9d-a474-4506-9f7d-333781b60f49.PNG)


- EntityManagerFactory는 고객의 요청이 올 때마다 (thread가 하나 생성될 때마다) EntityManager를 생성한다.
- EntityManager는 내부적으로 DB connection pool을 사용해서 DB에 접근한다.


    일반적으로 데이터베이스를 하나만 사용하는 어플리케이션은 하나의 엔티티 매니저 팩토리를 생성해 사용한다. 
    엔티티 매니저 팩토리는 이름 그대로 엔티티 매니저를 만드는 공장인데, 공장을 만드는 비용은 상당히 크다. 
    따라서 어플리케이션 전체에서 하나의 엔티티 매니저 팩토리를 공유하도록 설계되어 있다.


### - EntityManagerFactory


 	  //엔티티 매니저 팩토리 생성
      // META-INF/persistence.xml에서 이름이 name인 persistence-unit을 찾아서 엔티티 매니저 팩토리를 생성
      EntityManagerFactory emf = Persistence.createEntityManagerFatory("name");

- 만드는 비용이 상당히 큼.
- 엔티티 매니저 팩토리는 애플리케이션 전체에서 딱 한번 생성하고 공유해서 사용한다.
- 여러 스레드가 동시에 접근해도 안전하다.


      
### - EntityManager

    // 엔티티 매니저 생성, 비용이 거의 안든다.
    
    EntityManager em = emf.createEntityManager(); //엔티티 매니저 생성
    
- 여러 스레드가 동시에 접근하면 동시성 문제 발생
- 스레드간 절대 공유하면 안된다.
- 데이터베이스 연결이 필요한 시점까지 커넥션을 얻지 않는다.


#### 동시성(Concurrency)이란?

유저가 체감하기에는 동시에 수행하는 거 처럼 보이지만 사실은 유저가 체감할 수 없는 짧은 시간단위로 작업들을 번갈아가면서 수행하는 것이다.

예를 들면 싱글 코어에서 멀티 스레드를 구현하기 위해서 쓰이는 기법이다.
각 스레드들이 동시에 동작하는 거 같지만 알고 보면 스레드들이 아주 짧은 시간마다 번갈아가면서 작업을 수행하고 있는 것이다.


```요약```

    공장(엔티티 매니저 팩토리)에서 제품(엔티티 매니저)를 찍어내는 개념이라고 보면 될 것 같다.
    엔티티 매니저 팩토리는 엔티티 매니저와 달리 여러 스레드가 동시에 접근해도 안전하다.
    단순히 엔티티 매니저만 찍어대는 녀석이기 때문이다.

    비용도 보면 공장을 짓는 비용은 굉장히 크다.
    그래서 엔티티 매니저 팩토리는 DB 당 하나 밖에 사용하지 않는다.
    그에 비해 공장에서 제품을 찍어내는 것은 너무나도 당연하고 빈번하게 일어나는 일이기 때문에 비용이 엄청 크게 들지 않는다.

---

## 영속성 컨텍스트란?

영속성 컨텍스트란 엔티티를 영구 저장하는 환경 이라는 뜻이다.

	
    em.persist(member);
  
이 코드는 member 엔티티를 저장한다고 했었다. 하지만 정확하게 얘기하면 데이터베이스에 저장하는게 아니라 엔티티 매니저를 사용해서 회원 엔티티를 영속성 컨텍스트에 저장하는 코드다.

- 영속성 컨텍스트는 엔티티 매니저를 생성할 때 하나만 만들어진다. 
- 엔티티 매니저를 통해 영속성 컨텍스트에 접근하고 관리할 수 있다.


## 엔티티의 생명주기



|||
|------|---|
|비영속(new/transient)|영속성 컨텍스트와 전혀 관계가 없는 상태|
|영속(managed)|영속성 컨텍스트에 관리되는 상태|
|준영속(detached)|영속성 컨텍스트에 저장되었다가 분리된 상태|
|삭제(removed)|삭제된 상태|

### 비영속(new/transient)


![비영속](https://user-images.githubusercontent.com/68090443/135258779-499a27d5-dc1d-44f9-afc5-7811fba02158.PNG)


- 엔티티 객체를 생성.
- 순수한 객체 상태, 아직 저장하지 않음.
- 영속성 컨텍스트나 데이터베이스와 상관없음.


    	Member member = new Member();
    	member.setId(100L);
    	member.setUsername("회원1");


### 영속(managed)


![영속](https://user-images.githubusercontent.com/68090443/135258800-1a63a2f6-8206-404e-bfff-d493ccaa5eee.PNG)


- 엔티티 매니저를 통해 엔티티를 영속성 컨텍스트에 저장하면, 영속성 컨텍스트가 엔티티를 관리하므로 영속 상태가 된다.


- 영속상태 = 영속성 컨텍스트에 의해 관리된다는 뜻.

- em.find()나 JPQL를 사용해서 조회한 엔티티도 영속 상태.





		//객체 생성(비영속)
        Member member = new Member();
        member.setId(100L);
        member.setUsername("회원1");  
    	EntityManager em = entityManagerFactory.createEntityManager();
    	em.getTransaction().begin();
    	//
    	// 객체를 저장한 상태(영속)
    	em.persist(member);
        
        
    	회원 엔티티 : 비영속 상태 => 영속 상태



  영속 상태가 된다고 바로 DB에 쿼리가 날라가지 않는다. (즉, DB 저장 X)
    
    
    
    transaction.commit();
  
  
  트랜잭션의 commit 시점에 영속성 컨텍스트에 있는 정보들이 DB에 쿼리로 날라간다.


### 준영속(detached)

- 영속성 컨텍스트가 관리하던 영속 상태의 엔티티를 영속성 컨텍스트가 관리하지 않으면 준영속 상태가 된다.


	//  회원 엔티티를 영속성 컨텍스트에서 분리, 호출로 준영속 상태 명시적 호출
    em.detach()
    
    //영속성 컨텍스트를 닫음
    em.close()
    
    //영속성 컨텍스트 초기화
    em.clear()


### 삭제(removed)

- 엔티티를 영속성 컨텍스트와 데이터베이스에서 삭제


	em.remove(entity)


---

## 영속성 컨텍스트의 특징

### - 영속성 컨텍스트와 식별자 값

영속성 컨텍스트는 엔티티를 식별자 값(@Id로 테이블의 기본 키와 매핑한 값)으로 구분한다.
따라서 영속 상태는 식별자 값이 반드시 있어야 한다. 

식별자 같이 없으면 예외 발생

### - 영속성 컨텍스트와 데이터베이스 저장
 
JPA는 보통 트랜잭션을 커밋하는 순간 영속성 컨텍스트에 새로 저장된 엔티티를 데이터베이스에 반영한다. 이를 플러시(flush) 라고 한다.

### - 영속성 컨텍스트가 엔티티를 관리하면 얻게되는 장점
- 1차 캐시
- 동일성(identity) 보장
- 트랜잭션을 지원하는 쓰기 지연(transactional write-behind)
- 변경 감지(Dirty Checking)
- 지연 로딩(Lazy Loading)




## 엔티티 조회


![1차캐시](https://user-images.githubusercontent.com/68090443/135259043-e747f6db-281d-49ec-8c1a-66ed5acaf8d5.PNG)


- 영속성 컨텍스트는 내부에 캐시를 가지고 있다 => 1차 캐시
- 영속 상태의 엔티티는 모두 1차 캐시에 저장
 


    Member member = new Member();
	member.setId("member1");
	member.setUsername("회원1");

	em.persist(member);

 em.persist(member) 을 실행하게 되면 member 엔티티가 영속 상태가되고 1차캐시에 저장된다.
 
### 1차 캐시란?

    영속성 컨텍스트는 내부에 캐시를 가지고 있는데 이것을 1차 캐시라 한다. 
    영속 상태의 엔티티는 모두 이곳에 저장된다. 
    쉽게 말해 영속성 컨텍스트 내부에 Map이 하나 있는데 (1차 캐시), 
    키는 @Id로 매핑한 식별자고 값은 엔티티 인스턴스다.

- 식별자 값은 데이타베이스 기본 키와 매핑된다.
- 영속성 컨텍스트에 데이터를 저장하고 조회하는 모든 기준은 데이타베이스 기본 키 값이다.

<br>


### 엔티티 조회


 	Member findMember = em.find(Member.class, "member1");
    

- em.find() 호출 =>entityManager.find() 를 하면 DB보다 먼저 1차 캐시에서 엔티티 조회
- 엔티티가 1차 캐시에 없으면 데이터베이스 조회 후 해당 엔티티를 DB에서 꺼내와 1차 캐시에 저장 후 엔티티 반환 이후에 다시 해당 Entity를 조회하면 1차 캐시에 있는 Entity를 반환한다.



### 1차 캐시에서 조회


    Member member = new Member();
    member.setId("member1");
    member.setUsername("회원1");

    //1차 캐시에 저장
    em.persist(member);

    //1차 캐시에서 조회
    Member findMember = em.find(Member.class, "member1");


엔티티를 조회하는 find 메서드 실행 시


![find매서드실행시](https://user-images.githubusercontent.com/68090443/135259249-7aa7688c-5955-45d6-907c-a1399abdf7e7.PNG)



    1. 1차 캐시에서 식별자 값으로 엔티티를 찾는다.
    
    2. 만약 찾는 엔티티가 1차 캐시에 있으면 데이터베이스를 조회하지 않고 메모리에 있는 1차 캐시
       에서 엔티티를 조회
    
    3. 1차 캐시에 찾는 엔티티가 없으면 데이터베이스에서 조회



### 데이터베이스에서 조회

- em.find()를 호출했는데 엔티티가 1차 캐시에 없으면 엔티티 매니저는 데이터베이스를 조회해서 엔티티를 생성한다. 그리고 1차 캐시에 저장한 후에 영속 상태의 엔티티를 반환한다.



![db조회](https://user-images.githubusercontent.com/68090443/135259391-9efa33f0-c7da-483a-b071-fda9c6b7f603.PNG)


1. em.find(Member.class, "member2")를 실행한다
2. 현재 1차 캐시에는 member1만 있고, member2는 없는 상태이므로 -> DB에서 member2를 조회한다
3. 조회한 데이터로 member2 엔티티를 생성해서 1차 캐시에 저장한다(영속 상태)
4. 조회한 엔티티를 반환한다

이후 member1나, member2에 대해 find를 요청하면 DB에 접근하지 않고, 1차 캐시에 있는 엔티티를 반환 한다.

### 사실 1차 캐시는 큰 성능 이점을 가지고 있지 않다.

EntityManager는 Transaction 단위로 만들고 해당 DB Transaction이 끝날 때 (사용자의 요청에 대한 비지니스가 끝날 때) 같이 종료된다.
즉, 1차 캐시도 모두 날라가기 때문에 굉장히 짧은 찰나의 순간에만 이득이 있다. (DB의 한 Transaction 안에서만 효과가 있다.)
하지만, 비지니스 로직이 굉장히 복잡한 경우에는 효과가 있다.

즉 한 트랜잭션 안에서만 효과가 있기 때문이다.

### 영속 엔티티의 동일성 보장

    Member a = em.find(Member.class, "member1");
    Member b = em.find(Member.class, "member1");

	System.out.println(a == b); // 동일성 비교
    
	현재 member1이 영속성 컨텍스트에 존재하는 상황에서
	위 코드의 a == b 가 참일까 거짓일까?

``정답은 참이다.``

왜 같을까??

``영속성 컨텍스트는 1차 캐시에 있는 같은 엔티티 인스턴스를 반환하기 때문이다.(하나의 Transaction 안에서 같은 Entity 비교 시 true) ``



만약 영속성 컨텍스트에 member1이 없는데 위 코드를 실행하면 결과는 어떨까? 결과는 같다.

    처음 member1에 대한 find 요청 시 엔티티 매니저는 데이터베이스에서 
    member1을 조회해서 1차 캐시에 저장하고 반환한다. 
    
    두번째 find 요청시에는 영속성 컨텍스트가 1차 캐시에 있는 member1 엔티티 인스턴스를 반환하므로 같은 결과가 된다.


영속성 컨텍스트는 성능상 이점과 엔티티의 동일성을 보장한다.

---

## 엔티티 등록

엔티티를 영속성 컨텍스트에 등록하는 코드

    EntityManager em = emf.createEntityManager();
    EntityTransaction transaction = em.getTransaction();

    // 엔티티 매니저는 데이터 변경 시 트랜잭션을 시작해야 한다.
    transaction.begin();    // 트랜잭션 시작

    em.persist(memberA);
    em.persist(memberB);
    // 여기까지 INSERT SQL을 데이터베이스에 보내지 않는다.

    // 커밋하는 순간 데이터베이스에 INSERT SQL을 보낸다.
    transaction.commit();   // 트랜잭션 커밋
    
    

![엔티티 등록](https://user-images.githubusercontent.com/68090443/135259469-2238d5a5-d0cd-4f61-98a8-073430d079dc.PNG)



- 엔티티 매니저는 트랜잭션을 커밋하기 직전까지 데이터베이스의 엔티티를 저장하지 않는다.
- 내부 쿼리 저장소에 INSERT SQL을 차곡차곡 모아둔다.
- 트랜잭션 커밋할 때 모아둔 쿼리를 데이터베이스에 보내서 저장시킨다.

이를 트랜잭션을 지원하는 쓰기 지연이라 한다.

### 트랜잭션을 지원하는 쓰기 지연


![엔티티 등록](https://user-images.githubusercontent.com/68090443/135259669-6ea43584-315b-4782-bfeb-927caa20c6a6.PNG)


em.persist(memberA) 실행 시, 영속성 컨텍스트는 1차 캐시에 memberA에 대한 엔티티를 저장하면서 동시에 JPA가 이 entity를 분석해서 쓰기 지연 SQL 저장소에 INSERT 쿼리를 저장한다. DB에 바로 저장하지(INSERT 쿼리) 않고 기다린다.



![엔티티등록B](https://user-images.githubusercontent.com/68090443/135259748-de645ea9-6af9-4f5c-9e5a-e89870afdf9c.PNG)


em.persist(memberB)도 동일하다.



![커밋시](https://user-images.githubusercontent.com/68090443/135259780-22c0c03f-39de-4faf-a1e4-8e95d7853cd8.PNG)



transaction.commit() 실행 시, 쓰기 지연 SQL 저장소에 저장된 쿼리들을 DB로 날린다. [ flush(), 1차 캐시 삭제 x ]
flush() 후에 실제 DB Transaction이 커밋된다.



트랜잭션 범위 안에서 실행.
등록 쿼리를 그때 그때 데이타베이스에 전달해도 트랜잭션을 커밋하지 않으면 아무 소용이 없음

#### 플러시(flush)
    영속성 컨텍스트의 변경 내용을 데이터베이스에 동기화하는 작업이다.
    이때 등록, 수정, 삭제한 엔티티를 데이터베이스에 반영한다.


---

## 엔티티 수정

### 변경 감지

변경 감지는 엔티티의 변경사항을 데이터베이스에 자동으로 반영하는 기능이다.



    EntityManager em = emf.createEntityManager();
    EntityTransaction transaction = em.getTransaction();
    transaction.begin() // 트랜잭션 시작

    // 영속 엔티티 조회
    Member memberA = em.find(Member.class, "memberA");

    // 영속 엔티티 데이터 수정
    memberA.setUsername("hi");
    memberA.setAge(10);

    transaction.commit(); // 트랜잭션 커밋



엔티티 데이터 수정 시 update()나 persist()로 영속성 컨텍스트에 해당 데이터를 업데이트 해달라고 알려줘야 하지 않을까?

정답은 NO이다.

    엔티티 데이터만 수정하고 commit 하면 알아서 DB에 반영된다.
    즉, 데이터를 set하면 해당 데이터의 변경을 감지하여 자동으로 UPDATE Query가 나가는 것이다.



![변경감지](https://user-images.githubusercontent.com/68090443/135259603-cc96810a-f227-4894-902a-4931f5bd3872.PNG)



Snapshot: 영속성 컨텍스트에 최초로 값이 들어왔을 때의 상태값을 저장한다.

- 매커니즘


      1. transaction.commit() 실행 시 엔티티 매니저 내부에서 먼저 플러시(flush())가 호출된다.
      2. 엔티티와 스냅샷을 비교해서 변경된 엔티티를 찾는다.
      3. 변경된 엔티티가 있으면 수정 쿼리를 생성해서 쓰기 지연 SQL 저장소에 보낸다.
      4. 쓰기 지연 저장소의 SQL을 데이터베이스에 보낸다.
      5. 데이터베이스 트랜잭션을 커밋한다.




-  ```주의```


      변경 감지는 영속성 컨텍스트가 관리하는 영속 상태의 엔티티에만 적용된다
      비영속, 준영속처럼 영속성 컨텍스트의 관리를 받지 못하는 엔티티는 값을 변경해도 데이터베이스에 반영되지 않는다


그럼 변경 감지로 인해 실행된 UPDATE SQL의 쿼리는 변경된 부분만 수정 쿼리가 생성될까?

아니다.
JPA의 기본 전략은 엔티티의 모든 필드를 업데이트 한다. 모든 필드를 업데이트하면 데이터베이스에 보내는 데이터 전송량이 증가하는 단점이 있지만, 다음과 같은 장점으로 인해 모든 필드를 업데이트 한다.

모든 필드를 사용하면 수정 쿼리가 항상 같다. 따라서 애플리케이션 로딩 시점에 수정 쿼리를 미리 생성해두고 재사용할 수 있다.
데이터베이스에 동일한 쿼리를 보내면 데이터베이스는 이전에 한 번 파싱된 쿼리를 재사용할 수 있다.

- 변경 감지로 생성되는 update 쿼리는 기본적으로 모든 필드를 업데이트한다.
- @DynamicUpdate를 통해 엔티티 수정 시 변경된 필드만 반영되도록 할 수 있다.



### 엔티티 삭제


    Member memberA = em.find(Member.class, "memberA");
    em.remove(memberA);


em.remove()에 삭제 대상 엔티티를 넘겨주면 엔티티를 삭제한다.

티티를 즉시 삭제하는 것이 아니라, 엔티티 등록과 비슷하게 삭제 쿼리를 쓰기 지연 SQL 저장소에 등록한다.
이후 트랜잭션을 커밋해서 플러시를 호출하면 실제 데이터베이스에 삭제 쿼리를 전달한다.

em.remove(memberA)를 호출하는 순간 memberA는 영속성 컨텍스트에서 제거된다.





### 플러시

플러시(flush())는 영속성 컨텍스트의 변경 내용을 데이터베이스에 반영한다.
플러시를 실행하면 다음과 같은 일이 일어난다.


    1. 변경 감지가 동작해서 영속성 컨텍스트에 있는 모든 엔티티를 스냅샷과 비교해서 수정된 엔티티를 찾는다.
    2. 수정된 엔티티는 수정 쿼리를 만들어 쓰기 지연 SQL 저장소에 등록한다.
    3. 쓰기 지연 SQL 저장소의 쿼리를 데이터베이스에 전송한다.(등록, 수정, 삭제 쿼리)

- 영속성 컨텍스트를 비우지는 않는다.
- 영속성 컨텍스트의 변경내용을 데이터베이스에 동기화


#### 속성 컨텍스트를 플러시 하는 3가지 방법

 1. em.flush() - 직접 호출
 
    엔티티 매니저의 flush() 메서드를 직접 호출해서 영속성 컨텍스트를 강제로 플러시한다.

 2. 트랜잭션 커밋 - 플러시 자동 호출
 
    데이터베이스에 변경 내용을 SQL로 전달하지 않고 트랜잭션만 커밋하면 어떤 데이터도 데이터베이스에 반영되지 않는다. 따라서 트랜잭션을 커밋하기 전에 꼭 플러시를 호출해서 영속성 컨텍스트의 변경 내용을 데이터베이스에 반영해야 한다. JPA는 이런 문제를 예방하기 위해 트랜잭션을 커밋할 때 플러시를 자동으로 호출한다.

   
 3.  JPQL 쿼리 실행 - 플러시 자동 호출
    
    em.persist(memberA);
	em.persist(memberB);
	em.persist(memberC);

	// 중간에 JPQL 실행
	query = entityManager.createQuery("select m from Member m", Member.class);
	List<Member> members = query.getResultList();

- Q. memberA, B, C 를 영속성 컨텍스트에 저장한 상태에서 바로 조회하면 조회가 될까?

조회가 되지 않는다.

    DB 에 Query로도 날라가야 반영이 될텐데 INSERT Query 자체가 날라가지 않은 상태이다. 
    이런 상태에서 JPQL로 DB에서 가져오는 SELECT Query 요청을 한 것이므로 당연히 조회되지 않는다.
    JPQL은 SQL로 번역이 돼서 실행되는 것이다.
    이 때문에 JPA의 기본 모드는 JPQL 쿼리 실행 시 flush()를 자동으로 날린다.
    즉, JPQL 쿼리 실행 시 플러시 자동 호출로 인해 위의 코드는 조회가 가능하다.


한번 더 기억!!! JPQL이나 Criteria 같은 객체지향 쿼리를 호출할 때도 플러시가 실행된다!!!!





#### 플러시 모드 옵션

    FlushModeType.AUTO: 커밋이나 쿼리를 실행할 때 플러시(기본값)
    FlushModeType.COMMIT: 커밋할 때만 플러시
    
    JPQL 쿼리 실행시 플러시가 자동으로 일어나는데, 만약 JPQL에서 사용할 테이블이 이전 작업들과 전혀 관련이 없다면 이 옵션으로 플러시를 커밋할 때로 변경할 수 있다.
