# istio ingress gateway 앞단에 gcp-load-balancer 설정

## 아키텍쳐 

![istio12](https://user-images.githubusercontent.com/68090443/203513051-66f295f4-b9f7-4434-975e-14d20dd277b4.PNG)


## 결과 

order-prodcut grpc 통신

![image](https://user-images.githubusercontent.com/68090443/203521535-6584afd4-f301-40a9-9814-ca761ad30258.png)

![image](https://user-images.githubusercontent.com/68090443/203522254-6637cf25-8709-4368-a929-0122cd0f32a9.png)


productpage

![image](https://user-images.githubusercontent.com/68090443/203521665-4175bc5c-7900-44a7-9252-13e6eebf82e5.png)


## gcp-load-balncer 설정하기

### step 1 인스턴스 그룹 만들기(gcp에 직접 kubernetes를 설치했으므로 클러스를 그룹으로 만들어준다.)


![인스턴스 그룹만들기](https://user-images.githubusercontent.com/68090443/203516346-592585a0-c28d-4db0-9c17-6883fcfc949f.PNG)

그룹 만들기 버튼 클릭 후 

![인스턴스그룹만들기2](https://user-images.githubusercontent.com/68090443/203516394-6e2d2035-7977-467f-a478-ee0e104d46ca.PNG)

위치는 클러스터가 사용하고있는 리전으로 설정해 주고 vm 인스턴스를 설정해준다. (1 master, 2 worker node)

![인스턴스그룹만들기3](https://user-images.githubusercontent.com/68090443/203516714-194ed4fa-03d0-462a-a573-a06fe8cf0ae9.PNG)

istio-gateway port를 설정해준다. (나는 istio gateway의 서비스 타입을 nodeport로 설정했다.)

만들기 버튼을 클릭하면 완성된다.


### step 2 gcp-load-balncer 설정

네트워크 서비스에 부하분산 부분에 들어가면 아래 사진을 확인 할 수 있다. 

![istio-lb설정1](https://user-images.githubusercontent.com/68090443/203517643-b1c2f00f-9e2d-432f-a400-0c28192a0b1f.PNG)

부하 분산기 만들기 버튼을 클릭한다.

![istio-lb2](https://user-images.githubusercontent.com/68090443/203517769-4985a2b8-dd8b-4a31-a4f8-d45e386d803c.PNG)

L7 LB를 선택하고 구성시작 버튼을 클릭한다.

![istio-lb3](https://user-images.githubusercontent.com/68090443/203518105-2b331075-2ab2-4de2-8a23-d22697353c8b.PNG)

사진과 같이 설정하고 프론트엔드를 구성한다.

![istio-lb4프론트](https://user-images.githubusercontent.com/68090443/203518223-69264a7d-ea88-497b-9dc9-c6bc92aad9a8.PNG)

http, https 두가지로 구성해 주었다.

이제 백엔드 구성를 구성해보자!

![istio-lb5-백](https://user-images.githubusercontent.com/68090443/203518545-414b2d92-8515-480f-9c2d-213d15f6f761.PNG)

백엔드 서비스 만들기 버튼을 클릭한 후 2번 동그라미 부분에 step 1에서 만들었던 인스턴스 그룹을 넣어준다. 나는 istio-gateway에 tls를 설정해주 었으므로 포트를 istio-gateway의 https 포트를 사용할 것 이다.


![istio-lb6-백](https://user-images.githubusercontent.com/68090443/203519226-e85d3cf5-18a7-458f-9d8b-09fec5ba8b78.PNG)


프로토콜을 https로 변경하고 이림이 지정된 포트에 인스턴스 그룹에서 만들었던 https 포트를 넣어준다. 
상태확인 서비스를 등록해주자 

이 후 상태 확인을 생성해 주자

![상태확인](https://user-images.githubusercontent.com/68090443/203520422-a290565c-26dd-4465-98a8-317007e942ce.PNG)

/hello 경로에 상태 체크 서비스를 띄웠다.

![상태확인서비스](https://user-images.githubusercontent.com/68090443/203520638-0936a925-2d5b-49b9-9ea0-e12f08268a62.PNG)

### 상태 확인을 위한 서비스 및 virtualservice manifeste

hello-svc.yaml


    apiVersion: apps/v1
    kind: Deployment
    metadata:
     name: web-deploy
    spec:
     replicas: 1
     selector:
       matchLabels:
         app: web
     template:
       metadata:
         labels:
           app: web
       spec:
         containers:
         - name: pod-guest
           image: gcr.io/google-samples/kubernetes-bootcamp:v1
           ports:
           - containerPort: 8080
    ---
    apiVersion: v1
    kind: Service
    metadata:
     name: svc-web
    spec:
     ports:
       - port: 8080
         targetPort: 8080
     selector:
       app: web

hello-vs.yaml

    apiVersion: networking.istio.io/v1alpha3
    kind: VirtualService
    metadata:
      name: hello-vs
    spec:
      hosts:
      - "*"
      gateways:
      - bookinfo-gateway
      http:
      - match:
        - uri:
            prefix: /hello
        route:
        - destination:
            port:
              number: 8080
            host: svc-web


## 최종 gcp LB

![image](https://user-images.githubusercontent.com/68090443/203522980-2e74ff75-8aed-4fc1-8925-51731011f9ff.png)


