# kafka

## POD
![카프카2](https://user-images.githubusercontent.com/68090443/194305914-1e36e2e7-9945-4829-ae56-85191b599768.PNG)

## Service

![카프카3](https://user-images.githubusercontent.com/68090443/194305924-6c6594d3-2e6a-49f7-b58c-e62829eb5a8a.PNG)


## 카프카 web

 
![카프카 전송](https://user-images.githubusercontent.com/68090443/194304729-e78b3590-1358-4dcc-bf6e-570bb7e13515.PNG)


        https://beomsun.kro.kr/kafka-service/api/v1/kafka 로 GET 요청시 kafka producer(토픽=pbs)로 message 메시지 전송


#### 카프카 web - application.yaml 설정

    kafka:
      host: kafka-0.kafka-headless.default.svc.cluster.local:9092
      
      # host: [kafka 서비스명].kafka-headless.[네임스페이스명].svc.cluster.local:9092





### kafka dns

[kafka 서비스명].kafka-headless.[네임스페이스명].svc.cluster.local:9092

ex)
    
        kafka-console-consumer.sh --bootstrap-server kafka-0.kafka-headless.default.svc.cluster.local:9092 --topic pbs

----

# 카프카(Kafka) 설치

쿠버네티스에 helem으로 카프카를 설치해보자!

[bitnami kafka github](https://github.com/bitnami/charts/tree/master/bitnami/kafka)


helm이 설치되어있다고 가정하고 진행하겠습니다.


## Step 1
helm repo 추가

    helm repo add bitnami https://charts.bitnami.com/bitnami
  

## Step 2

pv, pvc volume 셋팅

kafka_zookeeper_volume.yaml


    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: kafka-pv
      labels:
        app: kafka-pv
    spec:
      storageClassName: ""
      accessModes:
        - ReadWriteOnce
      hostPath:
        path: "/mnt/data"
      capacity:
        storage: 1Gi


    ---
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: zoo-pv
      labels:
        app: zoo-pv
    spec:
      storageClassName: ""
      accessModes:
        - ReadWriteOnce
      hostPath:
        path: "/mnt/zoo"
      capacity:
        storage: 2Gi

    ---

    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: kafka-pvc
    spec:
      storageClassName: ""
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 1Gi

    ---

    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: zookeeper-pvc
    spec:
      storageClassName: ""
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 2Gi



## Step 3

step2에서 생성한 volume 적용 및 외부 접속 NodePort설정

설정정보는 https://github.com/bitnami/charts/tree/master/bitnami/kafka 해당 페이지에 있습니다. 

values.yaml


        persistence:
          enabled: true
          existingClaim: "kafka-pvc"


        zookeeper:
          persistence:
            existingClaim: "zookeeper-pvc"

        securityContext:
          enabled: true
          fsGroup: 1001    #makesfilesystem as root user
          runAsUser: 1001

        externalAccess:
          enabled: true
          service:
            type: NodePort
            nodePorts:
              - 30092
            useHostIPs: true
            domain: "34.64.108.102"


## Step 4

helm install


    helm install kafka -f values.yaml  bitnami/kafka --set volumePermissions.enabled=true --set volumePermissions.enabled=true
    

## bootstrap-server 


[kafka 파드명].kafka-headless.default.svc.cluster.local:9092


    kafka-0.kafka-headless.default.svc.cluster.local:9092

----

## 트러블슈팅

pv,pvc를 직접 설정해주지 않으면 bitnami/kafka 설치시 기본으로 생성된 pvc가 pending 상태를 계속 유지하면 kafka와 zookeeper pod도 pending로 머물러 있는다. pv와 pvc를 직접 생성해주고 values.yaml에 kafka와 zookeepr가 내가 만든 볼륨을 사용할 수 있도록 설정해주면서 문제를 해결할 수 있었습니다.


### mkdir: cannot create directory '/bitnami/zookeeper/data': Permission denied

kafka, zookeeper pod의 pending 상태를 해결하니 error가 발생했다.. 로그를 확인해보니 위 와 같이 에러가 발생했다..

pv의 hostPath 권한 문제였다.. kafka와 zookeeper 가 돌아가고있는 노드에 chmod 777을 선언하니 해결됐다. 


다른 방법을 좀 더 찾아보니 helm install시 

    --set volumePermissions.enabled=true 
    
위 부분을 추가해주므로 해결할 수 있었다.


    helm install kafka -f values.yaml  bitnami/kafka --set volumePermissions.enabled=true 

###  Warning  FailedScheduling  58s (x8 over 9m54s)  default-scheduler  0/3 nodes are available: 3 pod has unbound immediate PersistentVolumeClaims.

helm으로 kafka install시 pvc관련 오류로 zookeeper pod가 pending 상태로 지속됨.. kubectl describe 명령어로 확인한 결과 위와 같이 에러가 발생했다. 원인은 PVC와 PV의 연결을 PVC에 selector를 통해서 연결을 했는데  StorageClass로 찾고 있었고 StorageClass또한 존재하지 않아서 발생했다. 아래 내용으로 수정하니 문제를 해결할 수 있었다.

    storageClassName: ""

zookeeper.yaml

    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: zoo-pv
      labels:
        app: zoo-pv
    spec:
      storageClassName: ""
      accessModes:
        - ReadWriteOnce
      hostPath:
        path: "/mnt/zoo"
      capacity:
        storage: 2Gi


    ---

    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: zookeeper-pvc
    spec:
      storageClassName: ""
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 2Gi
