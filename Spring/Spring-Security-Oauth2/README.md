
## Spring Security

- 막강한 인증, 인가 기능을 가진 프레임워크
- 필터 기반의 보안 기능을 구현하는 것보다 스프링 시큐리티를 통해 구현하는 것을 적극적으로 권하고 있습니다.
 

## OAuth

- 인터넷 사용자들이 비밀번호 제공하지 않고 다른 웹 사이트 상의 자신들의 정보에 대해 웹 사이트나 애플리케이션의 접근 권한을 부여할 수 있는 공통적인 수단.
  - ex: 네이버 아이디로 로그인, 구글 아이디로 로그인 등


이제 스프링 부트에 적용해보자


클라이언트 ID와 클라이언트 보안 비밀코드를 프로젝트에 설정
application-oauth.yml에 등록


        security:
            oauth2:
              client:
                registration:
                  google:
                    client-id: 클라이언트 id
                    client-secret: 시크릿 키
                    scope:
                      - email
                      - profile
                      
  
        profile,email를 등록한 이유는 openid라는 scope가 있으면 Open id Provider로 인식한다...
        이러면 Open id Provider인 서비스(구글)와 그렇지 않은 서비스로 나눠서 각각 OAuth2Service를 만들어야 합니다.
        하나의 OAuth2Service로 사용하기 위해 일부러 openid scope를 빼고 등록합니다.




또한 Spring Security에서는 권한 코드에 항상 ROLE_xxx 형식이어야 한다.

        @Getter
        public enum Role {
            ROLE_USER, ROLSE_ADMIN
        }
        
        
        
## 스프링 시큐리티 설정     
먼저 build.gradle에 스프링 시큐리티 관련 의존성 하나를 추가합니다.

    build.gradle
    compile('org.springframework.boot:spring-boot-starter-oauth2-client')


- spring-boot-starter-oauth2-client
 - 소셜 로그인 등 클라이언트 입장에서 소셜 기능 구현 시 필요한 의존성
 - spring-boot-starter-oauth2-client와 spring-security-oauth2-jose를 기본으로 관리해줍니다.


build.gradle 설정이 끝났으면 OAuth 라이브러리를 이용한 소셜 로그인 설정 코드를 작성합니다.

##### SecurityConfig.java 클래스 생성

      
    public class SecurityConfig extends WebSecurityConfigurerAdapter {
    private final CustomOauth2UserService customOauth2UserService;

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
                .csrf().disable()
                .headers().frameOptions().disable()
                .and()
                    .authorizeRequests()
                    .antMatchers("/", "/h2-consloe/**").permitAll()
                    .antMatchers("/member/**").hasRole("USER")
                    .anyRequest().authenticated()
                .and()
                    .formLogin().permitAll()
                        .loginPage("/loginForm")
                            .loginProcessingUrl("/login") //login 주소가 호출되면 시큐리티가 낚아채서 대신 로그인 진행
                .and()
                    .oauth2Login().permitAll()
                        .loginPage("/loginForm")
                            .userInfoEndpoint()
                                .userService(customOauth2UserService);
    }


@EnableWebSecurity
- Spring Security 설정들을 활성화시켜 줍니다.

authorizeRequests
 - URL별 권한 관리를 설정하는 옵션의 시작점입니다.
 - authorizeRequests가 선언되어야만 antMatchers 옵션을 사용할 수 있습니다.

antMatchers
 - 권한 관리 대상을 지정하는 옵션입니다.
 - URL, HTTP 메소드별로 관리가 가능합니다.
 - "/"등 지정된 URL들은 permitAll() 옵션을 통해 전체 열람 권한을 주었습니다.
 - "/member/**"주소를 ROLE_USER 권한을 가진 사람만 가능하도록 했습니다.

anyRequest
 - 설정된 값들 이외 나머지 URL들을 나타냅니다.
 - 여기서는 authenticated()을 추가하여 나머지 URL들은 모두 인증된 사용자들에게만 허용하게 됩니다.
 - 인증된 사용자 즉, 로그인한 사용자들은 이야기합니다.

