# Kubernetes metrics

metrics란 지표를 뜻 합니다.

Kubernetes metrics은 쿠버네티스의 다양한 정보를 수집한 지표입니다.

예를 들면 CPU 사용률, memory 사용률 등이 있습니다.

프로덕션에서 Kuberenetes의 배포는 수천, 심지어 수만 개의 컨테이너를 실행하는 범위가 방대하기로 유명합니다. 이 양의 컨테이너를 추적하면 많은 복잡성이 발생할 수 있습니다.

Kubernetes 메트릭은 프로세스에 대한 가시성을 도입하여 컨테이너를 추적하는 데 도움이 됩니다. 


## kubernetes Metric-Server

Kubernetes Metrics Server는 클러스터 전체의 리소스 사용 데이터를 수집합니다. 
Kubelets에서 리소스 메트릭을 수집하고 이를 Metrics API 를 통해 Kubernetes apiserver에 노출하여 Horizontal Pod Autoscaler 및 Vertical Pod Autoscaler 에서 사용할 수 있도록 합니다.

[kubernetes metric-server 저장소](https://github.com/kubernetes-sigs/metrics-server)

## 설치

    kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml


[kubernetes metric-server 저장소](https://github.com/kubernetes-sigs/metrics-server)



## 확인

    kubectl top nodes

