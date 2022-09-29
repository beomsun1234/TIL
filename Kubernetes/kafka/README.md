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
      storageClassName: "kafka"
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
      storageClassName: "zookeeper"
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
      storageClassName: "kafka"
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
      storageClassName: "zookeeper"
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 2Gi




helm install kafka -f values.yaml  bitnami/kafka --set volumePermissions.enabled=true --set volumePermissions.enabled=true
