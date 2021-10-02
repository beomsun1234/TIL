# MariadbDB 사용하기


## MariadbDB 이미지를 다운

    docker pull mariadb

해당 명령어를 통해 MariadbDB 이미지를 다운로드한다.


## 컨테이너 실행


    docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 --name mariadbtest mariadb


![도커마리아디비](https://user-images.githubusercontent.com/68090443/135722247-19874591-d07a-4b82-b73d-14e080f643ad.PNG)




|명령어|설명|
|------|---|
|-d|detached mode, 백그라운드에서 실행|
|-p|호스트와 컨테이너의 포트를 연결 (포워딩)
호스트에서 3306 포트 접속 시 컨테이너 3306 포트로 포워딩됨|
|--name|	컨테이너 이름 설정
testmariadb|
|-e|컨테이너 내에서 사용할 환경변수 설정
MYSQL_ROOT_PASSWORD=1234는 root 계정의 패스워드를 1234로 지정|
|--character-set-server=utf8mb4 |character-set-server, DB 서버의 기본 문자셋으로서 설정 파일에 명시한 대로 utf8mb4로 설정|
|--collation-server=
utf8mb4_unicode_ci|collation-server 문자열 정렬 규칙|

    
    
    docker -exec -it testmariadb /bin/bash

mariadb를 실행하고 해당 DB에 접속하기 위해서 위에 명령어를 실행하여 컨테이너의 bash로 접속한다.


## MariaDB 접속

    mysql -u root -p

해당 명령어를 이용하여 DB 접속한다.


![마리아db접속](https://user-images.githubusercontent.com/68090443/135722213-3259e53a-8582-4d88-9f72-d65cf4d18ef7.PNG)


password는 MYSQL_ROOT_PASSWORD로 설정한 1234를 입력하면 된다.


---

heidisql을 사용하여 db에 접속하고 테이블 생성 후 데이터를 집어 넣고 조회해 보면


![db조회](https://user-images.githubusercontent.com/68090443/135722336-fe6783bf-38b5-463d-b7dc-b1656a38b238.PNG)


위와 같이 데이터를 조회할 수 있다.



## Characterset 변경

한글로 데이터를 집어넣을 경우


![도카dbutf깨짐](https://user-images.githubusercontent.com/68090443/135722297-571c018a-8e51-41b0-a49a-74738172a185.PNG)


위와 같이 데이터가 ??? 으로 들어간것을 볼수 있다.

해당 문제를 해결하기 위해  /etc/mysql/my.cnf 파일 수정하면 간단하게 해결할 수 있다.

우선 mariadb를 실행하고 있느 컨테이너에 vim을 설치해야한다. 

    apt-get update

    apt-get install vim

해당 명령어로 vim을 설치해준다.


    vim /etc/mysql/my.cnf

etc/mysql/my.cnf 에 내용 추가해준다.

    [client]
    default-character-set = utf8mb4

    [mysql]
    default-character-set = utf8mb4

    [mysqld]
    character-set-client-handshake = FALSE
    character-set-server = utf8mb4
    collation-server = utf8mb4_unicode_ci

설정 후 도커를 재시작한 후 다시 조회하면

![도커db저장](https://user-images.githubusercontent.com/68090443/135722311-3ae3570d-90c9-4638-b954-843bbaaa2935.PNG)


