## 쿠버네티스로 eureka server, spring cloud gatway, client(server1(order), server2(product)) 배포 중 발생한 트러블 슈팅

서비스1과 서비스2는 mariadb및 kafka를 사용하고 있다.

eureka server, spring cloud gatway, server1(order), server2(product)의 배포를 완료했고 gatway를 통해 서비스1에 접속 할때 에러가 발생했다..

failed to resolve 'demo-order-service-5fd86c79d9-b9lr4' after 2 queries ~~

prefer-ip-address를 설정해 주라는 https://github.com/spring-cloud/spring-cloud-gateway/issues/2091(나와 같은 문제가 발생했다.) 글을 보았다.

prefer-ip-address는 서비스의 호스트 이름이 아닌 IP 주소를 Eureka Server 에 등록하도록 지정 (디폴트 false) 아래와 같이 설정해 주었더니 잘 동작한다.


    eureka:
      instance:
        prefer-ip-address: true 
  

기본적으로 유레카는 호스트 이름으로 접속하는 서비스를 등록하는데 DNS 가 지원된 호스트 이름을 할당하는 서버 기반 환경에서는 잘 동작하지만, 
컨테이너 기반의 배포에서 컨테이너는 DNS 엔트리가 없는 임의의 생성된 호스트 이름을 부여받아 시작하므로 컨테이너 기반 배포에서는 해당 설정값을 false 로 하는 경우 호스트 이름 위치를 정상적으로 얻지 못함


## 설정

유레카 서버는 설정을 수정한게 없으므로생략한다. 

### gateway 설정

    server:
      port: 8000
  
    eureka:
      client:
        register-with-eureka: true
        fetch-registry: true
        service-url:
          defaultZone: http://[hostip]/eureka
      instance:
        hostname: localhost
        prefer-ip-address: true

    spring:
      application:
        name: msa-gateway

      cloud:
        gateway:
          routes:
            - id: msa-order-service
              uri: lb://MSA-ORDER-SERVICE
              predicates:
                - Path=/order/**

            - id: msa-product-service
              uri: lb://MSA-PRODUCT-SERVICE
              predicates:
                - Path=/product/**


### order-service 설정

    spring:
      application:
        name: msa-order-service
      jpa:
        hibernate:
          ddl-auto: update
        show-sql: true
      datasource:
        driver-class-name: org.mariadb.jdbc.Driver
        username: root
        password: 1234
        url: jdbc:mariadb://[hostIp]:[mariaDbNodeport]/msaorder
        
    eureka:
      instance:
        hostname: localhost
        prefer-ip-address: true
      client:
        fetch-registry: true
        register-with-eureka: true
        service-url:
          defaultZone: http://[hostIp]/eureka
          
    server:
      port: 8080

### product-service 설정

    spring:
      application:
        name: msa-product-service

      jpa:
        hibernate:
          ddl-auto: update
        show-sql: true
      datasource:
        driver-class-name: org.mariadb.jdbc.Driver
        username: root
        password: 1234
        url: jdbc:mariadb://[hostIp]:[mariaDbnodePort]/msaproduct
        
    eureka:
      instance:
        prefer-ip-address: true
        hostname: localhost
     client:
        fetch-registry: true
        register-with-eureka: true
        service-url:
          defaultZone: http://[hostIp]/eureka
          
    server:
      port: 8081
  
### 쿠버네티스 배포를 위한 yaml 

### product-service.yaml 

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: demo-product-service
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: demo-product-service
      strategy:
        type: RollingUpdate
        rollingUpdate:
          maxSurge: 1
          maxUnavailable: 1
      template:
        metadata:
          labels:
            app: demo-product-service
        spec:
          containers:
            - name: demo-product-service
              image: beomsun22/demo-product-service
              ports:
                - containerPort: 8081
              imagePullPolicy: Always

    ---

    apiVersion: v1
    kind: Service
    metadata:
      name: demo-product-service
    spec:
      ports:
        - port: 8081
          targetPort: 8081
      selector:
        app: demo-product-service
      type: LoadBalancer


### gateway

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: demo-gatway
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: demo-gatway
      strategy:
        type: RollingUpdate
        rollingUpdate:
          maxSurge: 1
          maxUnavailable: 1
      template:
        metadata:
          labels:
            app: demo-gatway
        spec:
          containers:
            - name: demo-gatway
              image: beomsun22/demo-gatway
              ports:
                - containerPort: 8000
              imagePullPolicy: Always

    ---

    apiVersion: v1
    kind: Service
    metadata:
      name: demo-gatway
    spec:
      ports:
        - port: 8000
          targetPort: 8000
      selector:
        app: demo-gatway
      type: LoadBalancer

### order-service.yaml

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: demo-order-service
    spec:
      replicas: 1
      selector:
       matchLabels:
          app: demo-order-service
      strategy:
        type: RollingUpdate
        rollingUpdate:
          maxSurge: 1
          maxUnavailable: 1
      template:
        metadata:
          labels:
            app: demo-order-service
        spec:
          containers:
            - name: demo-order-service
              image: beomsun22/demo-order-service
              ports:
                - containerPort: 8080
              imagePullPolicy: Always

    ---

    apiVersion: v1
    kind: Service
    metadata:
      name: demo-order-service
    spec:
      ports:
        - port: 8080
          targetPort: 8080
      selector:
        app: demo-order-service
      type: LoadBalancer

각 클라이언트에 prefer-ip-address: true 설정 한 이후 문제 없이 잘 동작한다!! 


## 결과

파드 확인

![k8smsa프로젝트1](https://user-images.githubusercontent.com/68090443/148034505-60430f7b-7aed-49c0-abda-1e55e7684f79.PNG)


주문 요청 POST / localhost:8000/order/product/{id}/order


![주문요청](https://user-images.githubusercontent.com/68090443/148034605-30e2083e-096f-44f0-9977-3ff2ca25db05.PNG)

주문이 요청될 경우 두 서비스에서 발생하는 일

order-service 

![주문시](https://user-images.githubusercontent.com/68090443/148034744-c3452baf-75ac-4aff-adea-7911a91382c5.PNG)


product-service


![재고감소](https://user-images.githubusercontent.com/68090443/148034847-37b2389b-08d6-4ac8-90b5-c045f1ed24c3.PNG)

