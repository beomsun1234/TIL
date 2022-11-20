## istio 모니터링 관련

설치된 istio 폴더에 들어간다. 

  cd istio-1.16.0
  


Granfana, Jaeger, Kiali, Prometheus 모두 실행시킨다.

[설치법](https://github.com/istio/istio/tree/master/samples/addons)

  kubectl apply -f samples/addons

모두 설치해 준다. 모든 서비스들의 타입이 clusterIP 이다. istio-gateway에 등록해서 사용해도 되지만 Kiali는 nodeport로 변경해서 열어 주었다.

아래 kiali.yaml의 변경한 service 부분이다.


    # Source: kiali-server/templates/service.yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: kiali
      namespace: istio-system
      labels:
        helm.sh/chart: kiali-server-1.55.1
        app: kiali
        app.kubernetes.io/name: kiali
        app.kubernetes.io/instance: kiali
        version: "v1.55.1"
        app.kubernetes.io/version: "v1.55.1"
        app.kubernetes.io/managed-by: Helm
        app.kubernetes.io/part-of: "kiali"
      annotations:
    spec:
      type: NodePort
      ports:
      - name: http
        protocol: TCP
        port: 20001
        nodePort: 30001
      - name: http-metrics
        protocol: TCP
        port: 9090

      selector:
        app.kubernetes.io/name: kiali
        app.kubernetes.io/instance: kiali

