# kafka 클러스터


1 zookeeper, 3 kafka, kafka ui


![스크린샷 2023-06-12 오후 9 17 41](https://github.com/beomsun1234/TIL/assets/68090443/b6d6dee2-e4ef-4fe4-9196-6ebdae1938a2)




## docker compose

kafka.yaml

    version: '3.8'
    services:
      zookeeper-1:
        image: confluentinc/cp-zookeeper:5.5.1
        ports:
          - '2181:2181'
        environment:
          ZOOKEEPER_CLIENT_PORT: 2181
          ZOOKEEPER_TICK_TIME: 2000
        restart: always
        volumes:
          - ~/data/zookeeper/data:/data
          - ~/data/zookeeper/datalog:/datalog

      kafka-1:
        image: confluentinc/cp-kafka:5.5.1
        ports:
          - '9091:9091'
        volumes:
          - ~/data/kafka1/data:/tmp/kafka-logs
        depends_on:
          - zookeeper-1
        restart: always
        environment:
          KAFKA_BROKER_ID: 1
          KAFKA_LISTENERS: INTERNAL://kafka-1:29091,EXTERNAL://0.0.0.0:9091
          KAFKA_ZOOKEEPER_CONNECT: zookeeper-1:2181
          KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT
          KAFKA_INTER_BROKER_LISTENER_NAME: INTERNAL
          KAFKA_ADVERTISED_LISTENERS: INTERNAL://kafka-1:29091,EXTERNAL://34.64.113.226:9091
          KAFKA_DEFAULT_REPLICATION_FACTOR: 3
          KAFKA_NUM_PARTITIONS: 3


      kafka-2:
        image: confluentinc/cp-kafka:5.5.1
        ports:
          - '9092:9092'
        volumes:
          - ~/data/kafka2/data:/tmp/kafka-logs
        depends_on:
          - zookeeper-1
        restart: always
        environment:
          KAFKA_BROKER_ID: 2
          KAFKA_LISTENERS: INTERNAL://kafka-2:29092,EXTERNAL://0.0.0.0:9092
          KAFKA_ZOOKEEPER_CONNECT: zookeeper-1:2181
          KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT
          KAFKA_INTER_BROKER_LISTENER_NAME: INTERNAL
          KAFKA_ADVERTISED_LISTENERS: INTERNAL://kafka-2:29092,EXTERNAL://34.64.113.226:9092
          KAFKA_DEFAULT_REPLICATION_FACTOR: 3
          KAFKA_NUM_PARTITIONS: 3


      kafka-3:
        image: confluentinc/cp-kafka:5.5.1
        ports:
          - '9093:9093'
        volumes:
          - ~/data/kafka3/data:/tmp/kafka-logs
        depends_on:
          - zookeeper-1
        restart: always
        environment:
          KAFKA_BROKER_ID: 3
          KAFKA_LISTENERS: INTERNAL://kafka-3:29093,EXTERNAL://0.0.0.0:9093
          KAFKA_ZOOKEEPER_CONNECT: zookeeper-1:2181
          KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT
          KAFKA_INTER_BROKER_LISTENER_NAME: INTERNAL
          KAFKA_ADVERTISED_LISTENERS: INTERNAL://kafka-3:29093,EXTERNAL://34.64.113.226:9093
          KAFKA_DEFAULT_REPLICATION_FACTOR: 3
          KAFKA_NUM_PARTITIONS: 3
          
      kafka-ui:
        image: provectuslabs/kafka-ui
        container_name: kafka-ui
        ports:
          - "8989:8080"
        restart: always
        depends_on:
          - kafka-1
          - kafka-2
          - kafka-3
        environment:
          - KAFKA_CLUSTERS_0_NAME=beom
          - KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=kafka-1:29091,kafka-2:29092,kafka-3:29093
          - KAFKA_CLUSTERS_0_ZOOKEEPER=zookeeper-1:2181
