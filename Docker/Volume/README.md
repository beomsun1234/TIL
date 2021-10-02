# 도커(Docker) Volume이란?

Docker 데이터 볼륨은 데이터를 컨테이너가 아닌 호스트에 저장하는 방식입니다. 따라서 데이터볼륨은 컨테이너끼리 데이터를 공유할 때 활용할 수 있습니다.

도커 이미지로 컨테이너를 생성하면 이미지는 읽기 전용이 되며 컨테이너의 변경 사항만 별도로 저장해서 각 컨테이너의 정보를 보존한다. 

이미 생성된 이미지는 어떠한 경우로도 변경되지 않으며, 컨테이너 계층에 원래 이미지에서 변경된 파일시스템을 저장

mysql 컨테이너를 삭제하면 컨테이너 계층에 저장돼 있던 데이터베이스의 정보도 삭제

도커의 컨테이너는 생성과 삭제가 매우 쉬우며, 실수로 컨테이너를 삭제하면 데이터를 복구할 수 없게 됨

이를 방지하기 위해 컨테이너의 데이터를 영속적(Persistent) 데이터로 활용할 수 있는 방법이 몇가지 있다.

 
그중 가장 활용하기 쉬운 방법이 볼륨(Volume)을 활용한다.

---

## 명령어

데이터 볼륨 옵션은 -v <컨테이너 디렉터리> 형식입니다. 

    docker run -d -p 3306:3306 -v C:\Users\"폴더이름"\datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=qkrqjatjs15 mariadb

:를 기준으로 왼쪽은 나의 로컬 PC에 존재하는 디렉토리, 오른쪽은 MySQL 컨테이너 데이터가 저장되는 디렉토리 입니다. 즉, 두 디렉토리를 서로 연결시키겠다는 뜻
(MySQL 컨테이너 디렉토리가 나의 로컬 디렉토리를 참조하겠다는 뜻)

컨테이너에 들어가보면

![마운트](https://user-images.githubusercontent.com/68090443/135726746-fabb9e28-82d6-4dfa-b64d-4c1e247229d9.PNG)

내 pc

![내pc](https://user-images.githubusercontent.com/68090443/135726775-1ec180ba-dfd2-4e37-a061-5cdc0ffe7063.PNG)

잘 마운트 되었다.


이제 db에 데이터를 저장해보자

![db볼륨저장](https://user-images.githubusercontent.com/68090443/135726668-822d2f61-4bcc-49eb-90f9-04bf822cc5fb.PNG)

    docker rm [컨테이너id]
    
데이터를 저장 했으니 해당 명령어로 컨테이너를 삭제하고 다시 시작해보자

    docker run -d -p 3306:3306 -v C:\Users\"폴더이름"\datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=qkrqjatjs15 mariadb
    
    
    docker exec -it [컨테이너id] /bin/bash
    
이제 데이터를 조회해 보면


![도커조회](https://user-images.githubusercontent.com/68090443/135726724-09b3d9af-5651-487a-a562-f21cc2041f65.PNG)

데이터가 컨테이너를 삭제하기 전과 동일하다.

기존에 Volume를 사용하지 않고 mariadb컨테이너를 생성하고 삭제하면 테이블과 데이터가 삭제 되어 있었지만 Volume을 사용하니 컨테이너의 정보를 보존했다.