logout().logoutSuccessUrl("/")
  - 로그아웃 기능에 대한 여러 설정의 진입점입니다.
  - 로그아웃 성공 시 / 주소로 이동합니다.

oauth2Login
  - OAuth 2 로그인 기능에 대한 여러 설정의 진입점입니다.
  - userInfoEndpoint
  - OAuth 2 로그인 성공 이후 사용자 정보를 가져올 때의 설정들을 담당합니다.

userService
  - 소셜 로그인 성공 시 후속 조치를 진행할 UserService 인터페이스의 구현체를 등록합니다.
  - 리소스 서버(즉, 소셜 서비스들)에서 사용자 정보를 가져온 상태에서 추가로 진행하고자 하는 기능을 명시할 수 있습니다.


##### CustomOAuth2UserService클래스를 생성 합니다
- 이 클래스에서는 구글 로그인 이후 가져온 사용자의 정보(email,name,picture등) 들을 기반으로 가입 및 정보수정, 세션 저장 등의 기능을 지원합니다.


      @RequiredArgsConstructor
      @Service
      public class CustomOauth2UserService implements OAuth2UserService<OAuth2UserRequest, OAuth2User> {
          private final MemberRepository memberRepository;
          private final HttpSession httpSession;

          @Override
          public OAuth2User loadUser(OAuth2UserRequest userRequest) throws OAuth2AuthenticationException {
              OAuth2UserService delegate = new DefaultOAuth2UserService();
              OAuth2User oAuth2User = delegate.loadUser(userRequest);
              // 현재 로그인 진행 중인 서비스를 구분하는 코드
              /**
               * registrationId
               * 현재 로그인 진행 중인 서비스 구분하는 코드.
               * 이후에 여러가지 추가할 때 네이버인지 구글인지 구분
              */
              String registrationId = userRequest.getClientRegistration().getRegistrationId();
              // oauth2 로그인 진행 시 키가 되는 필드값
              /**
               *OAuth2 로그인 진행 시 키가 되는 필드값 (=Primary Key)
               * 구글 기본 코드: sub, 네이버 카카오 등은 기본 지원 x
               * 이후 네이버, 구글 로그인 동시 지원시 사용
               */
              String userNameAttributeName = userRequest.getClientRegistration()
                      .getProviderDetails().getUserInfoEndpoint().getUserNameAttributeName();
              // OAuthAttributes: attribute를 담을 클래스 (개발자가 생성)
              /**
               * OAuthAttributes
               * OAuth2UserService를 통해 가져온 OAuth2User의 attribute
               * 네이버 등 다른 소셜 로그인도 이 클래스 사용
              */
              OAuthAttributes attributes = OAuthAttributes.
                      of(registrationId, userNameAttributeName, oAuth2User.getAttributes());

              Member member = saveOrUpdate(attributes);
              httpSession.setAttribute("member", new SesstionUser(member));
              return new DefaultOAuth2User(
                      Collections.singleton(new SimpleGrantedAuthority("ROLE_USER")),
                      attributes.getAttributes(),
                      attributes.getNameAttributeKey()
              );
          }

          private Member saveOrUpdate(OAuthAttributes attributes) {
              Member member = memberRepository.findByEmail(attributes.getEmail())
                      .map(entity-> entity.update(attributes.getName())
                      )
                      .orElse(attributes.toEntity());
              attributes.toEntity();

              return memberRepository.save(member);
          }
          
          
          
registrationId
 - 현재 로그인 진행 중인 서비스를 구분하는 코드입니다.
 - 지금은 구글만 사용하는 불필요한 값이지만, 이후 네이버 로그인 연동시에 네이버 로그인인지, 구글 로그인인지 구분하기 위해 사용합니다.

userNameAttributeName
 - OAuth2 로그인 진행 시 키가 되는 필드값을 이야기합니다. Primary Key와 같은 의미입니다.
 - 구글의 경우 기본적으로 코드를 지원하지만, 네이버 카카오 등은 기본 지원하지 않습니다. 구글의 기본 코드는 "sub"입니다.


OAuthAttributes
 - OAuth2UserService를 통해 가져온 OAuth2User의 attribute를 담을 클래스입니다.
 - 이후 네이버 등 다른 소셜 로그인도 이 클래스 사용합니다.
 
SessionUser
 - 세션에 사용자 정보를 저장하기 위한 Dto 클래스입니다.




##### OAuthAttributes



        @Getter
        public class OAuthAttributes {
            private Map<String, Object> attributes;
            private String nameAttributeKey;
            private String name;
            private String email;
            private String picture;


            @Builder
            public OAuthAttributes(Map<String, Object> attributes,
                                   String nameAttributeKey,
                                   String name, String email, String picture) {
                this.attributes = attributes;
                this.nameAttributeKey = nameAttributeKey;
                this.name = name;
                this.email = email;
                this.picture = picture;
            }
            public static OAuthAttributes of(String registrationId,
                                             String userNameAttributeName,
                                             Map<String, Object> attributes) {
                return ofGoogle(userNameAttributeName, attributes);
            }

            private static OAuthAttributes ofGoogle(String userNameAttributeName,
                                                    Map<String, Object> attributes) {
                return OAuthAttributes.builder()
                        .name((String) attributes.get("name"))
                        .email((String) attributes.get("email"))
                        .attributes(attributes)
                        .nameAttributeKey(userNameAttributeName)
                        .build();
            }

            /**
             * toEntity()
             * User 엔티티 생성
             * OAuthAttributes에서 엔티티 생성 시점 = 처음 가입 시
             * OAuthAttributes 클래스 생성이 끝났으면 같은 패키지에 SessionUser 클래스 생성
             * @return
             */
            public Member toEntity() {
                return Member.builder()
                        .name(name)
                        .email(email)
                        .role(Role.ROLE_USER)
                        .build();
            }
       
       
##### SesstionUser


      @Getter
      public class SesstionUser implements Serializable {
          private String name;
          private String email;
          private String picture;

          public SesstionUser(Member member){
              this.name = member.getName();
              this.email = member.getEmail();
              this.picture = member.getName();
          }
      }            
      
SessionUser에는 인증된 사용자 정보만 필요합니다.

@Entity User 클래스를 SessionUser로 사용안하는 이유

세션에 저장하기 위해 User클래스를 세션에 저장하려고 하니 User 클래스에 직렬화를 구현하지 않았다는
에러가 난다.

Entity 클래스는 직렬화 코드를 넣지 않는게 좋다
엔티티 클래스에는 언제 다른 엔티티와 관계가 형성될지 모른다.
@OneToMany, @ManyToMany등 자식 엔티티를 갖고 있다면 직렬화 대상에 자식들까지 포함되니 성능 이슈, 부수 효과가 발생할 확률이 높다
그래서 직렬화 기능을 가진 세션 Dto를 하나 추가로 만든 것이 더 좋은 방법이다.






##### 세션 정장소로 데이터베이스 사용하기
세션 저장소에 대해 3가지 중 한 가지를 선택합니다.

1. 톰캣 세션을 사용한다.
 - 일반적으로 별다른 설정을 하지 않을 때 기본적으로 선택되는 방식
 이렇게 될 경우 톰캣(WAS)에 세션이 저장되기 때문에 2대 이상의 WAS가 구동되는 환경에서는 톰캣들 간의 세션 공유를 위한 추가 설정이 필요하다.

2. MySQL과 같은 데이터베이스를 세션 저장소로 사용한다.
 - 여러 WAS 간의 공용 세션을 사용할 수 있는 가장 쉬운 방법
 - 많은 설정이 필용 없다,하지만 결국 로그인 요청마다 DB IO가 발생하여 성능상 이슈가 발생할 수 있습니다.
 - 보통 로그인 요청이 많이 없는 백오피스, 사내 시스템 용도에서 사용

3. Redis, Memcached와 같은 메모리 DB를 세션 저장소로 사용한다.
 - B2C 서비스에서 가장 많이 사용하는 방식입니다.
 - 실제 서비스로 사용하기 위해서는 Embedded Redis와 같은 방식이 아닌 외부 메모리 서버가 필요

2번을 사용하겠다.

spring-session-jdbc 등록


      -build.gradle
      compile('org.springframework.session:spring-session-jdbc')
      
      -application.yml
      spring.session.store-type=jdbc
