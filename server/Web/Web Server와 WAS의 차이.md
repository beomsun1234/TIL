# Web Server와 WAS의 차이

우선 정적 페이지와 동적 페이지를 알아보자!!


### Static Pages(정적 페이지)

      바뀌지 않는 페이지
    
웹 서버는 파일 경로 이름을 받고, 경로와 일치하는 file contents를 반환함

항상 동일한 페이지를 반환한다.

Ex) image, html, css, javascript 파일과 같이 컴퓨터에 저장되어 있는 파일들


### Dynamic Pages(동적 페이지)

   인자에 따라 바뀌는 페이지
  
인자의 내용에 맞게 동적인 contents를 반환함

웹 서버에 의해 실행되는 프로그램을 통해 만들어진 결과물임 (Servlet : was 위에서 돌아가는 자바 프로그램)

개발자는 Servlet에 doGet() 메소드를 구현함


## 웹 서버와 WAS의 차이

[사진]

### WEB Server

개념에 있어서 하드웨어와 소프트웨어로 구분된다.

하드웨어 - Web 서버가 설치되어 있는 컴퓨터

소프트웨어 - 웹 브라우저 클라이언트로부터 HTTP 요청을 받고, 정적인 컨텐츠(html, css 등)를 제공하는 컴퓨터 프로그램


#### WEB Server의 기능

      Http 프로토콜을 기반으로, 클라이언트의 요청을 서비스하는 기능을 담당

요청에 맞게 두가지 기능 중 선택해서 제공해야 한다.

1. 정적 컨텐츠 제공

      WAS를 거치지 않고 바로 자원 제공

2. 동적 컨텐츠 제공을 위한 요청 전달

      클라이언트 요청을 WAS에 보내고, WAS에서 처리한 결과를 클라이언트에게 전달

웹 서버 종류 : Apache, Nginx, IIS 등이 있다.

### WAS

     Web Application Server의 약자로
     DB 조회 및 다양한 로직 처리를 요구하는 동적인 컨텐츠를 제공하기 위해 만들어진 애플리케이션 서버이다.


HTTP를 통해 애플리케이션을 수행해주는 미들웨어다.

WAS는 웹 컨테이너 혹은 서블릿 컨테이너라고도 불림

(컨테이너란 JSP, Servlet을 실행시킬 수 있는 소프트웨어. 즉, WAS는 JSP, Servlet 구동 환경을 제공해줌)

종류는 Tomcat, JBoss 등이 있다.

#### 역활 

WAS = 웹 서버 + 웹 컨테이너

웹 서버의 기능들을 구조적으로 분리하여 처리하는 역할

보안, 스레드 처리, 분산 트랜잭션 등 분산 환경에서 사용됨 ( 주로 DB 서버와 함께 사용 )

#### WAS의 주요 기능

- 프로그램 실행 환경 및 DB 접속 기능 제공

- 여러 트랜잭션 관리 기능

- 업무 처리하는 비즈니스 로직 수행

## Web Server와 WAS를 구분하는 이유

### 웹 서버가 필요한 이유
  
      웹 서버에서는 정적 컨텐츠만 처리하도록 기능 분배를 해서 서버 부담을 줄이는 것
  
ex) 클라이언트에 이미지 파일을 보내는 과정을 생각해보자!
  
     이미지 파일과 같은 정적인 파일들은 웹 문서(HTML 문서)가 클라이언트로 보내질 때 함께 가는 것이 아니다.
     HTML 문서를 먼저 받고 그에 맞게 필요한 이미지 파일들을 다시 서버로 요청하면 그때서야 이미지 파일을 받아온다.
     Web Server를 통해 정적인 파일들을 Application Server까지 가지 않고 앞단에서 빠르게 보내줄 수 있다.
  
  
요약하자면
  
1. 웹 문서(html 문서)가 클라이언트로 보내질 때 이미지 파일과 같은 정적 파일은 함께 보내지지 않는다.
먼저 html 문서를 받음
  
2. 이에 필요한 이미지 파일들을 다시 서버로 요청해서 받아온다,


