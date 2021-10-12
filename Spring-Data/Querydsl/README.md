# QueryDSL 
	
    Querydsl 정적 타입을 이용해서 SQL과 같은 쿼리를 생성할 수 있도록 해 주는 프레임워크다. 
    문자열로 작성하거나 XML 파일에 쿼리를 작성하는 대신, 
    Querydsl이 제공하는 플루언트(Fluent) API를 이용해서 쿼리를 생성할 수 있다.

즉 SQL, JPQL을 코드로 작성할 수 있도록 도와주는 빌더 API

   
### 사용 목적

    Querydsl은 타입에 안전한 방식으로 HQL 쿼리를 실행하기 위한 목적으로 만들어졌다.
    HQL 쿼리를 작성하다보면 String 연결을 이용하게 되고, 이는 결과적으로 읽기 어려운 코드를 만드는 문제를 야기한다. 
    String을 이용해서 도메인 타입과 프로퍼티를 참조하다보면 오타 등으로 잘못된 참조를 하게 될 수 있으며, 이는 String을 이용해서 HQL 작성할 때 발생하는 또 다른 문제다.
    
    타입에 안전하도록 도메인 모델을 변경하면 소프트웨어 개발에서 큰 이득을 얻게 된다. 
    도메인의 변경이 직접적으로 쿼리에 반영되고, 쿼리 작성 과정에서 코드 자동완성 기능을 사용함으로써 쿼리를 더 빠르고 안전하게 만들 수 있게 된다.

    Querydsl의 최초 쿼리 언어 대상은 Hibernate의 HQL이었으나, 현재는 JPA, JDO, JDBC, Lucene, Hibernate Search, MongoDB, 콜렉션 그리고 RDFBean을 지원한다.


### 장점

- IDE의 코드 자동 완성 기능 사용

- 문법적으로 잘못된 쿼리를 허용하지 않음

- 도메인 타입과 프로퍼티를 안전하게 참조할 수 있음

- 도메인 타입의 리팩토링을 더 잘 할 수 있음

참고 [https://querydsl.com/static/querydsl/4.4.0/reference/html_single/#intro]


### Querydsl은 왜 필요할까?

JPA를 사용한다고 가정해보자. 간단한 쿼리라면 인터페이스에 메서드 명세만 잘 정의해 주면 별다른 문제 없이 사용할 수 있을 것이다. 예를 들면 아래처럼 “제목에 특정 문자열이 포함된 게시판을 조회”하는 메서드처럼 말이다.

	List<Board> findByTitleContains(String title);


그럼 조금 더 복잡한 쿼리가 필요한 경우에는??? 특정 문자열이 제목에 포함된 게시판을 조회하는 것이 아닌, 게시판을 작성한 사용자의 권한 기준으로 게시판을 조회해 보자.


	@Query(value = "SELECT * FROM board WHERE user_id IN (SELECT id
    FROM User  WHERE role = :role)", nativeQuery = true)
	List<Article> findByLevel(@Param(value = "role") String role);
    
    
이 코드는 가독성은 감안하더라도 문자열을 이어 붙여가며 직접 작성하기 때문에 오타가 발생할 확률이 높다.

##### SQL, JPQL의 문제점

- SQL, JPQL은 문자열이다. 
- Type-check가 불가능하다. 
- 잘 해봐야 애플리케이션 로딩 시점에 알 수 있지만 컴파일 시점에 알 수 있는 방법이 없다. 자바와 문자열의 한계이다.
- 해당 로직 실행 전까지 작동여부 확인을 할 수 없다.
- 해당 쿼리 실행 시점에 오류를 발견한다.


이 코드를 Querydsl로 변경해보자


	public List<Board> findByUserRole(String role) {
    
    QBoard board = Qboard.board;
    QUser user = QUser.user;

    return queryFactory.selectFrom(board)
        .where(
            board.userId.in(
                JPAExpressions
                    .select(user.id)
                    .from(user)
                    .where(user.role.eq(role))
            )
        )
        .fetch();
}


위에 코드보다 코드의 양은 늘었지만 가독성이 훨씬 좋다. Querydsl 사용하기 이전에는 오류 발생 구문을 확인하기 어려운 반면 Querydsl을 사용할 경우 친절하게 컴파일 오류를 발생시켜 오류를 쉽게 수정할 수 있다.

---

## [실습코드](https://github.com/beomsun1234/Study/tree/master/Spring/hello-querydsl)














