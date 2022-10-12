# mariadb_monitoring

[사진]


## mariadb exporter
mariadb exporter 배포

mariadb_exporter.yaml


    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: mysqld-exporter
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: mysqld-exporter
      template:
        metadata:
          labels:
            app: mysqld-exporter
        spec:
          containers:
          - name: mysqld-exporter
            image: prom/mysqld-exporter:v0.12.1
            args:
            - --collect.info_schema.tables
            - --collect.info_schema.innodb_tablespaces
            - --collect.info_schema.innodb_metrics
            - --collect.global_status
            - --collect.global_variables
            - --collect.slave_status
            - --collect.info_schema.processlist
            - --collect.perf_schema.tablelocks
            - --collect.perf_schema.eventsstatements
            - --collect.perf_schema.eventsstatementssum
            - --collect.perf_schema.eventswaits
            - --collect.auto_increment.columns
            - --collect.binlog_size
            - --collect.perf_schema.tableiowaits
            - --collect.perf_schema.indexiowaits
            - --collect.info_schema.userstats
            - --collect.info_schema.clientstats
            - --collect.info_schema.tablestats
            - --collect.info_schema.schemastats
            - --collect.perf_schema.file_events
            - --collect.perf_schema.file_instances
            - --collect.perf_schema.replication_group_member_stats
            - --collect.perf_schema.replication_applier_status_by_worker
            - --collect.slave_hosts
            - --collect.info_schema.innodb_cmp
            - --collect.info_schema.innodb_cmpmem
            - --collect.info_schema.query_response_time
            - --collect.engine_tokudb_status
            - --collect.engine_innodb_status
            ports:
            - containerPort: 9104
              protocol: TCP
            env:
            - name: DATA_SOURCE_NAME
              value: "root:1234@(mariadb.default.svc.cluster.local:3306)/"
      
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: mysqld-exporter
      labels:
        app: mysqld-exporter
    spec:
      type: NodePort
      ports:
      - port: 9104
        protocol: TCP
        name: http
      selector:
        app: mysqld-exporter


운영환경에서는 configmap 사용해서 아래 부분 보완 해야한다.

     env:
       - name: DATA_SOURCE_NAME


## prometheus manifest 수정

[prometheus-community helm chart 저장소](https://github.com/prometheus-community/helm-charts)를 git clone 했다고 가정합니다.


vi /helm-charts/charts/prometheus/values.yaml


    serverFiles:
       ......
       
       prometheus.yml:
         .......
         
         scrape_configs:
           - job_name: "mysql-exporter"
             static_configs:
               - targets: ["mysqld-exporter.default.svc:9104"]
               
targets 부분에 exporter 주소를 넣어주면된다. dns는 [exporter 서비스명].[namespace명].svc:[exporter 포트] 이다.

## grafana dashboard

[대시보드](https://grafana.com/grafana/dashboards/7362-mysql-overview/)

