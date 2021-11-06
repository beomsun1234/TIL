# AWS

## 좌충우돌 윈도우에서 EC2 인스턴스 접속기


### 터미널 툴을 사용해서 인스턴스에 접속해야한다. 많이 사용하고 있는 PuTTY를 사용해 보자!

### puttygen으로 .pem 파일을 .ppk 파일로 변환

설치 - (https://putty.softonic.kr/)[Putty설치]

PuTTY를 설치하면 puttygen 파일도 같이 설치가 되었 있을 거다.

puttygen 실행하여 .pem 파일을 .ppk 파일로 변환해 보자!


![ppk로바꾸기](https://user-images.githubusercontent.com/68090443/138425757-03c3a623-5ceb-4067-bc75-542be78a484f.PNG)


상단의 Conversions탭을 클릭 -> import key를 클릭 -> .pem 저장한 폴더에서 .pem파일을 클릭해준다. 


![ppk로변환2](https://user-images.githubusercontent.com/68090443/138425794-1a2a52ea-dd34-418e-bdb6-031a596ea46c.png)


Save private Key를 클릭하여 저장하면 .ppk 파일이 생성된다.

### 이제 Putty로 EC2 인스턴스에 접속해보자.

Putty를 실행하면 아래와 같은 화면이 나올것이다.


![ec접속](https://user-images.githubusercontent.com/68090443/138426396-2f0f544c-a6a8-42f5-b675-47482a94b2bd.png)


Host Name(or IP address) 부분에 접속하려는 ec2 인스턴스에 퍼블릭 ip를 집어 넣자


![ec2접속2](https://user-images.githubusercontent.com/68090443/138426619-3c906fc2-b221-4064-adc3-b3484261f2fd.png)

실행된 PuTTY 사진에 왼쪽 트리의 Connection-> SSH -> Auth로 이동하고 

Private Key File for authentication부분에 Browse를 클릭하여 puttygen으로 생성한 .ppk파일을 등록해주자


![세션저장오픈](https://user-images.githubusercontent.com/68090443/138426972-d8e0b6d8-a92c-4f83-818e-f0bbd8035a80.png)


접속 할때 마다 위의 과정을 반복하는 것이 귀찮기에 세션에 저장하고 접속 할 때, 저장한 세션을 클릭 후,
Loard 버튼을 클릭하여 설정 정보를 불러온 후 Open을 눌러주면 접속 된다. 

![저장](https://user-images.githubusercontent.com/68090443/138427280-a26cd841-d345-43ee-aaf7-609fd6763f4d.png)

이후 로그인 하라고 나오는데 ec2-user를 입력하고 엔터를 누르면 로그인이 되어 인스턴스에 접속된다.


