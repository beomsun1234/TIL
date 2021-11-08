# 도커를 이용한 Kafka 환경 구축

docker와 docker compose가 설치되어 있다고 가정한다.

## 환경구축

1. 우선 git clone을 통해 해당 레포지토리를 받아온다. 

		$ git clone https://github.com/wurstmeister/kafka-docker

2. 클론 받아 온 후 클론 받은 파일을 확인하면 docker-compose-single-borker.yml이 있을 것이다. yml 파일을 수정해 주자(나는 한대의 카프카서버를 구축할 것이기에 docker-compose-single-borker.yml을 수정해준 것 이다.)


    version: '2'
    services:
      zookeeper:
        image: wurstmeister/zookeeper
        container_name: zookeeper
        ports:
          - "2181:2181"
      kafka:
        image: wurstmeister/kafka:2.12-2.5.0
        container_name: kafka
        ports:
          - "9092:9092"
        environment:
          KAFKA_ADVERTISED_HOST_NAME: 127.0.0.1 # 로컬에서 실행하므로 127.0.0.1로 수정
          KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
          KAFKA_ADVERTISED_PORT: 9092
        depends_on:
          - zookeeper
        volumes:
          - /var/run/docker.sock:/var/run/docker.sock
     

위와 같이 yml을 변경해주고 

	docker-compose -f docker-compose-single-broker.yml up

위 명령어를 실행시켜주고 docker ps를 입력하면 kafka와 zookeeper 두개의 컨테이너가 동작하고 있으면 성공이다.

	docker exec -it kafka bash

위 명령어를 통해 카프카에 접속하고 

	kafka-topics.sh --list --bootstrap-server localhost:9092

위 명령어를 통해 카프카 서버에 토픽을 확인할 수 있다.


## Kafka 명령어

### 토픽생성

    kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic 토픽이름
    
### 토픽 리스트 확인

	kafka-topics.sh --list --bootstrap-server localhost:9092
    
### 컨슈머 그룹 리스트 확인

	kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list

### 컨슈머 상태와 오프셋 확인

	kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group test-consumer --describe
    
### 토픽의 파티션 수 변경

	kafka-topics.sh --zookeeper zookeeper:2181 --alter --topic test-topic -partitions 2
    
- 카프카에서는 운영 중에 간단한 명령어로 토픽의 파티션 수를 늘려줄 수 있음.
- 주의할 점은 토픽의 파티션 수는 증가만 가능하고, 감소는 불가능.
- 파티션만 증가했다고 메시지에 대한 전체 처리 성능이 좋아지는 것은 아님.
- 파티션의 수만큼 컨슈머 역시 추가해줘야 함.//producer실행

### Producer 실행

	kafka-console-producer.sh --broker-list localhost:9092 --topic (토픽이름)

### cousumer 실행

	kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic (토픽이름)
