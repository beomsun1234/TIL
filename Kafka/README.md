# Kafka 란?

하루에 1조4천억 건의 메시지를 처리하기 위해 LinkedIn이 개발한 내부 시스템으로 시작했으나, 현재 이는 다양한 기업의 요구사항을 지원하는 애플리케이션을 갖춘 오픈소스 데이터 스트리밍 솔루션이 되었다.  Kafka는 실시간으로 기록 스트림을 게시, 구독, 저장 및 처리할 수 있는 분산 데이터 스트리밍 플랫폼이다. 이는 여러 소스에서 데이터 스트림을 처리하고 여러 사용자에게 전달하도록 설계되었고 간단히 말해, A지점에서 B지점까지 이동하는 것뿐만 아니라 A지점에서 Z지점을 비롯해 필요한 모든 곳에서 대규모 데이터를 동시에 이동할 수 있다고 한다.


시스템 간 데이터가 불일치 문제가 발생하는 문제를 해결하기 위해서 탄생했다.

|용어|설명|
|------|---|
|producer|메세지 생산(발행)자|
|consumer|메세지 소비자, 하나의 서버|
|consumer group|consumer 들끼리 메세지를 나눠서 가져간다.offset 을 공유하여 중복으로 가져가지 않는다.|
|broker| 카프카 서버|
|zookeeper|카프카 서버 (+클러스터) 상태를 관리|
|cluster|브로커들의 묶음|
|topic| 메세지 종류, 데이터베이스의 table정도의 개념으로 생각 카프카에 저장되는 데이터를 구분하기위해 토픽이라는 이름을 사용한다.|
|partitions|topic 이 나눠지는 단위 하나의 파티션에 대해 데이터의 순서를 보장한다. 만약 토픽에 대해 모든데이터의 순서를 보장받고 싶다면 파티션의 수를 1로 생성하면 된다. 파티션은 각각의 파티션에 대해서만 순서를 보장하고 만약 파티션의 숫작 많아진다면 프로듀서가 보낸 순서대로 메시지를 가져올 수 없다|
|offset|파티션 내에서 각 메시지가 가지는 unique id|


카프카의 브로커(broker)는 토픽(topic)을 기준으로 메시지를 관리합니다.
프로듀서(producer)는 특정 토픽의 메시지를 생성한 뒤 해당 메시지를 브로커에게 전달합니다. 브로커가 전달받은 메시지를 토픽별로 분류하여 쌓아놓으면,
해당 토픽을 구독하는 컨슈머(consumer)들이 메시지를 가져가서 처리하게 됩니다.
카프카는 확장성(scale-out)과 고가용성(high availability)을 위하여 브로커들이 클러스터로 구성되어 동작하도록 설계되어있습니다.


#### Zookeeper 란?
분산 코디네이션 서비스 제공
코디네이션 서비스는 분산 시스템 내에서 중요한 상태정보를 유지하기 때문에 고가용성을 제공해야함
서버와 클라이언트로 구성
서버앙상블 : n개 서버로 단일 주키퍼 클러스터 구성
클라이언트 : 앙상블에 속한 서버에 연결하여 서비스 사용


### 토픽(topic), 파티션(partition)
- 카프카 클러스터는 토픽이라는 곳에 데이터를 저장합니다.
- 카프카에 저장되는 메시지는 토픽으로 분류되고 토픽은 여러개의 파티션으로 나눠진다.
- 파티션안에는 메시지의 위치를 나타내는 오프셋(offset)이 있는데, 이 오프셋 정보를 이용해서 가져간 메시지의 위치정보를 알 수 있다.

### 컨슈머(consumer), 컨슈머그룹(consumer group)
- 컨슈머는 카프카 토픽에서 메시지를 읽어오는 역할을 한다.
- 컨슈머 그룹은 하나의 토픽에 여러 컨슈머 그룹이 동시에 접속해 메시지를 가져올 수 있다.
- 컨슈머그룹은 컨슈머가 프로듀서의 메시지 생성 속도를 따라가지 못할 때, 컨슈머 확장을 용이하게 할 수 있도록 하기위한 기능.

출저 https://saramin.github.io/2019-09-17-kafka/
