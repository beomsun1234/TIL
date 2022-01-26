
## ELK 

```우선 ELK( Elasticsearch, Logstash, Kibana)를 도커를 이용해서 ELK를 설치```

    git clone https://github.com/deviantony/docker-elk.git

    cd docker-elk

1. Elasticsearch 설정

        cd elasticsearch


    Dockerfile 변경

        ARG ELK_VERSION

        # https://www.docker.elastic.co/
        FROM docker.elastic.co/elasticsearch/elasticsearch:${ELK_VERSION}

        # Add your elasticsearch plugins setup here
        # Example: RUN elasticsearch-plugin install analysis-icu
        RUN elasticsearch-plugin install analysis-nori ##여기 추가
    
    config 설정(elasticsearch.yml)

        cd config

        ---
        ## Default Elasticsearch configuration from Elasticsearch base image.
        ## https://github.com/elastic/elasticsearch/blob/master/distribution/docker/src/docker/config/elasticsearch.yml
        #
        cluster.name: "docker-cluster"
        network.host: 0.0.0.0

        ## x팩 부분을 전부 제거해준다


2. kibana 설정

    config 설정(kibana.yml)

        cd kibana/config
        ---
        ## Default Kibana configuration from Kibana base image.
        ## https://github.com/elastic/kibana/blob/master/src/dev/build/tasks/os_packages/docker_generator/templates/kibana_yml.template.ts
        #
        server.name: kibana
        server.host: 0.0.0.0
        elasticsearch.hosts: [ "http://elasticsearch:9200" ]
        monitoring.ui.container.elasticsearch.enabled: true

        ## x팩 제거


3. logstash 설정

    config 설정(logstash.yml)

        cd logstash/cofig

        ---
        ## Default Logstash configuration from Logstash base image.
        ## https://github.com/elastic/logstash/blob/master/docker/data/logstash/config/logstash-full.yml
        #
        http.host: "0.0.0.0"
        xpack.monitoring.elasticsearch.hosts: [ "http://elasticsearch:9200" ]
        ## x팩 제거

     lgstash.conf 설정

        cd logstash/pipeline

        -----

        input {
            tcp {
                port => 5000
            }
        }

        ## Add your filters / logstash plugins configuration here

        output {
            elasticsearch {
                hosts => "elasticsearch:9200"
                index => "logstash-log"
                user => "username"
                password => "password"
            }
        }

설정 완료 후 실행

    docker-compose build && docker-compose up -d 

    http://{ip-address}:5601/로 Kibana에 접속


spring boot과 연결하기위해 logback.xml을 만들어준다.(생략)

이 후 로그가 찍히면 kibana대시보드에서 확인 할 수 있다.

```References```

[ELK세팅부터 알람까지 - 우아한 형제들 기술 블로그]( https://techblog.woowahan.com/2659/)
