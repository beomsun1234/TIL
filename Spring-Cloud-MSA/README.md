# hello msa

## Service Discovery

- Spring Cloud Netflix Eureka를 사용, Eureka의 역할 -> Service Discovery
- Service Discovery는 말그대로 외부의 서비스들이 마이크로서비스를 검색하기 위해 사용하는 일종의 전화번호부와 같은 역할
- 각각의 마이크로서비스가 어느 위치에 있는지 등록해 놓은 정보
- 요청 정보가 Load Balancer(API Gateway)에 전달되면 다음으로 service Discovery에 전달된다. Service Discovery로 정보가 전달되는 것은 필요한 정보가 어디 있는 지 묻는 행위와 같다. 그럼 service Discovery는 필요한 서비스가 어느 곳에 있는지에 대한 정보를 API Gateway로 반환하고 API Gateway는 이에 따라 해당 서비스를 호출하고 결과를 받는다.

- 각각의 서비스의 위치가 등록된 서버에서 특정 작업을 위한 서버의 위치를 파악하는 작업을 뜻한다. Service Discovery를 위해서 Spring Cloud Netflix - Eureka Server를 사용한다.


### Spring Cloud Eureka Server 설정

의존성 설정


    dependencies {
        implementation 'org.springframework.boot:spring-boot-starter-actuator'
        implementation 'org.springframework.cloud:spring-cloud-starter-netflix-eureka-server'
        developmentOnly 'org.springframework.boot:spring-boot-devtools'
        testImplementation 'org.springframework.boot:spring-boot-starter-test'
    }
    
application.yml 작성

    server:    					
      port: 8761                # 1

    spring: 					
      application:
        name: discovery-service # 2

    eureka:                     
      client:
        register-with-eureka: false # 3
        fetch-registry: false # 4
        
- #1 
	 - 해당 유레카 서버가 동작되는 서버의 포트를 지정한다. 보통 8761 포트를 사용
- #2
    - 마이크로서비스를 담당하는 스프링 부트 프레임 워크에 각각의 마이크로서비스에 고유한 아이디를 부여 -> name,  모든 서비스를 spring.application.name 으로 식별한다.
- #3,4 
 	- eureka 라이브러리가 포함된 채 스프링부트가 구동이 되면 기본적으로 eureka 클라이언트의 역할로서 어딘가에 등록하는 작업을 시도한다.
 	- register-with-eureka,fetch-registry 설정들은 기본값이 true로 현재 작업하고 있는 것을 client의 역할로 전화번호부에 등록하는 것과 같다.
 	- 현재 이건 서버가 될 것인데 자신의 정보를 자신에게 등록하는 현상이 된다. 의미가 없는 작업이므로 false로 수정
 	
 정리하자면 유레카 서버 자체를 구동하지만 유레카 서버 자체의 정보는 등록할 필요가 없다는 것
 유레카는 연결 역할을 하는 것으로 다른 서비스들을 등록하는 거지 자기 자신은 등록필요가 없다 
 
 - eureka.client.register-with-eureka : 해당 서버를 클라이언트로 동작시키겠냐는 설정을 false 로 설정해야 한다.
- eureka.client.fetch-registry : 위와 동일한 false로 지정해야 하는데, 그렇지 않으면 자신을 디스커버리에 등록하게 된다.
 
 XXApplication에 @EnableEurekaServer 어노테이션 추가 후 실행
 
---

## Service Registry

- 각각의 서비스가 자신의 위치(IP) 정보를 특정 서버에 등록 Registry 하는 작업을 말한다.
 Service Registry를 위해서 Spring Cloud Netflix - Eureka Client를 사용한다.
 
### Spring Cloud Eureka Client

 2개의 마이크로서비스를 구성한다고 가정해 보자
 
- User 서비스 user-service
- board 서비스 board-service

user-service 의존성 설정

    dependencies {
        implementation 'org.springframework.boot:spring-boot-starter-web'
        implementation 'org.springframework.cloud:spring-cloud-starter-netflix-eureka-client'
        compileOnly 'org.projectlombok:lombok'
        developmentOnly 'org.springframework.boot:spring-boot-devtools'
        annotationProcessor 'org.projectlombok:lombok'
        testImplementation 'org.springframework.boot:spring-boot-starter-test'
        runtimeOnly 'com.h2database:h2'
        implementation('org.springframework.boot:spring-boot-starter-data-jpa')
    }
    
    
