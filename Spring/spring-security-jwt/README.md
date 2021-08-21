웹 보안은 기본적으로 요청하는 사용자를 식별하는 인증(Authenticate)과 인증된 사용자가 보호된 리소스에 접근할 권한이 있는지 확인하는 인가(Authorize)이 기본 바탕입니다.

![screensh](./img/jwt.png)

## JWT란? (Json Web Token)
먼저 JWT는 JSON Web Token의 약자로 Json형태로 표현된 정보를 전달하는 하나의 방식으로, 토큰 자체에 모든 정보(토큰 기본정보, 전달할 정보, 검증됐다는 시그니쳐 정보 등)를 스스로 지니고 있다는 것이 큰 특징입니다. (자가 수용적, Self-Contained)
웹 서버의 경우 헤더나 파라미터를 통해 손쉽게 넘길 수 있어 인증이 필요한 REST 서비스에서 주로 활용됩니다.

## 구조
![screensh](./img/jwt구조.png)
- Header : 이 JWT가 어떤 방식으로, 어떤 알고리즘을 사용하여 토큰화 했는지 명시
- Payload : 토큰에 사용자가 담고자 하는 정보를 담는 곳
- Signature : 위 토큰이 유효한지 유효하지 않은지에 대한 정보를 가짐. 암호화에 사용되는 키 값은 서버에 저장해놓는다. 그리고 발행된 JWT 값이 서버에 들어왔을 때 두 값을 비교해서 올바른 JWT 토큰이 맞는지 확인한다.

### 과정

 1. 클라이언트가 인증 API를 통해 인증 요청
 2. 서버는 인증 진행 후 유효한 경우 토큰 발급 (JWT)
 3. 다음 요청 시 인증 토큰을 요청에 포함시켜 요청
 4. 서버는 요청에 포함된 인증 토큰을 해석해 권한 검사


## 내가 작성한 코드 및 설명

