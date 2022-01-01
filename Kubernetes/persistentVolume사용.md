## 스토리지로 퍼시스턴트볼륨(PersistentVolume)을 사용하도록 파드 설정하기

PV설정에서 정말 많이 트러블슈팅이 발생한 것 같다. 기존에 쿠버네티스 doc에서 제공하는 예제로 진행 할 경우 아래는 볼륨설정 파일이다.

    apiVersion: v1
    kind: PersistentVolume
    metadata:
    name: task-pv-volume
    labels:
        type: local
    spec:
    storageClassName: manual
    capacity:
        storage: 10Gi
    accessModes:
        - ReadWriteOnce
    hostPath:
        path: "/mnt/data"

위의 설절 파일은 클러스터 노드의 /mnt/data 에 볼륨이 있다고 지정한다. 또한 설정에서 볼륨 크기를 10 기가바이트로 지정하고 단일 노드가 읽기-쓰기 모드로 볼륨을 마운트할 수 있는 ReadWriteOnce 접근 모드를 지정한다. 여기서는 퍼시스턴트볼륨클레임의 스토리지클래스 이름을 manual 로 정의하며, 퍼시스턴트볼륨클레임의 요청을 이 퍼시스턴트볼륨에 바인딩하는데 사용한다. 

퍼시스턴트 볼륨을 생성해 보았다.

    kubectl apply -f https://k8s.io/examples/pods/storage/pv-volume.yaml

볼륨을 생성하였다면 퍼시스턴트볼륨클레임 생성해야한다. 파드는 퍼시스턴트볼륨클레임을 사용하여 물리적인 스토리지를 요청한다

아래는 퍼시스턴트볼륨클레임에 대한 설정 파일이다.

    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
    name: task-pv-claim
    spec:
    storageClassName: manual
    accessModes:
        - ReadWriteOnce
    resources:
        requests:
        storage: 3Gi

퍼시스턴트볼륨클레임을 생성한다.

    kubectl apply -f https://k8s.io/examples/pods/storage/pv-claim.yaml

볼륨으로 퍼시스턴트볼륨클레임을 사용하는 mariadb 파드를 만들어 주었다. (mariadb.yaml)

    apiVersion: v1
    kind: Service
    metadata:
      name: mariadb
    spec:
      ports:
        - port: 3306
          targetPort: 3306
          nodePort: 30001
      selector:
        app: mariadb
      type: NodePort
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
    name: mariadb
    spec:
    selector:
        matchLabels:
        app: mariadb
    strategy:
        type: Recreate
    template:
        metadata:
        labels:
            app: mariadb
        spec:
        containers:
            - image: mariadb:10.7 # MariaDB 이미지
            name: mariadb
            env:
                - name: MYSQL_ROOT_PASSWORD
                value: "1234"
            ports:
                - containerPort: 3306 # Container 포트

            volumeMounts:
                - name: mariadb-persistent-storage
                mountPath: /var/lib/mysql
        volumes:
            - name: mariadb-persistent-storage
            persistentVolumeClaim:
                claimName: manual

파드의 설정 파일은 퍼시스턴트볼륨클레임을 지정하지만, 퍼시스턴트볼륨을 지정하지는 않는다는 것을 유념하자. 파드의 관점에서 볼때, 클레임은 볼륨이다.

파드를 생성한다.

    kubectl apply -f mariadb.yaml


이렇게 할 경우 hostPath 볼륨을 찾지 못해서 에러가 났다....  [https://small-thing.tistory.com/203] 이분의 블로그가 날 구해주셨다...

## 동적 볼륨 프로비저닝

관리자가 스토리지 기능 및 분류 정보를 담고 있는 스토리지 클래스(StorageClass) 리소스만 정의해 놓고 개발자가 PVC를 요청하면 스토리지 클래스 리소스에 의해 PV가 자동으로 프로비저닝되어 사용할 수 있도록 동적 프로비저닝 기능을 제공한다.

## 스토리지 클래스

쿠버네티스의 스토리지 클래스 리소스는 스토리지의 클래스(분류, 정책, 종류)에 대한 정보를 정의할 수 있는 리소스다. 쿠버네티스는 자체적으로 클래스에 무엇을 정의해야 하는지에 대한 강제성은 없다. 필요한 스토리지의 여러 정보를 정의할 수 있다. 

출처: https://small-thing.tistory.com/203 [It's really something]


    kubectl get storageclasses.storage.k8s.io  명령어를 통해 스토리지 클래스 리소스 확인해보았더니 

[사진] 이있었다..

pv를 설정하지 않고 pvc만 설정해주고

hello-volume-claim.yaml

    apiVersion: v1

    kind: PersistentVolumeClaim

    metadata:
    name: mariadb-pv-claim

    spec:
    storageClassName: hostpath

    accessModes:
        - ReadWriteOnce
    resources:
        requests:
        storage: 20Gi

퍼시스턴트볼륨클레임을 생성

    kubectl apply -f hello-volume-claim.yaml    

마리아db파드를 삭제하고 

    kubectl delete -f mariadb.yaml

mariadb.yaml을 수정해주자

        ...
        volumes:
            - name: mariadb-persistent-storage
            persistentVolumeClaim:
                claimName: hostpath # 여기를 수정해주자


마리아db파드를 실행시키자

    kubectl apply -f mariadb.yaml

정상적으로 작동 된다~~