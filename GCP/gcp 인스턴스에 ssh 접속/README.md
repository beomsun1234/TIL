## GCP인스턴스에 SSH로 접속하기

ci/cd 구성 중에 jenkins 서버에서 서비스가 돌아가고 있는 서버의 서비스들을 배포할 때 서비스가 구동되고 있는 서버에 접속하기 위해 ssh를 사용했다.

우선 서비스 구동 서버에 ssh 접속을 위한 rsa key를 jenkins서버에 생성해주자.

    ssh-keygen -t rsa -f ~/.ssh/[KEY_FILE_NAME] -C [USERNAME]
    
key 생성이 끝났으면 *.pub key 내용을 복사해서 GCP 에 입력해야 한다. 아래의 명령어를 통해 key 내용 확인하고 gcp에 복사하자

    cat ~/.ssh/[KEY_FILE_NAME].pub
    
복사한 키를 Compute Engine -> 메타데이터 -> SSH키 탭에 키를 입력하고 저장 버튼을 누르면 된다.

이 후 jenkins서버에서 

    root@[gcp-public-ip]
    
를 입력하여 접속하면 된다. 


## 트러블 슈팅

    gcp에 ssh키를 등록할 때 자꾸 유효하지 않은 key라고 나왔다... 한 5번 넘게 만들어보고 문제를 찾을 수 있었다.. 복사를 똑바로 하지 않아서 발생한 문제였다...
    어이없었지만 앞으로 복사할 때 꼼꼼하게 복사해야겠다...
