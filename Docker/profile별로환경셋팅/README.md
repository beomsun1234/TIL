## 파일업로드 관련 프로젝트를 진행할 때 맥과 윈도우는 로컬저장소가 다르므로 환경을 나누어보자 

dockerfile

    FROM adoptopenjdk/openjdk11:alpine-jre
    ARG JAR_FILE=build/libs/*.jar
    ENV	USE_PROFILE default
    ADD ${JAR_FILE} app.jar
    ENTRYPOINT ["java", "-Dspring.profiles.active=${USE_PROFILE}", "-jar","app.jar"]
    
    
이미지 실행

    docker run -d -p 8080:8080 --rm -e USER_PROFILE=win 이미지이름 
    
    
application.yml

    spring:
      profiles: 
        active: win
        include: oauth2, db


    ---

    spring:
      profiles: mac


application-win.yml

    spring:
      servlet:
        multipart:
          max-file-size: 10MB
          max-request-size: 20MB

      jpa:
        hibernate:
          ddl-auto: create-drop

        show-sql: true

        properties:
          hibernate:
            format_sql: true

    resources:
      location: /C:/Users/park/images/
      

application-mac.yml


    spring:
      servlet:
        multipart:
          max-file-size: 10MB
          max-request-size: 20MB

      jpa:
        hibernate:
          ddl-auto: create-drop

        show-sql: true

        properties:
          hibernate:
            format_sql: true

    resources:
      location: /Users/park/images/
