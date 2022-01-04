# Deploying Kubernetes With Kafka

## zookeeper배포

우선 zookeeper.yaml 파일을 작성해보자

### Service

    apiVersion: v1
    kind: Service
    metadata:
      name: zookeeper
      labels:
        app: zookeeper
    spec:
      ports:
        - port: 2181
          protocol: TCP
      selector:
        app: zookeeper
        
## Deployment

    kind: Deployment
    apiVersion: apps/v1
    metadata:
      name: zookeeper
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: zookeeper
      template:
        metadata:
          labels:
            app: zookeeper
        spec:
          containers:
            - name: zookeeper
              image: digitalwonderland/zookeeper
              ports:
                - containerPort: 2181


### 완성 zookeeper.yaml


    kind: Deployment
    apiVersion: apps/v1
    metadata:
      name: zookeeper
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: zookeeper
      template:
        metadata:
          labels:
            app: zookeeper
        spec:
          containers:
            - name: zookeeper
              image: digitalwonderland/zookeeper
              ports:
                - containerPort: 2181
    ---

    apiVersion: v1
    kind: Service
    metadata:
      name: zookeeper
      labels:
        app: zookeeper
    spec:
      ports:
        - port: 2181
          protocol: TCP
      selector:
        app: zookeeper

이제 zookeeper를 배포해보자

    kubectl create -f zookeeper.yaml
    
이제 kafka를 배포해보자

## kafka 배포

### Service

    apiVersion: v1
    kind: Service
    metadata:
      name: kafka
      labels:
        name: kafka
    spec:
      ports:
        - port: 9092
          targetPort: 9092
          protocol: TCP
      selector:
        app: kafka
      type: LoadBalancer

### Deployment

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: kafka
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: kafka
      template:
        metadata:
          labels:
           app: kafka
        spec:
          containers:
            - name: kafka
              image: wurstmeister/kafka
              ports:
                - containerPort: 9092
              env:
                - name: KAFKA_PORT
                  value: "9092"
                - name: KAFKA_ADVERTISED_HOST_NAME
                  value:  127.0.0.1
                - name: KAFKA_ZOOKEEPER_CONNECT
                  value: zookeeper:2181
                - name: KAFKA_ADVERTISED_LISTENERS
                  value: PLAINTEXT://[hostname]:9092
                  

### 최종 (kafka.yaml)

    apiVersion: v1
    kind: Service
    metadata:
      name: kafka
      labels:
        name: kafka
    spec:
      ports:
        - port: 9092
          targetPort: 9092
          protocol: TCP
      selector:
        app: kafka
      type: LoadBalancer

    ---

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: kafka
    spec:
      replicas: 2
      selector:
        matchLabels:
         app: kafka
      template:
        metadata:
          labels:
            app: kafka
        spec:
          containers:
            - name: kafka
              image: wurstmeister/kafka
              ports:
                - containerPort: 9092
              env:
                - name: KAFKA_PORT
                  value: "9092"
                - name: KAFKA_ADVERTISED_HOST_NAME
                  value:  127.0.0.1
                - name: KAFKA_ZOOKEEPER_CONNECT
                  value: zookeeper:2181
                - name: KAFKA_ADVERTISED_LISTENERS
                  value: PLAINTEXT://[host-name]:9092 #내 로컬 아이피 OR 쿠버네티스 카프카 서비스명 입력하면 알아서 매칭시켜줌 ex) kafka:9092


yaml파일을 작성을 완료했다면 배포해보자

    kubectl create -f kafka.yaml
    
디폴리이먼트로 생성된 pod를 확인해보자

    kubectl get pod
    
zookeeper, kafka가 출력될것이다.

## Kafka 인스턴스 접근
    
    kubectl exec -it [카프카 파드명] bash
    
잘 접속 될 것이다. 이후 토픽을 생성하고 producer, consumer를 통해 메시지를 주고받으면 된다.

[카프카 명령어](https://github.com/beomsun1234/TIL/tree/main/Kafka/Docker%EC%B9%B4%ED%94%84%EC%B9%B4%ED%99%98%EA%B2%BD%EA%B5%AC%EC%B6%95)


## 트러블 슈팅

카프카 디폴리이먼트에서 카프카 환경 변수 중 KAFKA_ADBERTISED_PORT를 지정해줄 경우

     env:
      - name: KAFKA_PORT KAFKA_ADVERTISED_PORT
       value: "9092"
       
위 처럼 지정해줄 경우 configuration port: Not a number of type INT에러가 발생한다.. 이를 해결하기위해 

    env:
      - name: KAFKA_PORT
        value: "9092"
        
위 처럼 변경해주면 잘 작동한다.. 원인이 쿠버네티스는 kafka가 돌아가면서 환경변수를 만들기 때문에 yaml파일에 위 와같이 변경해 주어야한다..

출저 - https://stackoverflow.com/questions/37761476/kafka-on-kubernetes-cannot-produce-consume-topics-closedchannelexception-error


----

전부 설정이 끝나고 토픽을 생성해서 메시지를 주고 받으려고 했지만.. 메시지를 주고받을수 없었다.. KAFKA_ADVERTISED_LISTENERS를 설정하지 않아서 
외부에서 kafka 서버로 들어오는 ip를 지정해주지 않았다.. 이때문에 Consumer와 Producer가 Kafka와 연결되지 않아 발생한 오류였다.. 

카프카인스턴스에 접근해서 cd opt/kafka/config에 들어가서 vi server.properties에 들어갔지만 까만화면만 나오고 text가 나오지 않았다.. esc누른후 -q를 누르니 나가진긴했다..
해결 방법이 없을까? 하다가 환경변수로 지정해주면 될 것 같았다. 아래와 같이 kafka.yaml파일에서 환경변수 KAFKA_ADVERTISED_LISTENERS 값을 추가해 주었다

    env:
      .....
      - name: KAFKA_ADVERTISED_LISTENERS
        value: PLAINTEXT://[host-name]:9092 #내 로컬 아이피 OR 쿠버네티스 카프카 서비스명 입력하면 알아서 매칭시켜줌 ex) kafka:9092


문제 해결 완료~~

