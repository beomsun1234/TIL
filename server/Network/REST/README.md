# REST

## REST란?

- REpresentational State Transfer의 약자로 월드 와이드 웹과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 아키텍처의 한 형식이다. 
- 자원을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미한다. 
- 웹에 존재하는 모든 자원(이미지, 동영상, DB 자원)에 고유한 URI를 부여해 활용”하는 것으로, 자원을 정의하고 자원에 대한 주소를 지정하는 방법론


REST의 구체적인 개념

- HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미한다.
- 웹 사이트의 이미지, 텍스트, DB 내용 등의 모든 자원에 고유한 ID인 HTTP URI를 부여한다.


- CRUD Operation

    Create : 생성(POST)
    Read : 조회(GET)
    Update : 수정(PUT)
    Delete : 삭제(DELETE)
    HEAD: header 정보 조회(HEAD)


### REST 특징

- REST 아키텍처 형식을 따르면 HTTP나 WWW가 아닌 아주 커다란 소프트웨어 시스템을 설계하는 것도 가능하다.
