# Kubernetes 특정 Node에 Pod할당

Kubernetes는 scheduler를 통해 pod를 할당합니다. 

특정 노드에서만 특정 파드를 할당 하고 싶은 경우 방법을 알아보겠습니다.

##  nodeSelector

### node label 추가

    kubectl label nodes <your-node-name> [key]=[value]
  
ex)
  
    kubectl label node k8s-worker-03 worker=service
  
### node label 제거
  
    kubectl label nodes <your-node-name> [key]-

ex)
  
    kubectl label node k8s-worker-03 worker-
  

### 선택한 노드에 스케줄되도록 파드 생성하기

nginx.yaml

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-deployment
      labels:
        app: nginx
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - name: nginx
            image: nginx:1.14.2
            ports:
            - containerPort: 80
          nodeSelector:
            worker: service
            
            
nodeSelector 부분에 pod를 스케줄링할 node의 label을 입력해줍니다. [key]: [value]



                     
          
