# REST

## REST란?

- REpresentational State Transfer의 약자로 월드 와이드 웹과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 아키텍처의 한 형식이다. 

- 자원을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미한다. 

- 웹에 존재하는 모든 자원(이미지, 동영상, DB 자원)에 고유한 URI를 부여해 활용”하는 것으로, 자원을 정의하고 자원에 대한 주소를 지정하는 방법론


```REST 의 구체적인 개념```

- HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미한다.

- 웹 사이트의 이미지, 텍스트, DB 내용 등의 모든 자원에 고유한 ID인 HTTP URI를 부여한다.


- CRUD Operation

    Create : 생성(POST)
    Read : 조회(GET)
    Update : 수정(PUT)
    Delete : 삭제(DELETE)
    HEAD: header 정보 조회(HEAD)


### REST 특징

#### Server-Client

- Server : 자원 존재, API를 제공하고 비즈니스 로직 처리 및 저장을 책임진다.

- Client: 자원 요청, 사용자 인증이나 context(세션, 로그인 정보) 등을 직접 관리하고 책임진다.

- 클라이언트와 서버의 의존성 감소

#### Stateless

HTTP 프로토콜은 Stateless Protocol이므로 REST 역시 무상태성을 갖는다.


- Client의 context를 Server에 저장하지 않음 → 구현 단순
- Server는 모든 요청을 각자 별개의 것으로 인식하고 처리


#### Cacheable

- HTTP의 캐싱 기능 활용 가능 → 응답 시간, 성능 빨라짐


#### Uniform Interface

특정 언어에 종속되지 않고 HTTP 프로토콜을 따르면 모든 플랫폼에 적용 가능하다.


### REST 장점

- REST 아키텍처 형식을 따르면 HTTP나 WWW가 아닌 아주 커다란 소프트웨어 시스템을 설계하는 것도 가능하다.

- HTTP 프로토콜의 인프라를 그대로 사용하므로 REST API 사용을 위한 별도의 인프라를 구출할 필요가 없다.


- HTTP 프로토콜의 표준을 최대한 활용하여 여러 추가적인 장점을 함께 가져갈 수 있게 해준다.

- HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능하다.

- REST API 메시지가 의도하는 바를 명확하게 나타내므로 의도하는 바를 쉽게 파악할 수 있다.

- 서버와 클라이언트의 역활을 명확하게 분리한다. (Server : 자원 존재 / Client : 자원 요청!)


### REST 단점

- 표준이 존재하지 않는다.

- HTTP Method 형태가 제한적이다.(GET, HEAD, POST, PUT, PATCH, CONNECT, TRACE, OPTIONS)

- 구형 브라우저가 아직 제대로 지원해주지 못하는 부분이 존재한다

### REST가 필요한 이유
- 애플리케이션 분리 및 통합
- 
- 최근의 서버 프로그램은 다양한 브라우저와 안드로이폰, 아이폰과 같은 모바일 디바이스에서도 통신을 할 수 있어야 한다.(다양한 클라이언트의 등장)

### REST 구성요소

#### 자원(Resource) - URI

- 모든 자원에 고유한 ID가 존재하고, 이 자원은 Server에 존재한다.

- 자원을 구별하는 ID는 'user/:user_id' 와 같은 HTTP URI다.

- Client는 URI를 이용해서 자원을 지정하고 해당 자원의 상태(정보)에 대한 조작을 Server에 요청한다.

#### 행위 - HTTP Method

- HTTP 프로토콜의 Method를 사용한다. 대표적으로 GET, POST, PUT, DELETE 를 사용한다. 

#### 표현(Representaion of Resource)

- Client가 자원의 상태(정보)에 대한 조작을 요청하면 Server는 이에 적절한 응답(Representation)을 보낸다.

- REST에서 하나의 자원은 JSON, XML, TEXT, RSS 등 여러 형태의 Representation으로 나타내어 질 수 있다.

- JSON 혹은 XML를 통해 데이터를 주고 받는 것이 일반적이다.


## REST API

API(Application Programming Interface)란

    데이터와 기능의 집합을 제공하여 컴퓨터 프로그램간 상호작용을 촉진하며, 서로 정보를 교환가능 하도록 하는 것


REST API란??

    웹 상에서 REST는 HTTP URI로 자원들을 구분하고 HTTP Method로 표현한 상태를 클라이언트와 서버가 서로 전송을 주고 받아 CRUD 작업을 진행하는 것이다. 이런 인터페이스를 사용자가 활용할 수 있도록 구축해둔 것이 REST API라고 할 수 있다. 즉 REST 기반으로 서비스 API를 구현한 것 이다.
    
    


### REST API 특징

- 확장성과 재사용성을 높여 유지보수 및 운용을 편리하게 할 수 있다.

- HTTP 표준을 기반으로 구현하므로, HTTP를 지원하는 프로그램 언어로 클라이언트, 서버를 구현할 수 있다.

### RESTful 이란?