user-service의 application.yml 설정

    server:
      port: 8081

    spring:
      application:
        name: msa-user-service
      datasource:
        driver-class-name: org.h2.Driver
        username: sa
        password: 1234
        url: jdbc:h2:tcp://localhost/~/msaut
      jpa:
        hibernate:
          ddl-auto: update
        show-sql: true
        
    eureka:
      client:
        register-with-eureka: true   # 유레카에 등록
        fetch-registry: true        # 레지스트리 정보 로컬에 캐시 여부
        service-url:                # 서비스를 등록할 서버의 주소 지정
          defaultZone: http://localhost:8761/eureka  # Eureka Client로써 Eureka Server에 등록하기 위해 사용되는 Endpoint가 http://localhost:8761/eureka 이므로 뒤에 /eureka를 붙여줘야 한다.


board service 의존성 설정


    dependencies {
        implementation 'org.springframework.boot:spring-boot-starter-web'
        implementation 'org.springframework.cloud:spring-cloud-starter-netflix-eureka-client'
        compileOnly 'org.projectlombok:lombok'
        developmentOnly 'org.springframework.boot:spring-boot-devtools'
        annotationProcessor 'org.projectlombok:lombok'
        testImplementation 'org.springframework.boot:spring-boot-starter-test'
        runtimeOnly 'com.h2database:h2'
        implementation('org.springframework.boot:spring-boot-starter-data-jpa')
    }
    
board service의 application.yml

    server:
      port: 8080

    spring:
      application:
        name: msa-board-service
      datasource:
        driver-class-name: org.h2.Driver
        username: sa
        password: 1234
        url: jdbc:h2:tcp://localhost/~/msaut
      jpa:
        hibernate:
          ddl-auto: update
        show-sql: true

    eureka:
      client:
        register-with-eureka: true
        fetch-registry: true
        service-url:
          defaultZone: http://localhost:8761/eureka




- eureka.client.register-with-eureka & fetch-registry 이번에는 해당 서비스가 클라이언트로 인식되어야 하므로 true로 해주자
- eureka.client.service-url.defaultZone : eureka server 가 위치하고 있는 기본 주소를 적어줄 수 있다.
defaultZone 같은 경우는 꼭 Camel Case 로 적어야 한다고 Spring Cloud Eureka에 나와있다.


XXApplication에 @EnableDiscoveryClient 어노테이션 추가

