## Controller계층 단위테스트
아래는 회원 Controller부분이다.
    
    private final MemberService memberService;
    /*
     회원가입
     */
    @PostMapping("members/signup")
    public Long createMember(String name){
        return memberService.createMember(name);
    }

    /*
     유저상세조회
     */
    @GetMapping("members/{id}")
    public Member findById(@PathVariable Long id){
        return memberService.findById(id);
    }
    
    /*
    유저전체조회
     */
    @GetMapping("members")
    public List<Member> findAll(){
        return memberService.findAll();
    }
    
해당 Controller계층을 단위테스트 해보자!

### @WebMvcTest
- MVC를 위한 테스트   
- 웹상에서 요청과 응답에 대해 테스트할 수 있다.
- @SpringBootTest의 경우 모든 빈을 로드하기 때문에 테스트 구동 시간이 오래 걸리고, 테스트 단위가 크기 때문에 디버깅이 어려울 수 있다. Controller 레이어만 슬라이스 테스트 하고 싶을 때에는 @WebMvcTest를 쓰는게 유용하며 @SpringBootTest 어노테이션보다 가볍게 테스트할 수 있다.
- @Controller, @ControllerAdvice, @JsonComponent, Converter, GenericConverter, Filter, HandlerInterceptor  내용만 스캔하도록 제한된다.
- Service, Repository dependency가 필요한 경우에는 @MockBean으로 주입받아 테스트를 진행 한다.

특정 Controller를 지정하여 스캔한다.

    @WebMvcTest(MemberController.class)

### MockMvc

실제 객체와 비슷하지만 테스트에 필요한 기능만 가지는 가짜 객체를 만들어서 애플리케이션 서버에 배포하지 않고도 스프링 MVC 동작을 테스트 할 수 있게 해준다.

      @Autowired
      private MockMvc mockMvc;

MockMvc를 사용한 GET, POST 테스트

    //get
    mockMvc.perform(get("/api/members/1"))
                  .andExpect(status().isOk())
                  .andExpect(content().contentTypeCompatibleWith(MediaType.APPLICATION_JSON))
                  .andExpect(jsonPath("$.name").value("홍길동"));
                  
                  
    //post
    mockMvc.perform(post("/api/members/signup"))
                .andExpect(status().isOk());


### @MockBean

@MockBean은 스프링 컨텍스트에 mock객체를 등록하게 되고 스프링 컨텍스트에 의해 @Autowired가 동작할 때 등록된 mock객체를 사용할 수 있도록 동작합니다.

      @MockBean
      private MemberService memberService;
 
 @MockBean으로 Mock객체를 스프링 컨텍스트에 등록한다. spring container가 필요하고 Bean이 container 존재해야한다면 @MockBean을 사용한다.
 
아래는 테스트 코드이다.

      @WebMvcTest(MemberController.class)
      class MemberControllerTest {
          private static final String MEMBER_NAME = "홍길동";
          private static final Long MEMBER_ID = 1L;
          @Autowired
          private MockMvc mockMvc;

          @MockBean
          private MemberService memberService;

          @DisplayName("회원가입")
          @Test
          void 회원가입() throws Exception {
              given(memberService.createMember(MEMBER_NAME)).willReturn(MEMBER_ID);
              //when
              mockMvc.perform(post("/api/members/signup"))
                      .andExpect(status().isOk());
          }

          @DisplayName("회원상세조회")
          @Test
          void 회원상세조회() throws Exception {
              Member member = Member.builder().id(MEMBER_ID).name(MEMBER_NAME).build();
              given(memberService.findById(MEMBER_ID)).willReturn(member);
              //when
              mockMvc.perform(get("/api/members/1"))
                      .andExpect(status().isOk())
                      .andExpect(content().contentTypeCompatibleWith(MediaType.APPLICATION_JSON))
                      .andExpect(jsonPath("$.name").value("홍길동"));
          }

          @DisplayName("모든회원조회")
          @Test
          void 모든회원조회() throws Exception {
              List<Member> members = List.of(Member.builder().id(1L).name("김길동").build()
                      , Member.builder().id(2L).name("이길동").build()
                      , Member.builder().id(3L).name("박길동").build()
                      , Member.builder().id(4L).name("홍길동").build());
              given(memberService.findAll()).willReturn(members);
              //when
              mockMvc.perform(get("/api/members"))
                      .andExpect(status().isOk())
                      .andExpect(content().contentTypeCompatibleWith(MediaType.APPLICATION_JSON))
                      .andExpect(jsonPath("$.[0].name").value("김길동"))
                      .andExpect(jsonPath("$.[1].name").value("이길동"));
          }
      }
 
