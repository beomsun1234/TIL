## 로컬(Window)에서 gcp인스턴스 ssh 접속 

puttygen를 통해 rsa key 생성한다.

우선 puttygen를 실행 시켜 Generate버튼을 클릭하여 키를 생성해준다. 완성된 키를 복사 후 Save privaete key버튼을 클릭하여 로컬 pc에 저장해준다.

이 후 GCP - Compute Engine - 메타데이터 - SSH키 탭에 접속하여 복사한 key를 등록해준다.

PuTTY를 실행하여 Connection - SSH - Auth에 저장한 private key를 넣어주고 Session에 Host Name에 [USERNAME]@[GCP 공개 IP]를 입력하고 Open 버튼을 클릭하면 접속 할 수 있다
