## GCP(우분투)에 Jenkins 설치하기

step 1. 패키지 업데이트하기

    apt-get update -y && apt-get upgrade -y
    

step 2. Java 설치하기(jenkins를 실행하기 위해서는 자바가 필요하다)

    sudo apt install openjdk-8-jdk


step 3. 패키지에 Jenkins 추가하기

    wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
    
    패키지에 추가
    sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
    
    or
    
    sudo wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add - 
    echo deb http://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list'
    
step 4. Jenkins 설치

    sudo apt-get install jenkins
    

### key 파일이 제대로 설치되지 않았을 경우

    sudo vi /etc/apt/sources.list
    
    
    -----
    
    deb https://pkg.jenkins.io/debian-stable binary/
    
    입력 후 저장 및 종료 
    
    sudo apt-get update
    sudo apt-get install jenkins
    
step 5. Jenkins 실행

    sudo systemctl daemon-reload
    sudo systemctl start jenkins
    
    상태 확인
    sudo systemctl status jenkins
    
정상적으로 실행 되면 공인IP:8080으로 로그인하여 접속하고 

초기 패스워드를 해당명령어를 통해 얻은 후 접속하면 된다.

    sudo cat /var/lib/jenkins/secrets/initialAdminPassword

