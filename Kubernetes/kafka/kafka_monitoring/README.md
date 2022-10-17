# kafka monitoring

```Grafana Dashboard```

![카프카모니터링](https://user-images.githubusercontent.com/68090443/195311055-b36d33e1-2f9e-44f1-85db-38d00ea6e851.PNG)


## kafka_exporter 

[kafka_exporter helm 깃허브](https://github.com/danielqsj/kafka_exporter)


## prometheus 

[prometheus helm 깃허브](https://github.com/prometheus-community/helm-charts)





# 트러블슈팅

worker node 1 에 cpu 사용량이 100이 넘어서 뻗어서 worker node 1에서 돌아가는 pod들이 모두 terminating 상태가 되었다. worker node 1를 정지했다 재 시작 해야하니 카프카나 다른 앱들은 정상적으로 pod들이 재시작 되었다.. 하지만 kafka_exporter pod가 재시작되지 않아서 prometheus에서 카프카 메트릭을 수집하지 못해서 그라파나 대시보드에서 모든 데이터가 no가 되었다.. 

kafka_exporter helm chart에 values 부분에 restartPolicy: Always 를 추가해주므로 해결 할 수 있었다.

values.yaml 부분


    # Default values for kafka-exporter.
    # This is a YAML-formatted file.
    # Declare variables to be passed into your templates.

    replicaCount: 1

    image:
      repository: danielqsj/kafka-exporter
      tag: latest
      pullPolicy: IfNotPresent

    nameOverride: ""
    fullnameOverride: ""
    restartPolicy: Always
    
    service:
      type: ClusterIP
      port: 9308

    kafkaExporter:
      kafka:
        servers: []
          - kafka-0.kafka-headless.default.svc.cluster.local:9092
        # version: "1.0.0"

      sasl:
        enabled: false
        handshake: true
        username: ""
        password: ""
        mechanism: ""

      tls:
        enabled: false
        insecureSkipTlsVerify: false
        caFile: ""
        certFile: ""
        keyFile: ""

      log:
        verbosity: 0
        enableSarama: false

    prometheus:
      serviceMonitor:
        enabled: true
        namespace: monitoring
        interval: "30s"
        additionalLabels:
          app: kafka-exporter
        additionalScrapeConfigs:
          - job_name: "kafka-exporter"
            static_configs:
              - targets: ["kafka-exporter.default.svc:9308"]
        metricRelabelings: {}

    labels: {}
    podLabels: {}

    # Adds in Datadog annotations needed to scrape the prometheus endpoint.
    # prefix is required. If added, will provide a metric such as test.kafka_brokers.
    # Example metrics below. map metric name to a potential new metric name in dd.
    datadog:
      use_datadog: false
      prefix: <dd_prefix>
      metrics: [
        {"kafka_brokers": "kafka_brokers"},
        {"kafka_consumergroup_lag": "kafka_consumergroup_lag"},
        {"kafka_consumergroup_current_offset": "kafka_consumergroup_current_offset"}
        ]

    resources: {}
      # We usually recommend not to specify default resources and to leave this as a conscious
      # choice for the user. This also increases chances charts run on environments with little
      # resources, such as Minikube. If you do want to specify resources, uncomment the following
      # lines, adjust them as necessary, and remove the curly braces after 'resources:'.
      # limits:
      #   cpu: 100m
      #   memory: 128Mi
      # requests:
      #   cpu: 100m
      #   memory: 128Mi

    nodeSelector: {}

    tolerations: []

    affinity: {}
