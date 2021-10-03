# Docker Compose

## Docker Compose란?

    Docker compose는 yaml 파일로 여러 개의 도커컨테이너의 정의를 작성하여 한 번에 많은 컨테이너들을 작동시키고 관리할 수 있는 툴입니다.

Docker compose를 사용하면 많은 서비스들을 손쉽게 스핀 업하는데 편리합니다. 예를 들어 Apollo 서버, Rest API 서버, React 프론트엔드를 각각 도커화하여 사용하고 있다면 개발 환경을 시작할 때마다 docker run을 3번 실행해줘야 하는데 프로그래머로서 원치 않는 중복성이라 할 수 있습니다. 이러한 중복성을 줄이고자

docker-compose는 여러 개의 서비스를 한 번에 정의를 가능하게 합니다.

    services:
    application:
        image: hello-docker-compose

    database:
        image: mariadb

이렇게 하나의 문서에 여러 개의 컨테이너를 정의할 수 있습니다.


## Docker Compose의 특징

단일 호스트의 여러 격리된 환경
Compose는 프로젝트 이름을 사용하여 환경을 서로 격리하고 여러 다른 콘텍스트에서 이 프로젝트 이름을 사용하여 접근을 합니다.

예를 들어 application이라는 서비스를 실행시킬 때 my_application, your_application 형식으로 여러 개를 서로 격리하여 서비스가 가능합니다.

프로젝트 이름은 기본으로 실행한 폴더명이 기준이 되며 별도로 지정이 가능합니다.

    $ docker-compose -p my up 
    $ docker-compose -p your up

위와 같이 -p 옵션으로 프로젝트명을 주어 실행이 가능한데 하나의 애플리케이션을 두 개의 격리된 환경으로 제공해줍니다.

컨테이너 생성 시 볼륨 데이터 보존
컨테이너 생성 시 볼륨 데이터 보존하여 데이터가 휘발되지 않도록 처리해줍니다.
컨테이너 내부에서 생성하여 사용하는 파일 볼륨을 로컬 경로와 공유하여 실수로 컨테이너가 종료되더라도 재실 행시 같은 볼륨을 유지해주어 컨테이너를 내렸다가 다시 실행시키더라도 이전에 사용했던 환경 그대로 사용이 가능한 장점이 있습니다.

변경된 컨테이너만 재생성
컨테이너를 만드는 데 사용되는 구성을 캐시 하여 변경되지 않은 서비스를 다시 시작하면 Compose는 기존 컨테이너를 다시 사용합니다.

변수 및 환경 간 구성 이동
Compose 파일의 변수를 지원하여 다양한 환경 또는 다른 사용자에 맞게 컴포지션 커스텀이 가능합니다.


- 출저 [https://meetup.toast.com/posts/277] nhn 클라우드

---
## 서비스 정의

### application service 정의 

    docker run -d -p 8080:8080 -it bs1003/hello-docker-compose .

해당 명령어를 Compose로 작성하면

    application:
        ports:
            - 8080:8080
        container_name: spring-app
        build:
            context: .
            dockerfile: Dockerfile
        depends_on:
            - database
        restart: always

### MariaDB 서비스 정의

    docker run -d 
    -p 3306:3306
    -v C:\Users\박범선\datadir:/var/lib/mysql
    -e MYSQL_DATABASE=mydb
    -e MYSQL_USER=root
    -e MYSQL_ROOT_PASSWORD=1234 
    mariadb

해당 명령어를 Compose로 작성하면

    database:
    container_name: spring-db
    image: mariadb
    ports:
    - 3306:3306
    volumes:
      - C:\Users\박범선\datadir:/var/lib/mysql
    environment:
      - MYSQL_DATABASE=mydb
      - MYSQL_USER=root
      - MYSQL_ROOT_PASSWORD=1234
    restart: always

최종본

    version: "3.7"
    services:
        application:
            ports:
                - 8080:8080
            container_name: spring-app
            build:
                context: .
                dockerfile: Dockerfile
            depends_on:
                - database
            restart: always

        database:
            container_name: spring-db
            image: mariadb
            ports:
                - 3306:3306
            volumes:
                - C:\Users\박범선\datadir:/var/lib/mysql
            environment:
                - MYSQL_DATABASE=mydb
                - MYSQL_USER=root
                - MYSQL_ROOT_PASSWORD=1234
            command: ['--character-set-server=utf8mb4', '--collation-server=utf8mb4_unicode_ci']
            restart: always

        
- 파일 하나에 application, mysql 두 개의 설정을 한꺼번에 정의하여 실행환경을 빠르게 구성할 수 있다.

- 하나의 설정 파일로 관리가 되어 서비스를 올리고 내리는걸 빠르고 쉽게 할 수 있다.

- 여러 개의 서버에 같은 환경을 제공할 때 유용하게 사용이 가능하다.

---

## docker-compose 작성

    services:
        application:
            image: hello-docker-compose

        database:
            image: mariadb

- version : Docker-compose의 버전을 명시 / 버전에 따라 지원하는 형식이 다름

- serivces : docker-compose를 통해 관리할 컨테이너(이미지) 단위 / 하위에 이름으로 명시 ex) react, spring, app .. 등 등