이후 실행 하면 Eureka Server에 접속하면(http://localhost:8761) 접속하면 Eureka Dashboard에서 등록한 두개의 서비스가 추가될 것이다.

---

##  API Gateway Service 

- API Gateway는 모든 클라이언트의 요청을 받아 설정해 놓은 라우팅 설정에 따라서 각각의 endPoint로 클라이언트 대신에 요청을 보내고 응답을 받아 클라이언트에게 전달하는 프록시 역할
- 시스템 내부 구조는 숨기고 외부의 요청에 대해서 적절한 형태로 가공해서 응답한 수 있다는 장점
- 간단히 말하자면, 중간의 진입로 역할 -> 클라이언트는 직접적으로 마이크로서비스를 호출하지 않고 클라이언트는 Gateway만 상대한다.
- 클라이언트 요청 -> API Gateway -> Eureka Server에서 마이크로서비스 위치 정보 반환 -> API Gateway -> 해당 마이크로서비스로 이동 -> API Gateway로 응답 반환 -> 클라이언트에게 반환



|명칭|설명|
|------|---|
|라우트(Route)|라우트는 목적지 URI, 조건자 목록과 필터의 목록을 식별하기 위한 고유 ID로 구성된다. 라우트는 모든 조건자가 충족됐을 때만 매칭된다|
|조건자(Predicates)|각 요청을 처리하기 전에 실행되는 로직, 헤더와 입력된 값 등 다양한 HTTP 요청이 정의된 기준에 맞는지를 찾는다.|
|필터(Filters)|HTTP 요청 또는 나가는 HTTP 응답을 수정할 수 있게한다. 다운스트림 요청을 보내기전이나 후에 수정할 수 있다. 라우트 필터는 특정 라우트에 한정된다|


gateway service 의존성 설정 

    dependencies {
        implementation("org.springframework.cloud:spring-cloud-starter-gateway")
        implementation 'org.springframework.cloud:spring-cloud-starter-netflix-eureka-client'
        compileOnly 'org.projectlombok:lombok'
        developmentOnly 'org.springframework.boot:spring-boot-devtools'
        annotationProcessor 'org.projectlombok:lombok'
        testImplementation 'org.springframework.boot:spring-boot-starter-test'
    }

gateway service application.yml 설정

	server:
    	port: 8000
        
	eureka:
      	client:
        	register-with-eureka: true
        	fetch-registry: true
        	service-url:
          	defaultZone: http://localhost:8761/eureka
	spring:
  		application:
    		name: msa-gateway

 		 cloud:
   			 gateway:
    			  routes:        # 라우팅설정           	
     				- id: msa-user-service   # 그냥 구분하기 위한 값, 임의로 작성해도 무관
          			  uri: lb://msa-user-service # lb는 Load Balancer의 약자로 마이크로서비스에서 spring.application.name으로 정해둔 것
          			  predicates: 
           				- Path=/auth/** # 클라이언트로부터 Gateway에 명시한 path로 요청이 오면 url의 네임을 확인하여, Discovery Service(Eureka)에 등록되어있는 마이크로서비스 중에서, 해당 이름을 가진 서비스로 포워딩 시킨다.
           				#ex) localhost:8000/auth/info 로 요청이오면(게이트웨이로) localhost:8081/auth/info로 전달.
           				

                    - id: msa-user-service
                      uri: lb://msa-user-service
                      predicates:
                        - Path=/user-service/**
                      filters:# 필터 적용(토큰 확인용)
                        - AuthorizationHeaderFilter
                        - RewritePath=/user-service/?(?<segment>.*), /$\{segment}

                    - id: msa-board-service
                      uri:lb://msa-board-service
                      predicates:
                        - Path=/board-service/**
                      filters: # 필터 적용(토큰 확인용)
                        - AuthorizationHeaderFilter
                        - RewritePath=/board-service/?(?<segment>.*), /$\{segment}

       
       
  
- spring.cloud.gateway.routes : 라우팅에 대한 정보
- spring.cloud.gateway.routes.id : 해당 라우팅이 어떠한 이름으로 라우팅 될 것인지에 대한 이름
- spring.cloud.gateway.routes.uri : 현재 라우팅을 어디에 포워딩 시킬 것인지를 명시해준다.
- spring.cloud.gateway.routes.predicates : 조건식으로 특정 요청이 predicates에 맞는 조건으로 들어오면 해당 route를 수행할 것을 지정한다.


필터

  	@Component
  	@Slf4j
  	public class AuthorizationHeaderFilter extends AbstractGatewayFilterFactory<AuthorizationHeaderFilter.Config> {
      private JwtUtil jwtUtil;
      public AuthorizationHeaderFilter(JwtUtil jwtUtil) {
          super(Config.class);
          this.jwtUtil = jwtUtil;
      }

      private Mono<Void> handleUnAuthorized(ServerWebExchange exchange) {
          ServerHttpResponse response = exchange.getResponse();
          response.setStatusCode(HttpStatus.UNAUTHORIZED);
          response.writeWith(s -> {
              log.info("error");
          });
          return response.setComplete();
      }

      @Override
      public GatewayFilter apply(AuthorizationHeaderFilter.Config config) {
          return ((exchange, chain) -> {
              ServerHttpRequest request = exchange.getRequest();

              // Request Header 에 token 이 존재하지 않을 때
              if(!request.getHeaders().containsKey("Authorization")){
                  return handleUnAuthorized(exchange); // 401 Error
              }
              // Request Header 에서 token 문자열 받아오기
              List<String> token = request.getHeaders().get("Authorization");
              String tokenString = Objects.requireNonNull(token).get(0);
              log.info("token={}",tokenString);
              if(!tokenString.startsWith("Bearer")){
                  return handleUnAuthorized(exchange);
              }
              String jwtToken = jwtUtil.extractHeader(tokenString);
              // 토큰 검증
              if(!jwtUtil.validateToken(jwtToken)) {
                  return handleUnAuthorized(exchange); // 토큰이 일치하지 않을 때
              }
              return chain.filter(exchange); // 토큰이 일치할 때
          });
      }

      public static class Config {

      }

    }
