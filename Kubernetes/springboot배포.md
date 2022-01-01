## k8s를 이용하요 springboot 배포

springboot파일을 빌드하는 dockerfile을 만들자! 

    FROM openjdk:11
    ARG JAR_FILE=build/libs/*.jar
    COPY ${JAR_FILE} app.jar
    ENTRYPOINT ["java","-jar","/app.jar"]
    EXPOSE 8080
    
    
빌드 후 

이미지를 생성해준다.

    docker build -t [나의도커허브아이디]/[프로젝트이름] .(현재 도커파일 위치)
    
생성된 이미지를 도커허브에 push하자

    docker push [나의도커허브아이디]/[프로젝트이름]
    

이제 쿠버네티스를 통해 배포해보자

Deployment와 Service 설정을 정의한 demo-app-deployment.yaml, demo-app-service.yaml을 작성하자


## Service(demo-app-service.yaml)


    apiVersion: v1
    kind: Service
    metadata:
      name: demo-app-service
    spec:
      ports:
        - port: 8080
          targetPort: 8080
      selector:
        app: demo-app-service
      type: LoadBalancer
  
----

## Deployment(demo-app-deployment.yaml)

    #apiVersion: API 버전을 명시한다
    #이 오브젝트를 생성하기 위해 사용하고 있는 쿠버네티스 API 버전이 어떤 것인지
    #명시한다.
    apiVersion: apps/v1

    #어떤 종류의 오브젝트를 생성하고자 하는지 명시한다.
    kind: Deployment


    #이름 문자열, UID, 그리고 선택적인 네임스페이스를 포함하여
    #오브젝트를 유일하게 구분지어 줄 데이터이다.
    metadata:
      name: demo-app-service 
  
    #오브젝트에 대해 어떤 상태를 의도하는지 명시한다.
    spec:
      replicas: 3
  
  
      #(.spec.selector)디플로이먼트가 관리할 파드를 찾는 방법을 정의한다.
      #이 사례에서는 파드 템플릿(아래 명시된 template)에 정의된 레이블(app: demo-app-service)을 선택한다.
      selector:
        matchLabels:
          app: demo-app-service
      
      
      #파드 교체 전략을 지정한다. Recreate의 경우 기존 파드를 모두
      #삭제한 다음 새로운 파드를 생성하는 방법이다. (이 방식은 무중단이 아니다)
      #기본값은 RollingUpdate이다. RollingUpdate은 Pod를 하나씩 죽이고
      #새로 띄우면서 순차적으로 교체하는 방법이다.
      strategy:
        type: RollingUpdate
        rollingUpdate:
          maxSurge: 1
          maxUnavailable: 1
      template:
        metadata:
          labels:
            app: demo-app-service
        
        
        #.template.spec 필드는 파드가 도커 허브의
        #beomsun22/k8s-app 이미지를 실행하는
        #app 컨테이너 1개를 실행하는 것을 나타낸다
        #컨테이너 1개를 생성하고 .spec.template.spec.containers[0].name 필드를 사용해서 hello-k8s-app-service 이라는 이름을 붙인다.
        #즉 컨테이너의 이름이 hello-k8s-app-service이 된다. describe deployment 명령어로 확인 가능
        #파드는 여러 개의 컨테이너를 가질 수 있는데 여기서는 하나만 선언한 것
        spec:
          containers:
            - name: hello-k8s-app-service
              image: beomsun22/k8s-app
              ports:
                - containerPort: 8080
              imagePullPolicy: Always

## 최종 yaml


# Service

apiVersion: v1
kind: Service
metadata:
  name: demo-app-service
spec:
  ports:
    - port: 8080
      targetPort: 8080
  selector:
    app: demo-app-service
  type: LoadBalancer

---

## Deployment

    apiVersion: apps/v1
    kind: Deployment
    metadata:
    name: demo-app-service
    spec:
    replicas: 3
    selector:
        matchLabels:
        app: demo-app-service
    strategy:
        type: RollingUpdate
        rollingUpdate:
        #kubectl set image deployment <디플로이먼트 이름> <컨테이너 이름>=<새 이미지>
        #kubectl set image deployment -f <디플로이먼트 파일> <컨테이너 이름>=<새 이미지>
        maxSurge: 1
        maxUnavailable: 1
    template:
        metadata:
        labels:
            app: demo-app-service
        spec:
        containers:
            - name: hello-k8s-app-service
            image: beomsun22/k8s-app
            ports:
                - containerPort: 8080
            imagePullPolicy: Always



## 디플로이먼트 롤링업데이트

    kubectl set image deployment <디플로이먼트 이름> <컨테이너 이름>=<새 이미지>
    kubectl set image deployment -f <디플로이먼트 파일> <컨테이너 이름>=<새 이미지>