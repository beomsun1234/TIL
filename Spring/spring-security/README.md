### Spring Security

   	    Spring Security is a framework that provides authentication, authorization, and protection
        against common attacks. With first class support for both imperative and reactive    
        applications, it is the de-facto standard for securing Spring-based applications.
    
		구글 번역하면 "Spring Security는 일반적인 공격에 대한 인증, 권한 부여 및 보호를 제공하는 프레임워크입니다."
        -Spring Security Reference

즉 Spring Security는 Spring 기반의 애플리케이션의 보안(인증과 권한, 인가 등)을 담당하는 스프링 하위 프레임워크이다. Spring Security는 '인증'과 '권한'에 대한 부분을 Filter 흐름에 따라 처리하고 있다. Filter는 Dispatcher Servlet으로 가기 전에 적용되므로 가장 먼저 URL 요청을 받지만, Interceptor는 Dispatcher와 Controller사이에 위치한다는 점에서 적용 시기의 차이가 있다. Spring Security는 보안과 관련해서 체계적으로 많은 옵션을 제공해주기 때문에 개발자 입장에서는 일일이 보안관련 로직을 작성하지 않아도 된다는 장점이 있다.



웹 보안은 기본적으로 요청하는 사용자를 식별하는 인증(Authenticate)과 인증된 사용자가 보호된 리소스에 접근할 권한이 있는지 확인하는 인가(Authorize)이 기본 바탕입니다.

### 용어(인증, 인가, 권한)
  
 - 인증(Authentication)
  
   		- 보호된 리소스에 접근한 대상에 대해 이 유저가 누구인지, 애플리케이션의 작업을 수행해도 되는
        주체인지 확인하는 과정
        
        -> 해당 사용자가 본인이 맞는지를 확인하는 절차(접근 주체가 누구인지 식별하는 과정)

- 인가
 
		- 해당 리소스에 대해 접근 가능한 권한을 가지고 있는지 확인하는 과정
        
        - 인증을 통해 확인한 사용자가 보유한 권한(Roles)을 확인해 요청한 서비스(API)를 수행할 권한이 있는지 확인하는 과정
        
        ->현재 사용자가 보호된 리소스에 대해 권한이 있는지 검사
       

- 권한

		- 인증된 접근 주체가 요청한 서비스를 수행할 자격이 있음을 증명하는 것


------
Spring Security는 기본적으로 인증 절차를 거친 후에 인가 절차를 진행하게 되며, 인가 과젱에서 해당 리소스에 대한 접근 권한이 있는지 확인을 하게 된다. Spring Security에서는 이러한 인증과 인가를 위해 Principal을 아이디로, Credential을 비밀번호로 사용하는 Credential 기반의 인증 방식을 사용한다. 

Principal(접근 주체): 보호받는 Resource에 접근하는 대상

Credential(비밀번호): Resource에 접근하는 대상의 비밀번호

