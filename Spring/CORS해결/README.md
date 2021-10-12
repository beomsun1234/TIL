# CORS 해결법

## Configuration 을 통해 Global하게 적용하기

### addMapping

    @Configuration
    public class WebConfig implements WebMvcConfigurer {
        @Override
        public void addCorsMappings(CorsRegistry registry) {
            registry.addMapping("/**");
    }    
    
    
- registry.addMapping을 이용해서 CORS를 적용할 URL패턴을 정의할 수 있다.

- 위 처럼 "/**" 와일드 카드를 사용할 수도 있다. 
- "/somePath/**" 이렇게 적용할 수도 있다.

- Default
    - Allow all origins.
    - Allow "simple" methods GET, HEAD and POST.
    - Allow all headers.
    - Set max age to 1800 seconds (30 minutes).
    
### allowedOrigins

    @Configuration
    public class WebConfig implements WebMvcConfigurer {
        @Override
        public void addCorsMappings(CorsRegistry registry) {
            registry.addMapping("/**")
                    .allowedOrigins("*");
    }    
    
- allowedOrigins 메소드를 이용해서 자원 공유를 허락할 Origin을 지정할 수 있다.
- 위 처럼 "*"로 모든 Origin을 허락할 수 있습니다.
- allowedOrigins("http://localhost:3000", "http://localhost:8081") 를 통해 한번에 여러 Origin을 설정할 수 있다.

### allowedMethods

    @Configuration
    public class WebConfig implements WebMvcConfigurer {
        @Override
        public void addCorsMappings(CorsRegistry registry) {
            registry.addMapping("/**")
                    .allowedOrigins("*")
                    .allowedMethods("*");
    }
    
- allowedMethods를 이용해서 허용할 HTTP method를 지정할 수 있다.

- 위 처럼 여러개를 지정할 수 있고 마찬가지로 "*"를 이용하여 모든 method를 허용할 수 있다.    
    
