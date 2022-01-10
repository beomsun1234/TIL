## blue-green 배포


기존에는 롤링 업데이트(default)를 통해 변경 사항을 적용해주었다..pod 들을 정해진 개수만큼 새로운 pod를 띄우고, 기존의 pod를 종료시킨다. 새로운 pod가 띄어지면서 기존의 pod가 삭제되어 여러 버전의 pod가 띄어져있을 수 있는 전략이다. 하지만 이런 방식으로 인해 2가지 버전의 pod가 실행되어 사용자에게 혼란을 줄 수 있는 단점이 있다.

이러한 단점이 있기에 블루그린 배포인데blue-green 배포 전략을 사용할 수 있다. blue-green 배포를 할 경우 똑같은 수의 pod을 추가로 만들어서 service가 바라보는 쪽을 변경하는 방식의 배포형태이다. 하지만 리소스가 제한적일 때는 적용 힘들다.

이제 blue-green배포 전략을 사용해 보자!


    업데이트 전 GET - localhost:8080 -> hello

    업데이트 후 GET - localhost:8080 -> hello2


## step

도커 이미지를 만들고 도커허브에 push해보자 (빌드 했다고 가정한다)

    FROM adoptopenjdk/openjdk11:alpine-slim
    ARG JAR_FILE=build/libs/*.jar
    COPY ${JAR_FILE} app.jar
    ENTRYPOINT ["java", "-jar", "app.jar"]


위의 Dockerfile 작성 후

    docker build -t [도커허브id]/[이미지명]:[버전]
    
    완료 후 이미지 도커허브에 push
    docker push [도커허브id]/[이미지명]:[버전]
    
완료 됐으면 blue, green 배포 yaml을 만들어보자

### app-blue.yaml


    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: demo-blue-app
      labels:
        app: demo-app
        color: blue
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: demo-app
          color: blue
      template:
        metadata:
          labels:
            app: demo-app
            color: blue
        spec:
          containers:
            - name: demo-app
              image: beomsun22/demo-blue-green:v0.1
              ports:
                - containerPort: 8080



### app-green.yaml

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: demo-green-app
      labels:
        app: demo-app
        color: green
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: demo-app
          color: green
      template:
        metadata:
         labels:
            app: demo-app
            color: green
        spec:
          containers:
            - name: demo-app
              image: beomsun22/demo-blue-green:v0.2
              ports:
                - containerPort: 8080


배포 파드를 생성하자

    kubectl create -f app-blue.yaml
    kubectl create -f app-green.yaml
    

이후 서비스가 blue(app-blue)를 바라보도록 만들어보자

### blue-green-service.yaml

apiVersion: v1
kind: Service
metadata:
  name: demo-app
  labels:
    app: demo-app
spec:
  ports:
    - port: 8080
      targetPort: 8080
  selector:
    app: demo-app
    color: blue
  type: LoadBalancer


서비스를 배포하자

    kubectl create -f blue-green-service.yaml
    

아래 명령어를 통해 확인해 보자

    curl "http://localhost:8080"

    hello가 뜨면 성공이다.
    
이제 업데이트를 해보자
    
    kubectl patch service demo-app --patch '{\"spec\":{\"selector\":{\"color\":\"green\"}}}


해당 명령어를 통해 서비스가 green을 바라보도록 변경해주면

    curl "http://localhost:8080"
    
    hello2가 뜨면 성공이다.


## 트러블슈팅

    
    kubectl patch service demo-app --patch '{"spec":{"selector":{"color":"green"}}}'

해당 명령어를 통해 blue에서 green을 바라보도록 설정을 변경 할 때  아래와 같은 오류가 발생했었다.. 
    
    invalid character s looking for beginning of object key string
    
다행이도 스택오버플로우에서 찾을 수 있었다. 구문 오류였다.. 다행이 빠르게 찾아서 해결 됐다.. 

[https://stackoverflow.com/questions/55602559/kubectl-patch-works-on-linux-bash-but-not-in-windows-powershell-ise]