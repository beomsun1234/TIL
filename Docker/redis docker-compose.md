# redis 

    version: "3"
      
    services:
      redis:
        image: redis:7.2.2
        ports:
          - 6379:6379
        volumes:
          - redis_data:/data
          - redis_config:/usr/local/etc/redis/redis.conf
        restart: always
        command: redis-server /usr/local/etc/redis/redis.conf
    volumes:
      redis_data:
      redis_config:
