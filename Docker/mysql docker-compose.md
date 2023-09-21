docker-compose.yaml
    
    version: '3'
    services:
        # 서비스 명
        mysql:
            image: mysql:8.0
            restart: always
            container_name: mysql
            ports:
              - "3306:3306"
            environment:
                MYSQL_ROOT_PASSWORD: qkrqjatjs15
                TZ: Asia/Seoul
            command:
                - --character-set-server=utf8mb4
                - --collation-server=utf8mb4_unicode_ci
            volumes:
                - data1:/var/lib/mysql
    
    volumes:
      data1:
