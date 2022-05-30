## 쿠버네티스로 mariadb 배포(단일 인스턴스 스테이트풀 애플리케이션 실행하기)

service와 delployment yaml을 작성해보자

## Service

    apiVersion: v1
    kind: Service
    metadata:
      name: mariadb
    spec:
      ports:
        #기본적으로 그리고 편의상 'targetPort'는
        #'port' 필드와 동일한 값으로 설정된다.
        #즉 nodePort로 설정한 30000포트로 요청이 들어오면
        #3306포트로 연결시켜준다는 것이다.
        - port: 3306
          #내부에 있는 컨테이너를 연결해주기 위하여 3306포트를 사용하는 것이다.
          targetPort: 3306

          #고정 포트(NodePort)로 각 노드의 IP에 서비스를 노출시킨다.
          #NodePort 서비스가 라우팅되는 ClusterIP 서비스가 자동으로 생성된다.
          #<NodeIP>:<NodePort>를 요청하여, 클러스터 외부에서 NodePort 서비스에 접속할 수 있다.
          #즉 워커노드의 특정 포트를 열고(nodePort) 여기로 오는
          #모든 요청을 노드포트 서비스로 전달하고 노드포트 서비스는
          #해당 업무를 처리할 수 잇는 파드로 요청을 전달한다.
          #노드에 오픈할 Port를 지정하는 것이다(미지정시 30000-32768 중에 자동 할당된다.)
          #외부에 노드포트로 expose하기 위해 30000번 포트를 지정한다.
          #이것은 expose 명령으로도 대체가 가능하나 이 30000번은 쓸 수 없다.
          nodePort: 30000
      selector:
        app: mariadb
      type: NodePort

## Delployment

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
                  name: mariadb
          


## 최종 hello-mariadb.yaml
    
    # Service

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

    ## Deployment
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


작성이 완료되면 YAML 파일의 오브젝트들을 배포한다.
    
    kubectl create -f hello-mariadb.yaml

maraidb가 배포가 완료됐다! 이제 외부에서 접속해보자!

## Mariadb 인스턴스 접근

    1. kubectl run -it --rm --image=mariadb:10.7 --restart=Never mariadb-client -- bash

    2. mysql -h mariadb -u root -p
    
    *참고 h 뒤에는 mariadb-deployment.yaml에 설정한 metadata:name: mariadb인 mariadb를 붙이면 알아서 hostIp를 대입해준다.
    
    3. mysql에 접속 후(외부접속을 위해)
      CREATE USER 'test'@'127.0.0.1' IDENTIFIED BY 'test#'; 
      
    heidisql에 접속하면 된다.



volume을 설정하지 않았기에 파드를 종료하면 데이터가 전부 날아간다.. 다음에는 파드가 날아가도 데이터가 날아가지 않도록 volume을 설정해보자!


### 참고 사이트
[쿠버네티스DOC](https://kubernetes.io/ko/docs/tasks/run-application/run-single-instance-stateful-application/)