#### 스프링 시큐리티에서 UsernamePasswordAuthenticationFilter가 있다

 - /login을 요청해서 username, password 전송하면(post) UsernamePasswordAuthenticationFilter가 동작함(나의 프로젝트는 formlogin을 disable했기에 위에 필터가 작동하지 않는다)
   
 
   1. UsernamePasswordAuthenticationFilter를 작동시키기 위해서는 (JwtAuthenticationFilter)를 시큐리티필터에 등록해줘야한다.
        
   2. 등록 후 /login 요청을 하면 로그인 시도를 위해 UsernamePasswordAuthenticationFilter의 <strong>attemptAuthentication</strong> 함수가 실행된다.
          이후 username(email), password를 받아서 정상인지 로그인 시도를 해본다. 
        
   3. authenticationManager로 로그인 시도를 하면 CustomUserDetailsService의 loadUserByUsername 함수가 실행된다.
        
   4. authentication 객체가 sesstion 영역에 저장된다(로그인이 되었다는뜻). 이후 authentication객체를 리턴해주면 된다.(권환관리를 시큐리티가 대신 해주기때문에)
          굳이 jwt토큰을 사용하면서 세션을 만들 이유가 없다. 이유는 권한 처리떄문에 세션에 넣어준다.
          
         
            public class JwtAuthenticationFilter extends UsernamePasswordAuthenticationFilter {
                private final AuthenticationManager authenticationManager;
                //@Value("${jwttest.secret-key}")
                private String secret = "qkrqjatjs12345678910111231231232131232131231231231231231232131231231231245";
                /**
                * /login 요청오면 실행되는 함수
                */
                @Override
                public Authentication attemptAuthentication(HttpServletRequest request, HttpServletResponse response) throws AuthenticationException {
                    log.info("로그인시도중");
                    /**
                    * 1.useremail, password 받아서
                    * 2.정상인지 로그인시도 해봄. authenticationManager로 로그인시도를 하면 CustomUserDetailsService가 호출된다
                    * 3. securityUser를 세션에 담고
                    * 4. jwt 토큰을 만들어 응답
                    */
                    //1
                    try {
                        ObjectMapper objectMapper = new ObjectMapper();
                        User user = objectMapper.readValue(request.getInputStream(), User.class);
                        log.info("username={}", user.getName());
                        log.info("email={}", user.getEmail());
                        log.info("pass={}", user.getPassword());           
                        
                     UsernamePasswordAuthenticationToken newAuthentication = new UsernamePasswordAuthenticationToken(
                             user, user.getPassword());
                     UsernamePasswordAuthenticationToken authenticationToken = new UsernamePasswordAuthenticationToken(user.getEmail(), user.getPassword());
                     //  CustomUserDetailsService의 loadByUsername() 함수가 실행된다(나는 email로 호출한다)
                     Authentication authentication = authenticationManager.authenticate(authenticationToken);
                     // authentication 객체가 세션영역에 저장됨 => 로그인이 되었다는 뜻
                     SecurityUser securityUser = (SecurityUser) authentication.getPrincipal();
         
                     log.info("-----------로그인완료됨");
                     log.info("email={}", securityUser.getEmail());
                     return authentication;
         
                 } catch (IOException e) {
                     e.printStackTrace();
                 }
                 return null;
             }
          
          
 (로그인완료 후)<br>
            
 1. attemptAuthentication 실행 후 인증이 정상적으로 되었으면 successfulAuthentication 함수가 실행된다.
 2. JWT 토큰을 만들어서 request요청한 사용자에게 jwt토큰을 response해주면된다
 
        
        @Override
           protected void successfulAuthentication(HttpServletRequest request, HttpServletResponse response, FilterChain chain, Authentication authResult) throws IOException, ServletException {
               log.info("인증이완료되었습니다---- 토큰발급");
       
               SecurityUser user = (SecurityUser)authResult.getPrincipal();
               log.info("screct={}",secret);
               String jwtToken = Jwts.builder().setSubject("cos_token")
                       .setExpiration(new Date(System.currentTimeMillis()+(60000*10)))
                       .claim("id",user.getUser().getId())
                       .claim("email", user.getEmail())
                       .claim("name", user.getUsername())
                       .signWith(SignatureAlgorithm.HS256, secret.getBytes())
                       .compact();
               response.addHeader("Authorization", "Bearer "+jwtToken);
           }
           
           
  ------
  
#### 유저네임or email, 패스워드 로그인 정상
   - 서버쪽 - JWT토큰 생성 후 클라이언트쪽으로 JWT토큰 응답
   - 클라이언트쪽 - JWT토큰을 가지고 요청 
   - 서버는 JWT토큰이 유효한지를 판단(필터를 만들어야한다)
        
        

#### 시큐리티가 filter가지고 있는데 그 필터중에 BasicAuthenticatrionFilter라는 것이 있다.
  - 권한이나 인증이 필요한 특정 주소를 요청했을 위 필터를 무조건 타게되어있다
  - 만약 권한이나 인증이 필요한 주소가 아니라면 필터를 안탄다
  
  
  


             //인증이나 권한이 필요한 주소요청이 있을 때 해당 필터를 타게된다
       
           @Override
              protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain chain) throws IOException, ServletException {
                  String jwtHeader = request.getHeader("Authorization");
                  // 헤더가 있는지 확인
                  if( jwtHeader == null || !jwtHeader.startsWith("Bearer")){
                      chain.doFilter(request,response);
                      log.info("헤더가 없으면 필터 안타고 리턴");
                      return;
                  }
                  String jwtToken = jwtHeader.substring(7);
                  Claims claims = Jwts.parserBuilder()
                          .setSigningKey(secret.getBytes())
                          .build()
                          .parseClaimsJws(jwtToken)
                          .getBody();
                  if (claims.get("email",String.class) !=null){
                      log.info("토큰검증 통과");
                      User user = userRepository.findByEmail(claims.get("email", String.class)).orElseThrow(()->new IllegalArgumentException("찾는 이메일이 없습니다."));
                      SecurityUser securityUser = new SecurityUser(user);
                      //jwt토큰 서명을 통해 서명이 정상이면 Authentication객체를만들어준다
                      Authentication authentication = new UsernamePasswordAuthenticationToken(securityUser,null,securityUser.getAuthorities());
                      //강제로 시큐리티의 세션에 접근하여 Authentication 객체를 저장.
                      SecurityContextHolder.getContext().setAuthentication(authentication);
                      chain.doFilter(request,response);
                  }
              }



## 다른분 방식(보고 배워야겠다)
Spring Security와의 JWT 연동
Spring Security는 세션 방식으로 사용자의 인증/허가를 주로 이루고 있다.
따라서 우리는 기존 방식을 Custom 하여 Token 방식으로 구성해야 하다.

또한 스프링 Security는 사용자의 요청과 응답사이에 여러가지 기능을 수행하는 필터(Filter)를 두어 인증/허가 기능을 수행하고 있다.


- SecurityContextPersistenceFilter : SecurityContext(authentication객체) 객체를 로딩하여 SecurityContextHolder에 저장하고 요청이 끝나면 삭제

- UsernamePasswordAuthennticationFilter : /login 요청이 오면 동작하는 필터(formlogin을 사용하지 않을경우 UsernamePasswordAuthenticationFilter를 작동시키기 위해서는 (커스텀필터))를 시큐리티필터에 등록해줘야한다.)

- FilterSecurityInterceptor : 인증에 성공한 사용자가 해당 리소스에 접근할 권한이 있는지를 검증
우리가 사용할 부분은 
UsernamePasswordAuthenticationFilter 앞에 Custom Filter를 두어 세션이 존재하지 않아도 올바른 Jwt 값이 존재하면, SecurityContextHolder에 UserDetail 정보를 넣어 로그인 된 사용자로 인식 하도록 할 것이다.

출저 - https://velog.io/@ehdrms2034/Spring-Security-JWT-Redis%EB%A5%BC-%ED%86%B5%ED%95%9C-%ED%9A%8C%EC%9B%90%EC%9D%B8%EC%A6%9D%ED%97%88%EA%B0%80-%EA%B5%AC%ED%98%84