mariadb가 실행될 컨테이너

    database:
            container_name: spring-db
            image: mariadb
            ports:
                - 3306:3306
            volumes:
                - C:\Users\박범선\datadir:/var/lib/mysql
            environment:
                - MYSQL_DATABASE=mydb
                - MYSQL_USER=root
                - MYSQL_ROOT_PASSWORD=1234
            command: ['--character-set-server=utf8mb4', '--collation-server=utf8mb4_unicode_ci']
            restart: always
            
|명령어|설명|
|------|---|
|container_name |컨테이너 이름 지정|
|image|사용할 이미지 ex) mariadb|
|environment|컨테이너 내부에서 사용할 인자, 위는 mariadb 환경변수 지정, MYSQL_DATABASE-> mydb란 이름의 db생성, MYSQL_USER -> user는 root, MYSQL_ROOT_PASSWORD -> root 패스워드 지정 |
|volumes|마운트할 볼륨 설정, local 디렉토리와 컨테이너 경로 매칭|
|ports|외부에서 접속하는 포트를 Docker 내부 포트와 매칭|
|restart|컨테이너 오류와 같이 종료되었을 때 다시 시작할지 여부|

    Spring Boot에서 DB를 접근하고자 할 때 포트 번호를 포함하여 spring-db:3306으로 적는다. docker-compose.yml로 생성하는 컨테이너는 자동으로 하나의 네트워크 그룹에 포함 됩니다. 컨테이너 이름과 포트 번호를 이용해 서로를 찾아낼 수 있죠.


 Spring Boot가 실행될 application 컨테이너

    application:
            ports:
                - 8080:8080
            container_name: spring-app
            build:
                context: .
                dockerfile: Dockerfile
            depends_on:
                - database
            restart: always


|명령어|설명|
|------|---|
|ports|host의 8080 포트를 컨테이너의 8080포트와 매핑|
|container_name|컨테이너 이름 지정|
|build|빌드 옵션, context -> 도커파일의 위치를 지정, dockerfile -> 도커 파일의 경로|
|depends_on|의존성을 추가한다. db를 사용할 경우 스프링 부트는 실행할 때 database connection을 요청한다. 따라서 mysql 컨테이너가 완전히 로드되지 않은 상태에서 접속을 시도하면 에러가 발생한다. 따라서 이 옵션을 두어 mariadb 컨테이너가 완전히 로드된 이후에 접속을 시도한다.|

---
## 실행

[사진]

내 프로젝트 구조(루트에서)

    docker-compose up -d  명령어를 실행하면


[사진]

spring boot 컨테이너와 mariadb 컨테이너가 잘 동작한다.


db를 조회해 보면

[사진]


데이터가 잘 보존되어있다.

---

## docker-compose 명령어


    docker-compose up [옵션] [서비스명]

컨테이너를 생성 및 실행

|옵션|설명|
|------|---|
|-d|백그라운드 실행|
|--no-deps|링크 서비스 실행하지 않음|
|--build|이미지 빌드|
|-t|타임아웃을 지정(기본 10초)|

    
    docker-compose ps

현재 동작중인 컨테이너들의 상태 확인

    docker-compose logs

컨테이너들의 로그를 출력

    docker-compose run

docker-compose up 명령어를 이용해 생성 및 실행된 컨테이너에서 임의의 명령을 실행하기 위해 사용

만약 특정 서비스에서 /bin/bash를 실행시켜 쉘 환경으로 진입하고 싶다면 아래와 같은 명령어를 이용하면 됩니다. 참고로 서비스명과 컨테이너명은 다르다.

    # docker-compose run [서비스명] [명령]
    docker-compose run database /bin/bash

서비스명은 docker-compose.yml의 services: 밑에 작성한 서비스 이름


    # 서비스 시작
    docker-compose start

    # 서비스 정지
    docker-compose stop

    # 서비스 일시 정지
    docker-compose pause

    # 서비스 일시 정지 해제
    docker-compose unpause

    # 서비스 재시작
    docker-compose restart

여러개의 서비스 또는 특정 서비스를 시작 / 정지 / 일시정지 / 재시작을 할 수 있습니다.


    docker-compose rm

docker-compose로 생성한 컨테이너들을 일괄 삭제 합니다. (삭제 전, 관련 컨테이너들을 종료 시켜두어야 합니다.)

---