# AWS EC2 도커 사용기

## 도커를 ec2에도 설치해 보자!

우선 yum 업데이트 해주자

	sudo yum update -y
	
도커를 설치해 보자

	sudo yum -y install docker
	or
	sudo amazon-linux-extras install -y docker

설치 후 아래 명령어를 통해 설치를 확인 하자

 	docker -v
	
도커를 시작해 보자

	sudo service docker start
	
이후 usermod 명령어를 사용하여 그룹에 사용자인 ec2-user를 추가합니다

	sudo usermod -aG docker ec2-user

Docker-compose를 설치해 보자

	sudo curl -L https://github.com/docker/compose/releases/download/1.25.0\
	-rc2/docker-compose-`uname -s`-`uname -m` -o \
	/usr/local/bin/docker-compose

설치 후에 chmod 명령어를 사용하여 디렉토리에 excute 권한을 추가하자

	sudo chmod +x /usr/local/bin/docker-compose

설치를 확인해 보자

	docker-compose -v
	
----

### 에러

프론트/백을 나누어 프로젝트를 진행하면서 백엔드를 AWS EC2에 도커를 이용해 서버를 구동 시켰다. 이 과정에서 30분 정도 헤맨 기억을 작성해 보았다..


docker-compose.yml 작성 후 기존에 도커를 사용할 때 사용했던 명령어인 

	docker compose up -d

를 통해 실행했지만  is not a docker command 라는 문구와 함께 동작하지 않앗다.... 30분 정도 헤맨 것 같다....

	docker-compose up -d

위 와같이 변경하니 동작한다... 


## 트러블슈팅
	
	docker ps

위 명령어를 작성하고 실행할 경우 


	Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json": dial unix /var/run/docker.sock: connect: permission denied 

권한 관려 에러가 발생한다

이럴 경우 

	chmod 666 /var/run/docker.sock

위 명령어로 권한을 설정해주자!
