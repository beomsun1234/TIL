# Spring PSA

PSA란 Portable Service Abstraction의 약자로 이식 가능한 서비스 추상화라고 한다. ```잘만든 인터페이스라고도 한다.```

서비스 추상화란?? 특정 서비스가 추상화되어있다는 것은 서비스의 내용을 모르더라도 해당 서비스를 이용할 수 있다는 것을 의미한다


아래 3가지 예를 들어보자!!

## Spring Web MVC

서블릿을 사용하려면 HttpServlet을 상속받고 doGet(), doPost()를 구현하는 등의 작업을 직접 해야한다.

Spring Web MVC를 사용해서 @Controller, @GET, @POST 등의 어노테이션을통해 서블릿을 구현하는 작업 없이 원하는 기능을 편리하게 처리해준다.

즉 서블릿을 low level로 개발하지 않아도 된다.

## Spring Transaction

Low level로 트랜잭션 처리를 하려면 setAutoCommit()과 commit(), rollback()을 명시적으로 호출해야 한다.

ex)


    try {
      dbConnection.setAutoCommit(false);

      doSomething()...

      dbConnection.commit();

      System.out.println("Done!");

    } catch(SQLException e) {
      dbConnection.rollback();
    }
    finally {
      ...
          dbConnection.close();
    }


그러나 Spring이 제공하는 @Transactional 애노테이션을 사용하면 단순히 메소드에 애노테이션을 붙여줌으로써 트랜잭션 처리가 이루어진다. 



## Spring Cache
