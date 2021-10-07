# 도커를 사용해서 spring boot에 mongodb와 mariadb를 붙여보자!


## 도커 허브에서 Mongodb 이미지와 Mariadb 이미지를 받아오자

Mongodb

    docker pull mongo
    
Mariadb

    docker pull mariadb
    

## 실행

도커 허브에서 받아온 mongodb 이미지 와 mariadb 이미지를 컨테이너에 올려보자

### mongodb

    docker run --rm -d -p 27017:27017 -e MONGO_INITDB_DATABASE=test --name mongodb mongo

test라는 데이터베이스를 만들었다. 잘 생성됐는지 확인해 보자
    
    // bash 쉘 실행
    docker exec -it mongodb bash
    
    //mongo db 접속
    mongo
    
    //데이터베이스 확인
    db
    
만들었던 test가 나오면 성공이다.


### mariadb

    docker run --rm -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=testrdb --name mariadb mariadb
    
mariadb에서는 testrdb라는 데이터베이스를 만들었다. 잘 생성됐는지 확인해 보자

    // bash 쉘 실행
    docker exec -it mariadb bash
    
    //mongo db 접속
    mysql -u root -p 
    
    //비밀번호입력
    1234
    
    //데이터베이스 확인
    show databases;
    
testrdb라는 데이터베이스가 있으면 성공이다.
    
---

## db 환경 설정이 끝났으니 Spring boot을 설정해보자

### 의존성 설정

    dependencies {
	    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
	    implementation 'org.springframework.boot:spring-boot-starter-data-mongodb' //mongodb
	    implementation 'org.springframework.boot:spring-boot-starter-web'
	    compileOnly 'org.projectlombok:lombok'
	    developmentOnly 'org.springframework.boot:spring-boot-devtools'
	    runtimeOnly 'org.mariadb.jdbc:mariadb-java-client' //mariadb
	    annotationProcessor 'org.projectlombok:lombok'
	    testImplementation 'org.springframework.boot:spring-boot-starter-test'
    }

### 연결할 db를 설정해주자( application-db.yml-> 실제 배포시 깃허브에 올라가면 안되므로 .gitignore 설정)

application-db.yml

    spring:
      datasource:
        url: jdbc:mariadb://localhost:3306/mydb
        username: root
        password: 1234
        driver-class-name: org.mariadb.jdbc.Driver

      data:
        mongodb:
          uri: mongodb://localhost:27017/test    



applcation.yml


    spring:
      profiles:
        include: db

      jpa:
        show-sql: true
        hibernate:
          ddl-auto: create-drop


spring boot을 실행시켜보면 잘 동작할 것이다. 이제 spring boot 애플리케이션을 도커이미지로 만들고 컨테이너에 올려서 실행해보자

[링크를 클릭하면 spring boot 애플리케이션 도커이미지로 만드는 방법을 알수있다.](https://github.com/beomsun1234/TIL/tree/main/Docker/spring%EB%8F%84%EC%BB%A4%EC%82%AC%EC%9A%A9)

### 실행

spring boot 애플리케이션 이미지를 컨테이너에 올려보자

    docker run -p 8080:8080 --rm {설정한 이미지 이름 or 이미지id}
    
    
실행하면 db연결 오류가 발생 할 것이다. 

application-db.yml에서 db연결 url을 localhost라 설정했다. 
하지만 app(spring boot)과 db가 서로다른 컨테이너에 올라가 있기에 db를 찾지 못해 오류가 발생한다.


#### 해결방법은??

우선 application-db.yml 수정 하자

    spring:
      datasource:
        url: jdbc:mariadb://{원하는이름}:3306/mydb
        username: root
        password: 1234
        driver-class-name: org.mariadb.jdbc.Driver

      data:
        mongodb:
          uri: mongodb://{원하는이름}:27017/test    


    ex) 마리아 db는 rdb이라는 이름으로 링크 설정, 몽고디비는 nosql이라는 이름으로 설정
    
    spring:
      datasource:
        url: jdbc:mariadb://rdb:3306/mydb
        username: root
        password: 1234
        driver-class-name: org.mariadb.jdbc.Driver

      data:
        mongodb:
          uri: mongodb://nosql:27017/test    
    

