# Ingress Monitoring

Prometheus and Grafana

[쿠버네티스 ingress 모니터링 가이드](https://kubernetes.github.io/ingress-nginx/user-guide/monitoring/)


## Prometheus
![ingress 프로메테우스](https://user-images.githubusercontent.com/68090443/194521618-7cef64e2-6d11-4924-bd8e-f1cd22d1c2d9.PNG)


## Grafana
![ingress 그라파나모니터링](https://user-images.githubusercontent.com/68090443/194521602-f8e7a712-7677-4b13-b268-9a5765caef8b.PNG)


## Grafana

[Grafana helm chart](https://github.com/grafana/helm-charts/blob/main/charts/grafana/values.yaml)

# Prometheus install 


우선 쿠버네티스 ingress 모니터링 가이드 링크에 나와있듯이 ingress를 manifest 파일을 설정을 변경해주어야한다.

ingress manifest파일의 일부분이다.

ingress.yaml

    apiVersion: v1
    kind: Service
    metadata:
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "10254"
      labels:
        app.kubernetes.io/component: controller
        app.kubernetes.io/instance: ingress-nginx
        app.kubernetes.io/name: ingress-nginx
        app.kubernetes.io/part-of: ingress-nginx
        app.kubernetes.io/version: 1.3.1
      name: ingress-nginx-controller
      namespace: ingress-nginx
    spec:
      ipFamilies:
      - IPv4
      ipFamilyPolicy: SingleStack
      ports:
      - name: prometheus
        port: 10254
        targetPort: prometheus
      - appProtocol: http
        name: http
        port: 80
        protocol: TCP
        targetPort: http
        nodePort: 30100
      - appProtocol: https
        name: https
        port: 443
        protocol: TCP
        targetPort: https
        nodePort: 30200
      selector:
        app.kubernetes.io/component: controller
        app.kubernetes.io/instance: ingress-nginx
        app.kubernetes.io/name: ingress-nginx
      type: NodePort

    ---

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app.kubernetes.io/component: controller
        app.kubernetes.io/instance: ingress-nginx
        app.kubernetes.io/name: ingress-nginx
        app.kubernetes.io/part-of: ingress-nginx
        app.kubernetes.io/version: 1.3.1
      name: ingress-nginx-controller
      namespace: ingress-nginx
    spec:
      minReadySeconds: 0
      revisionHistoryLimit: 10
      selector:
        matchLabels:
          app.kubernetes.io/component: controller
          app.kubernetes.io/instance: ingress-nginx
          app.kubernetes.io/name: ingress-nginx
      template:
        metadata:
          annotations:
            prometheus.io/port: "10254"
            prometheus.io/scrape: "true"
          labels:
            app.kubernetes.io/component: controller
            app.kubernetes.io/instance: ingress-nginx
            app.kubernetes.io/name: ingress-nginx
        spec:
          containers:
          - args:
            - /nginx-ingress-controller
            - --election-id=ingress-controller-leader
            - --controller-class=k8s.io/ingress-nginx
            - --ingress-class=nginx
            - --configmap=$(POD_NAMESPACE)/ingress-nginx-controller
            - --validating-webhook=:8443
            - --validating-webhook-certificate=/usr/local/certificates/cert
            - --validating-webhook-key=/usr/local/certificates/key
            env:
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
            - name: LD_PRELOAD
              value: /usr/local/lib/libmimalloc.so
            image: registry.k8s.io/ingress-nginx/controller:v1.3.1@sha256:54f7fe2c6c5a9db9a0ebf1131797109bb7a4d91f56b9b362bde2abd237dd1974
            imagePullPolicy: IfNotPresent
            lifecycle:
              preStop:
                exec:
                  command:
                  - /wait-shutdown
            livenessProbe:
              failureThreshold: 5
              httpGet:
                path: /healthz
                port: 10254
                scheme: HTTP
              initialDelaySeconds: 10
              periodSeconds: 10
              successThreshold: 1
              timeoutSeconds: 1
            name: controller
            ports:
            - name: prometheus
              containerPort: 10254
            - containerPort: 80
              name: http
              protocol: TCP
            - containerPort: 443
              name: https
              protocol: TCP
            - containerPort: 8443
              name: webhook
              protocol: TCP

          -------------
          
## Service 수정

가이드에 나와있듯이 ingress manifest의 service 부분을 수정해주어야한다.


![프로메테우스3](https://user-images.githubusercontent.com/68090443/194750210-0800cdd7-f52b-4371-88aa-30b84020802a.PNG)


위사진과 같이 추가해주면 된다.

## Deployment 수정

이제 ingress manifest의 Deployment 부분을 수정해주어야한다.


![프로메테우스설정2](https://user-images.githubusercontent.com/68090443/194750271-2ecc75b7-353b-4e19-a22c-789a7533fbb5.PNG)


![프로메테우스 설정1](https://user-images.githubusercontent.com/68090443/194750292-8af3a13c-2bdc-405b-aba7-1625c8f37376.PNG)

위 사진과 같이 추가해주자!

## 프로메테우스 실행

    kubectl apply --kustomize github.com/kubernetes/ingress-nginx/deploy/prometheus/

prometheus를 배포해준다.

## 확인

아래 명령어로 prometheus를 확인하고 접속해보자!

    kubectl get svc -n ingress-nginx
    
![프로메테우스설정1](https://user-images.githubusercontent.com/68090443/194750425-adb638b5-01bc-4e09-a282-c7698c558b9f.PNG)

node port로 접속해보자


![프로메테우스설정2](https://user-images.githubusercontent.com/68090443/194750516-a547d5b4-4991-45cc-9cfa-3b8b9fa736cd.png)


정상적으로 Prometheus가 설치 완료됐다.

# Grafana install



