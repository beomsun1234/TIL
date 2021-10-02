## Dockerfile이란?

도커파일이란 도커 이미지를 만들기 위해 작성하는 파일을 말한다.
docker build 명령어를 통해 Dodkcerfile에서 작성한 내용을 바탕으로 이미지를 생성할 수 있으며 도커 이미지를 구축해 도커 레지스트리에 올려놓으면 바뀌지 않는 환경들을 어디에서든 빠르게 사용이 가능합니다.


---

## 문법


|명령어|설명|
|------|---|
|FROM|베이스 이미지 지정|
|ARG|Dockerfile 에서의 변수|
|COPY|파일 복사|
|ADD|파일/디렉토리 추가|
|VOLUME|볼륨 마운트|
|RUN|명령 실행|
|EXPOSE|포트 익스포트|
|LABEL|라벨 설정|
|ENTRYPOINT|컨테이너 실행 명령, 빌드한 이미지를 컨테이너로 생성할때 단 한번 실행|
|CMD|컨테이너 실행 명령, 빌드한 이미지를 생성 및 시작할때 실행(Docker run, start) 단 하나의 CMD만 유효|
|WORKDIR|작업 디렉토리, RUN 명령어가 실행되는 위치를 지정하며, 컨테이너의 위치를 지정한다(bash의 cd와 유사합니다)|


ex)

    # Docker 환경 구성
    FROM java:8

    # 해당 이미지를 관리하는 사람
    LABEL maintainer="park"

    # 컨테이너가 필요한 데이터를 저장하는 곳
    VOLUME /tmp

    # 외부에 노출되는 포트 번호
    EXPOSE 8080

    # 현재 JAR 파일 변수 설정
    ARG JAR_FILE=build/lib/*.jar

    # app.jar의 이름으로 JAR 파일 추가
    ADD ${JAR_FILE} app.jar

    # 컨테이너 실행 시 실행될 명령어 "java -jar app.jar"
    ENTRYPOINT ["java", "-jar", "app.jar"]




spring boot


    FROM openjdk:11
    ARG JAR_FILE=build/libs/*.jar
    COPY ${JAR_FILE} app.jar
    ENTRYPOINT ["java","-jar","/app.jar"]
    EXPOSE 8080



### FROM 
- 베이스 이미지 지정
- 기반이 되는 이미지 레이어
- <이미지 이름>:<태그> 형식으로 작성 

springboot

    FROM 명령어는 스프링 부트 애플리케이션이 돌아갈 베이스 이미지를 의미합니다. 여기서는 openjdk11을 사용하고 있으니 아래와 같이 설정해주면 됩니다.


### ARG
- Dockerfile 내부 변수
- 환경변수로 gradle에서 빌드하였을때 떨어지는 jar의 위치를 잡아줍니다.

springboot jar 위치-> build/libs/

    ARG JAR_FILE=build/libs/*.jar


### COPY

- 파일 복사

springboot

     JAR_FILE=build/libs/*.jar

     COPY ${JAR_FILE} app.jar

잡아준 jar파일을 app.jar라는 이름으로 파일을 복사한다는 의미이며 컨테이너를 실행시 app.jar 파일이 존재하게 된다.


### ENTRYPOINT

- 컨테이너가 시작되었을 때 스크립트 혹은 명령을 실행
- 해당 이미지를 컨테이너로 생성할때 실행하고자하는 명령어를 작성


spring boot


    ENTRYPOINT ["java","-jar","/app.jar"]

     -> java -jar /app.jar


해당 컨테이너가 생성될때 jar 파일이 실행됩니다


---

 ## Docker Image 만들기

docker 이미지를 만들때 jar 파일이 필요하기 때문에 아래의 명령어로 jar파일을 생성해야 합니다.

    ./gradle clean build

     //주의
     jar파일이 생성된 위치와 Dockerfile에서 ARG로 정해준 위치가 동일해야 합니다!!

Docker Image를 만들어 보자

    docker build -t [도커 이미지 이름] [도커파일 위치]

    -t 옵션은 이미지이름과 태그를 지정하기 위해 사용

springboot

     docker build -t bs1002/hello-docker .

      dockerfile의 위치한 곳으로 이동해서 아래 명령어를 사용했하였기에 . (. 이 도커 파일 위치)

아래 명령어를 통해 잘 생성되었느지 확인해보자

    docker images



![도커이미지](https://user-images.githubusercontent.com/68090443/135713341-8ed34522-18e1-434d-8136-b193f1b507cc.PNG)


이미지가 잘 생성된 것을 확인 할 수 있다.

---

## Docker Image 실행

이제 docker run 명령어로 docker 이미지를 컨테이너로 올려서 애플리케이션이 작동되는지 확인해보자


### 기본 포맷

    docker run (<옵션>) <이미지 식별자> (<명령어>) (<인자>)

 이미지 식별자는 필수이며 이미지 ID나 리파지토리(repository):태그(tag)를 사용할 수 있다.


 ### 옵션

    -d

-d옵션은 백그라운드에서 실행하는 옵


    - p 

-p 옵션으 로컬과 컨테이너의 포트포워딩을 위한 옵션

    - v 

-v 옵션은 호스트와 컨테이너의 파일시스템을 공유하기위해 사용하는 옵션


    - it

-i 옵션과 -t 옵션은 같이 쓰이는 경우가 매우 많음

 이 두 옵션은 컨테이너를 종료하지 않은체로, 터미널의 입력을 계속해서 컨테이너로 전달하기 위해서 사용하는 옵셔

    —rm 옵션

--rm 옵션은 컨테이너를 일회성으로 실행할 때 주로 쓰이는데요. 컨테이너가 종료될 때 컨테이너와 관련된 리소스(파일 시스템, 볼륨)까지 깨끗이 제거해줍니다.



spring boot

    docker run -d -p 8080:8080 -it bs1002/hello-docker
