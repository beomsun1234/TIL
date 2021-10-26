# SPRING DI와 IoC

## DI 란?

DI란  Dependency Injection 약자로 의존성 주입이라 한다. 

### 의존성이란?

A라는 클래스 내부에 has a 관계로 B클래스를 포함을 시키면 A클래스는 B에 의존적이다 라고 말을 하는데 

이 말을 쉽게 풀어 쓰면 A라는 클래스가 작동하기 위해서는 B가 필요하다는 의미가 된다.

클래스 A에서 의존성 객체를 생성하는 방법 2가지가 있다.

1. A객체가 B객체를 New 생성자를 통해 직접 생성하는 방법


        public class A{

            private B b;
        
            public A(){
        
                b = new B();

            }

        }

2. 외부에서 생성 된 객체를 setter()나 생성자를 통해 사용하는 방법

        public class A{

            private B b;
    
            public void setB(B b){
                this.b = b;
    
            }

        }


여기서 두번째 방법은 A객체를 직접 생성하지 않고 외부에서 생성된 객체를 setter()로 받고 있다. 이런걸 주입이라고 하며
스프링에는 두번째 방법을 통해 의존성 객체를 주입시켜준다.

스프링에서는 객체의 생성과 소멸에 관련된 작업을 자동적으로 수행해주는데 객체가 생성되는 곳을 스프링에서는 ```Bean 컨테이너라고``` 부른다 

스프링에서는 ```객체를 Bean이라고 부르며```, 스프링에서는  프로젝트가 실행될때 사용자가 Bean으로 관리하는 객체들을 자동으로 생성해준다.

A라는 클래스 에서 B라는 클래스 C클래스를 요청했을때 스프링에서는 실행될때 생성했던 Bean을 주입시켜주는데 이 과정을 DI라고 한다.

### 스프링 DI

* 필드 주입

        @RestController
        public class BookController {
    
            @Autowired
            private BookService bookService;    
        }
        
        
        - 가장 일반적이고 쉬운 DI 방법
        - final로 지정할 수 없기에 mutable 하여 NullPointerException이 발생할 수 있다.
        - Runtime에서 예기치 않은 순환참조 문제가 발생할 수 있다.


* 수정자 주입

 
        @RestController
        public class BookController {

            private BookService bookService;
        
            public void setBookService(BookService bookService) {
                this.bookService = bookService;
            }
        }

        - 성당시 주입을 꼭 하지 않아도 된다. 즉, 원하는 호출 타이밍에 함수를 호출하여 주입시킬 수 있다.
        - 마찬가지로 mutable하여 NullPointerException이 발생할 수 있다.


* 생성자 주입

        @RestController
        public class BookController {
        
            private final BookService bookService;
    
            public BookController(BookService bookService) {
                this.bookService = bookService;
            }
        }
        
        - 가장 권장하는 DI 방식
        - final 지정이 가능하기에 Immutable(불변) 하다.
        - 테스트 코드 작성이 유리하다.
----

## Bean

스프링 IoC 컨테이너가 관리하는 객체

### 등록 방법

- Component Scanning

    - @가 붙어있는 모든 class들을 찾아서 Bean으로 등록해주는 것
 
        	종류
        	- @Component 
        	- @Repository
        	- @Service
        	- @Controller
        	- @Configuration
        	- etc ...


- 직접 XML이나 자바 설정파일에 등록 

	- 자주 없음

-----

## IoC Container

모든 작업을 사용하는 쪽에서 제어하게 되면서 IoC컨테이너에서 제어하게 되는데, 기본적으로 컨테이너는 객체를 생성하고 객체간의 의존성을 이어주는 역할을 한다.

----

## IoC란?

IoC(Inversion of Control)란 "제어의 역전" 이라는 의미로 제어의 흐름을 바꾼다라고 한다. 즉 메소드나 객체의 호출작업을 개발자가 결정하는 것이 아니라 외부에서 결정되는 것을 의미한다.


기존에는 다음과 순서로 객체가 만들어지고 실행되어졌다.

- 1.객체 생성

- 2.의존성 객체 생성(클래스내부에서)

- 3.의존성 객체 메소드 호출 

직접 의존성을 만듬
        
        @RestController
        public class BookController {
    	   private BookService bookService = new BookService();
        }


하지만 스프링에서는 다음과 같은 순서로 객체가 만들어지고 실행된다

- 1.객체 생성

- 2.의존성 객체 주입(스스로가 만드는것이 아니라 제어권을 스프링에게 위임하여 스프링이 만들어놓은 객체를 주입)

- 3.의존성 객체 메소드 호출

IoC

        @RestController
        public class BookController {
        
            private final BookService bookService;
    
            public BookController(BookService bookService) {
                this.bookService = bookService;
            }
        }

스프링이 모든 의존성 객체를 스프링이 실행될때 다 만들어주고 필요한곳에 주입시켜줌으로써 Bean들은 싱글턴 패턴의 특징을 가지며,

제어의 흐름을 사용자가 컨트롤 하는 것이 아니라 스프링에게 맡겨 작업을 처리하게 된다.

객체의 의존성을 역전시켜 객체 간의 결합도를 줄이고 유연한 코드를 작성할 수 있게 하여 가독성 및 코드 중복, 유지 보수를 편하게 할 수 있게 한다.
