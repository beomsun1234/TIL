# Kubernets ingress 실습

구성

![쿠버네티스 아키텍쳐](https://user-images.githubusercontent.com/68090443/192749410-9f7f99b8-01c9-4978-aac1-d3c8d82bf66d.PNG)



## 트래픽 부하분산


![ingress 부하분산](https://user-images.githubusercontent.com/68090443/194597758-3dd8fe18-f2f5-416f-a460-aaf46a6fa14a.PNG)




## SSL 인증서 발급 받기

주의!! - 80포트를 사용하고 있지 않아야 합니다.


    sudo certbot certonly --standalone


인증서 확인


    certbot certificates
  
인증서 위치


    /etc/letsencrypt/live/[도메인 네임]/
  
  
인증서 갱신


    certbot renew


## ingres ssl 적용

Kubernetes에 SSL 인증서를 적용하기 위해서는 인증서를 포함하는 Secret tls를 생성해야 합니다.

다음과 같은 형태로 생성할 수 있습니다.


    kubectl create secret tls [secret_name] --cert [crtfile_name] --key [keyfile_name]