이미지를 컨테이너에 올릴시 link옵션 사용
    
    link 옵션은 같은 호스트 내에 컨테이너 간 연결을 할 때 사용한다.
    컨테이너끼리는 private ip를 기반으로 통신한다. 
    그런데 컨테이너가 재시작되면 ip가 바뀔 수도 있다. 
    이 문제를 해결하는 방법으로 link를 사용한다. 
    ip가 아닌 컨테이너 이름을 기반으로 통신할 수 있기 때문이다.
    

명령어

    docker run -p 8080:8080 --rm --link yml에설정한url:실행중인컨테이너이름 이미지이름
    
    ex) 
  
    docker run -p 8080:8080 --rm --link rdb:mariadb --link nosql:mongodb beomsun22/hello-test
   
실행시켜보면 잘 동작할 것이다

----

현재 db와 애플리케이션을 실행하기 위해 아래와 같이 docker run 이라는 명령어를 3번이나 작성해야하는 번거로움이 있다....

    docker run 마리아db이미지
    
    docker run 몽고db이미지
    
    docker run springbootApp
    
중복되는 작업을 줄이기 위해 Docker compose를 통해 여러개의 컨테이너를 한번에 정의할 수 있다.

[더 알아보기](https://github.com/beomsun1234/TIL/tree/main/Docker/Docker-Compose)


docker-compose.yml

    version: "3.7"
    services:
      app:
        container_name: app
        image: beomsun22/hello-test
        restart: always
        ports:
          - 8080:8080
        depends_on:
          - mariadb
          - mongodb

      mariadb:
        container_name: mariadb
        image: mariadb
        ports:
          - 3306:3306
        environment:
          - MYSQL_ROOT_PASSWORD=1234
          - MYSQL_USER=root
          - MYSQL_DATABASE=mydb
          
      mongodb:
        container_name: mongodb
        image: mongo
        ports:
          - 27017:27017
        environment:
          - MONGO_INITDB_DATABASE=test



docker-compose를 백그라운드로 실행해보자

docker-compose.yml이 작성된 폴더로 들어가 아래 명령어를 실행해보자

    docker compose up -d
    
아래 명령어를 실행하여 잘 동작하는지 확인해보자

    docker ps 

3개의 컨테이너가 동작하고 있으면 성공이다.


    curl http://localhost:8080/hello


위 명령어를 실행할 경우 hello docker가 보여지면 성공이다.

---

실행중인 컨테이너를 종료하면 데이터가 모두 삭제 된다. 데이터를 저장하기 위해서 docker-compose에 volume을 설정해보자

[더 알아보려면 클릭](https://github.com/beomsun1234/TIL/tree/main/Docker/Volume)

현재 내가 작성한 docker-compose를 요약하면 아래와 같다

     version: "3.7"
      services:
        app
      
        mariadb
      
        mongodb
      

이제 컨테이너 종료시에도 데이터가 보존되도록 volume을 설정해보자


    version: "3.7"
      services:
        app
      
        mariadb
      
        mongodb
      
    volumes:
      볼륨이름:
      볼륨이름:
    
mariadb 데이터와 mongodb 데이터를 저장하기위해 2개의 volume을 설정해 주었다.

``수정한 docker-compose.yml``

    version: "3.7"
      services:
        app:
          container_name: app
          image: beomsun22/hello-test
          restart: always
          ports:
            - 8080:8080
          depends_on:
            - mariadb
            - mongodb

       mariadb:
          container_name: mariadb
          image: mariadb
          ports:
            - 3306:3306
          volumes:
            - rdb:/var/lib/mysql
          environment:
            - MYSQL_ROOT_PASSWORD=1234
            - MYSQL_USER=root
            - MYSQL_DATABASE=mydb
            
        mongodb:
          container_name: mongodb
          image: mongo
          ports:
            - 27017:27017
          volumes:
            - nosql:/data/db
          environment:
            - MONGO_INITDB_DATABASE=test

    volumes:
      rdb:
      nosql:
