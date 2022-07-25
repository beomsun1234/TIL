# Spring PSA

PSA란 Portable Service Abstraction의 약자로 이식 가능한 서비스 추상화라고 한다. ```잘만든 인터페이스라고도 한다.```

서비스 추상화란?? 특정 서비스가 추상화되어있다는 것은 서비스의 내용을 모르더라도 해당 서비스를 이용할 수 있다는 것을 의미한다


아래 3가지 예를 들어보자!!

## Spring Web MVC

서블릿을 사용하려면 HttpServlet을 상속받고 doGet(), doPost()를 구현하는 등의 작업을 직접 해야한다.

Spring Web MVC를 사용해서 @Controller, @GET, @POST 등의 어노테이션을통해 서블릿을 구현하는 작업 없이 원하는 기능을 편리하게 처리해준다.

즉 서블릿을 low level로 개발하지 않아도 된다.

또한 Spring Web MVC는 코드를 거의 그대로 둔 상태에서 톰캣이 아닌 다른 서버로 실행하는 것도 가능합니다.

프로젝트의 spring-boot-starter-web 의존성 대신 spring-boot-starter-webflux 의존성을 받도록 바꿔주기만 하면 Tomcat이 아닌 netty 기반으로 실행하게 할 수 있습니다

이처럼 기존 코드를 거의 변경하지 않고, 웹 기술 스택을 간편하게 바꿀 수 있도록 해줍니다.

## Spring Transaction

Low level로 트랜잭션 처리를 하려면 setAutoCommit()과 commit(), rollback()을 명시적으로 호출해야 한다.

ex)


    try {
      conn.setAutoCommit(false);

      //TODO Member findbyId

      conn.commit();

      System.out.println("완료!");

    } catch(SQLException e) {
      System.out.println(e.getMessage());
      conn.rollback();
    }
    finally {
      ...
          conn.close();
    }


그러나 Spring이 제공하는 @Transactional 애노테이션을 사용하면 단순히 메소드에 애노테이션을 붙여줌으로써 위 코드 처럼 Low level로 트랙잭션을 처리하는 코드를 작성하지 않아도 랜잭션 처리가 간단하게 이루어진다.


    @Transactional(readOnly = true)
    public Member findById(Long id){
        //TODO 로직

    }


또한 다양한 기술 스택으로 구현체를 바꿀 수 있다.

JDBC를 사용하는 DatasourceTransactionManager, JPA를 사용하는 JpaTransactionManager, Hibernate를 사용하는 HibernateTransactionManager를 유연하게 바꿔서 사용할 수 있다.

즉 기존 코드는 변경하지 않은 채로 트랜잭션을 실제로 처리하는 구현체를 사용 기술에 따라 바꿔 끼울 수 있는 것이다.


## Spring Cache

Cache도 마찬가지로  JCacheManager, ConcurrentMapCacheManager, EhCacheCacheManager와 같은
여러가지 구현체를 사용할 수 있습니다.



    @Cacheable(key = "#id")
    public Member findById(Long id){
        ....
    }


@Cacheable, @CacheEvict와 같은 Annotation을 이용하여 구현체는 신경 쓰지 않고 필요에 따라 바꿔서 사용 할 수 있다.