출저 [https://mangkyu.tistory.com/76]
 
----

### Spring Security 처리 과정


1. 로그인 요청 
	
    - 자는 로그인 하기 위해 아이디와 비밀번호를 입력해서 로그인 요청을 하게 된다.(사용자 인증 요청)


2. UserPasswordAuthenticationToken 발급
	- UsernamePasswordAuthenticationToken은 Authentication을 implements한 AbstractAuthenticationToken의 하위 클래스로, User의 ID가 Principal 역할을 하고, Password가 Credential의 역할을 한다. UsernamePasswordAuthenticationToken의 첫 번째 생성자는 인증 전의 객체를 생성하고, 두번째 생성자는 인증이 완려된 객체를 생성한다.

  	- AuthenticationFilter(사용할 구현체 UsernamePasswordAuthenticationFilter)가 HttpServletRequest에서 사용자가 보낸 아이디와 패스워드를 인터셉트한다. 프론트 단에서 유효성검사를 할 수도 있지만, 무엇보다 안전! 안전을 위해서 다시 한번 사용자가 보낸 아이디와 패스워드의 유효성 검사를 해줄 수 있다.(아이디 혹은 패스워드가 null인 경우 등) HttpServletRequest에서 꺼내온 사용자 아이디와 패스워드를 진짜 인증을 담당할 AuthenticationManager 인터페이스(구현체 - ProviderManager)에게 인증용 객체(UsernamePasswordAuthenticationToken)로 만들어줘서 위임한다.



3. UsernamePasswordToken을 Authentication Manager에게 전달

	- AuthenticationFilter는 생성한 UsernamePasswordToken을 AuthenticationManager에게 전달한다. AuthenticationManager은 실제로 인증을 처리할 여러개의 AuthenticationProvider를 가지고 있다.


4. UsernamePasswordToken을 Authentication Provider에게 전달

	- AuthenticationManager는 전달받은 UsernamePasswordToken을 순차적으로 AuthenticaionProvider들에게 전달하여 실제 인증의 과정을 수행해야 하며, 실제 인증에 대한 부분은 authenticate 함수에 작성을 해주어야 한다. SpringSecurity에서는 Username으로 DB에서 데이터를 조회한 다음에, 비밀번호의 일치 여부를 검사하는 방식으로 작동을 한다. 그렇기 때문에 먼저 UsernamePasswordToken 토큰으로부터 아이디를 조회해야한다.


5. UserDetailsService로 조회할 (id OR email)를 전달
 
	- AuthenticationProvider에서 아이디를 조회하였으면, UserDetailsService로부터 아이디를 기반으로 데이터를 조회해야 한다. UserDetailsService는 인터페이스이기 때문에 이를 implements한 클래스를 작성해주어야 한다. 


6. 아이디를 기반으로 DB에서 데이터 조회 

     - UserDetailService가 id나 email을 조회 하여 UserDetail타입으로 AuthenticationProvider에 반환


7.  AuthenticationProvider는 UserDetails를 넘겨받고 사용자 정보를 비교


8. 인증이 완료되면 권한 등의 사용자 정보를 담은 Authentication 객체를 반환합니다.


9 10. 인증이 완료되면 사용자 정보를 가진 Authentication 객체를 SecurityContextHolder에 담은 이후 AuthenticationSuccessHandle를 실행한다.(실패시 AuthenticationFailureHandler를 실행한다.)



#### 최종적으로 SecurityContextHolder는 세션 영역에 있는 SecurityContext에 Authentication 객체를 저장합니다. 세션에 사용자정보를 저장한다는 것은 스프링 시큐리티가 전통적인 세션-쿠키 기반의 인증 방식을 사용한다는 것을 의미합니다.

<br>



### Spring Security 모듈


- SecurityContextHolder

  	 	- Security Context 제공, 기본적으로 ThreadLocal을 사용한다. 
        - 기본 전략은 ThreadLocal 기반으로 동작한다. 
        - SecurityContextHolder를 통해 SecurityContext에 접근할 수 있다.
        
        
-  SecurityContext 

		- Authentication을 보관하는 역할을 하며, SecurityContext를 통해 Authentication 객체를 꺼내올 수 있다.
		- Authentication을 제공한다.
	
   
    
- Authentication

		- Spring Security에서 인증을 거치고난 뒤의 사용자의 인증정보를 Principal 이라하며
		이러한 Principal을 감싸고 있는 객체이다.
		- Printcipal 외에도 GrantedAuthorities (사용자 권한 정보) 등 다양한 정보를 가지고 있다.
		- SecurityContext 를 통해 Authentication 객체를 받아올 수 있다.

- GrantedAuthorities

		- ROLE_USER, ROLE_ADMIN 등 Principal이 가지고 있는 권한을 나타낸다.
		- 인증 이후 인가 및 권한을 확인할때 참조한다.


- ThreadLocal
 
	    - ThreadLocal은 같은 Thread 내에서 공유하는 저장소이다.
		- Parameter를 넘기지 않아도, 쓰레드 내에서 데이터를 공유 및 전달이 가능하다.
		

#### ```인증된 사용자 정보인 Principal을 Authentication에서 관리하고 Authentication을 SecurityContext 관리하고 SecurityContext SecurityContextHolder가 관리한다.```


- UsernamePasswordAuthenticationToken

		- Authentication을 implements한 AbstractAuthenticationToken의 하위 클래스로 username이
	  Principal의 역할을 하고, password가 Credential의 역할을 합니다.
       - 첫번째 생성자는 인증 전의 객체를 생성하고, 두번째 생성자는 인증이 완료된 객체를 생성해줍니다.

- AuthenticationProvider

	    - 실제 인증에 대한 부분을 처리하는데, 인증 전의 Authentication 객체를 받아서 인증이 완료된 객체를 반환하는 역할을 합니다.


- AuthenticationManager

		- 인증에 대한 부분은 AuthenticationManager를 통해서 처리하게 되는데, 실질적으로는 AuthenticationManager에 등록된 AuthenticationProvider에 의해 처리됩니다.

		- 인증이 성공하면 isAuthenticated=true 인 객체를 생성하여 SecurityContext에 저장합니다.

		- 실패할 경우에는 AuthenticationException을 발생시킵니다.

		- DaoAuthenticationProvider는 AbstractUserDetailsAuthenticationProvider를 상속받아 실제 인증 과정에 대한 로직을 처리합니다.

		- AuthenticationManager에 DaoAuthenticationProvider를 등록하는 방법은 WebSecurityConfigurerAdapter를 상속해 만든 ApplicationSecurityConfig에서 할수 있습니다.

- UserDetails

		- 인증에 성공하여 생성된 UserDetails 객체는 UsernamePasswordAuthenticationToken을 생성하기 위해 사용됩니다.
		
		- UserDetails 인터페이스의 경우 직접 개발한 ApplicationUser에 UserDetails를 implements하여 사용하면 됩니다
		

- UserDetailsService

		- UserDetails 객체를 반환하는 단 하나의 메소드를 가지고 있는데, 일반적으로 이를 구현한 클래스의 내부에 UserRepository를 주입받아 DB에 연결하여 처리합니다.

----
### Spring Security Filter

- SecurityContextPersistentFilter 

   	    SecurityContextRepository에서 SecurityContext를 가져와서 SecurityContextHolder에 주입하거나 반대로 저장하는 역할을 합니다.
    
- LogoutFilter 

   	    logout 요청을 감시하며, 요청시 인증 주체(Principal)를 로그아웃 시킵니다.
      
      
- UsernamePasswordAuthenticationFilter 

	    login 요청을 감시하며, 인증 과정을 진행합니다.
     
     
- DefaultLoginPageGenerationFilter

	    사용자가 별도의 로그인 페이지를 구현하지 않은 경우, 스프링에서 기본적으로 설정한 로그인 페이지로 넘어가게 합니다.
        
        
- BasicAuthenticationFilter 
 
	    HTTP 요청의 (BASIC)인증 헤더를 처리하여 결과를 SecurityContextHolder에 저장합니다.
      
      
- RememberMeAuthenticationFilter 

 	    SecurityContext에 인증(Authentication) 객체가 있는지 확인하고 RememberMeServices를 구현한 객체 요청이 있을 경우, RememberMe를 인증 토큰으로 컨텍스트에 주입합니다.
      
- AnonymousAuthenticationFilter : 

	    이 필터가 호출되는 시점까지 사용자 정보가 인증되지 않았다면 익명 사용자로 취급합니다.

- SessionManagementFilter

 	    요청이 시작된 이후 인증된 사용자인지 확인하고, 인증된 사용자일 경우 SessionAuthenticationStrategy를 호출하여 세션 고정 보호 매커니즘을 활성화 하거나 여러 동시 로그인을 확인하는 것과 같은 세션 관련 활동을 수행합니다.
 
- ExceptionTranslationFilter

        필터체인 내에서 발생되는 모든 예외를 처리합니다.
 
- FilterSecurityInterceptor 
  
  	    AccessDecisionManager로 권한부여처리를 위임하고 HTTP 리소스의 보안 처리를 수행합니다.