```웹 서버를 통해서 정적인 파일을 애플리케이션 서버까지 가지 않고 보낼 수 있다(서버의 부하가 줄어듬)```


### WAS가 필요한 이유

웹 페이지는 정적 컨텐츠와 동적 컨텐츠가 모두 존재한다.

사용자의 요청에 맞게 적절한 동적 컨텐츠를 만들어서 제공해야 한다.

이때, Web Server만을 이용한다면 사용자가 원하는 요청에 대한 결과값을 모두 미리 만들어 놓고 서비스를 해야하기에 자원이 절대적으로 부족하다.

```WAS를 통해 요청에 맞는 데이터를 DB에서 가져와 비즈니스 로직에 맞게 그때마다 결과를 만들어서 제공하면서 자원을 효율적으로 사용할 수 있다.```
  
### 그러면 WAS로 웹 서버 역할까지 다 처리할 수 있는거 아닌가요?

1. 기능을 분리하여 서버 부하 방지


        - WAS는 DB 조회, 다양한 로직을 처리하는 데 집중해야 함. 따라서 단순한 정적 컨텐츠는 웹 서버에게 맡기며 기능을 분리시켜 서버 부하를 방지하는 것

        - 만약 WAS가 정적 컨텐츠 요청까지 처리하면, 부하가 커지고 동적 컨텐츠 처리가 지연되면서 수행 속도가 느려짐 → 페이지 노출 시간 늘어나는 문제 발생


2. 물리적으로 분리하여 보안강화


       - SSL에 대한 암복호화 처리에 Web Server를 사용
  
  
3. 여러 대의 WAS를 연결 가능


     - load Balancing을 위해서 Web Server를 사용(NGINX)
     - fail over(장애 극복), fail back 처리에 유리
     - 특히 대용량 웹 어플리케이션의 경우(여러 개의 서버 사용) Web Server와 WAS를 분리하여 무중단 운영을 위한 장애 극복에 쉽게 대응할 수 있다.
     - 웹 서버를 앞 단에 두고, WAS에 오류가 발생하면 사용자가 이용하지 못하게 막아둔 뒤 재시작하여 해결할 수 있음 (사용자는 오류를 느끼지 못하고 이용 가능)


즉 자원 이용의 효율성 및 장애 극복, 배포 및 유지보수의 편의성을 위해 Web Server와 WAS를 분리한다.


#### 가장 효율적인 방법

[사진]

웹 서버를 WAS 앞에 두고, 필요한 WAS들을 웹 서버에 플러그인 형태로 설정하면 효율적인 분산 처리가 가능함

      Client -> Web Server -> WAS -> DB

동작 과정

- 1. Web Server는 웹 브라우저 클라이언트로부터 HTTP 요청을 받는다.
- 2. Web Server는 클라이언트의 요청(Request)을 WAS에 보낸다.
- 3. WAS는 관련된 Servlet을 메모리에 올린다.
- 4. WAS는 web.xml을 참조하여 해당 Servlet에 대한 Thread를 생성한다. (Thread Pool 이용)

- 5. HttpServletRequest와 HttpServletResponse 객체를 생성하여 Servlet에 전달한다.
  - 5-1. Thread는 Servlet의 service() 메서드를 호출한다.
  - 5-2. service() 메서드는 요청에 맞게 doGet() 또는 doPost() 메서드를 호출한다.
  - protected doGet(HttpServletRequest request, HttpServletResponse response)
 
- 6. doGet() 또는 doPost() 메서드는 인자에 맞게 생성된 적절한 동적 페이지를 Response 객체에 담아 WAS에 전달한다.
- 7. WAS는 Response 객체를 HttpResponse 형태로 바꾸어 Web Server에 전달한다.
- 8. 생성된 Thread를 종료하고, HttpServletRequest와 HttpServletResponse 객체를 제거한다.


### 래퍼런스

[참고자료1](https://gmlwjd9405.github.io/2018/10/27/webserver-vs-was.html)

[참고자료2](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Web/Web%20Server%EC%99%80%20WAS%EC%9D%98%20%EC%B0%A8%EC%9D%B4.md)
