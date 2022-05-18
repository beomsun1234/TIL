## 단위테스트
단위 테스트란? 애플리케이션을 구성하는 하나의 기능이 올바르게 동작하는지를 독립적으로 테스트하는 것으로, "어떤 기능이 실행되면 어떤 결과가 나온다" 정도로 테스트를 진행한다.

## Service 계층 단위테스트

[전에 팀 프로젝트를 진행할 때 작성한 코드 중 회원에 대한 비지니스로직을 바탕으로 작성했습니다.](https://github.com/beomsun1234/ohou-backend) MemberService에는 회원 가입, 조회, 정보 변경
등의 로직으로 구성되어 있습니다.

          
          private final ImageUtil imageUtil;
          private final MemberRepository memberRepository;
          private final BCryptPasswordEncoder bCryptPasswordEncoder;
          /**
           * 회원가입
           * @param memberJoinRequestDto
           * @return
           */
          @Transactional
          public ApiCommonResponse join(MemberJoinRequestDto memberJoinRequestDto){
              validateEmail(memberJoinRequestDto.getEmail());
              return ApiCommonResponse.builder()
                      .message("회원가입 성공")
                      .status(String.valueOf(HttpStatus.OK.value()))
                      .data(memberRepository.save(memberJoinRequestDto.toEntity(bCryptPasswordEncoder.encode(memberJoinRequestDto.getPassword()))).getId())
                      .build();
          }
          /**
           * 유저정보보
           * @param memberId
           * @return
           */
          @Cacheable(value = "member", key = "#memberId", unless = "#result == null ")
          @Transactional(readOnly = true)
          public MemberInfo getUserInfoById(Long memberId){
              MemberInfo memberInfo = MemberInfo.builder()
                      .entity(memberRepository.findById(memberId).orElseThrow(() -> new IllegalArgumentException("존재하지 않는 회원입니다")))
                      .build();
              return memberInfo;
          }
          /**
           * 유저정보 변경 및 프로필 업로드
           * @param userId
           * @param memberUpdateRequestDto
           * @return
           * @throws IOException
           */
          @CachePut(value = "member", key = "#userId", unless = "#result == null ")
          @Transactional
          public MemberInfo updateInfo(Long userId, MemberUpdateInfoRequestDto memberUpdateRequestDto) throws IOException {
              Member member = memberRepository.findById(userId).orElseThrow(() -> new IllegalArgumentException("해당 유저는 존재하지않습니다"));
              if (memberUpdateRequestDto.getProfileImage()==null){
                  return MemberInfo.builder().entity(memberRepository
                          .save(member.updateMyInfo(memberUpdateRequestDto.getNickname(), memberUpdateRequestDto.getGender(), null, memberUpdateRequestDto.getIntroduce())))
                          .build();
              }
              if(!imageUtil.checkContentType(memberUpdateRequestDto.getProfileImage().getContentType())){
                  throw new IOException("잘못된 컨텐츠입니다.");
              }
              String imagePath = imageUtil.generateImagePath(member.getId().toString(), memberUpdateRequestDto.getProfileImage());
              return MemberInfo.builder().entity(memberRepository
                      .save(member.updateMyInfo(memberUpdateRequestDto.getNickname(), memberUpdateRequestDto.getGender(), imagePath, memberUpdateRequestDto.getIntroduce())))
                      .build();
          }

          /**
           * 패스워드 변경
           * @param userId
           * @param memberUpdatePasswordDto
           * @return
           */

          @Transactional
          public ApiCommonResponse updatePassword(Long userId, MemberUpdatePasswordDto memberUpdatePasswordDto){
              validatePassword(memberUpdatePasswordDto.getPassword(),memberUpdatePasswordDto.getCheckPassword());
              String password = bCryptPasswordEncoder.encode(memberUpdatePasswordDto.getPassword());
              Member member = memberRepository.findById(userId).orElseThrow(() -> new IllegalArgumentException("존재하지 않는 사용자입니다."));
              return ApiCommonResponse.builder()
                      .message("패스워드 변경 성공")
                      .status(String.valueOf(HttpStatus.OK.value()))
                      .data(memberRepository.save(member.updatePassword(password)).getId())
                      .build();
          }



아래는 테스트 코드이다.

      @ExtendWith(MockitoExtension.class)
      class MemberServiceTest {
          
          @Mock
          private ImageUtil imageUtil;
          @Mock
          private MemberRepository memberRepository;
          @Mock
          private BCryptPasswordEncoder bCryptPasswordEncoder;
          
          @InjectMocks
          private MemberService memberService;

          @Test
          @DisplayName("회원가입 테스트")
          void test_join(){
              //given
              MemberJoinRequestDto memberJoinRequestDto = MemberJoinRequestDto.builder().nickname("test").password("1234").email("test").build();
              Member member = memberJoinRequestDto.toEntity(bCryptPasswordEncoder.encode(memberJoinRequestDto.getPassword()));
              given(memberRepository.save(any(Member.class))).willReturn(member);
              //when
              ApiCommonResponse join = memberService.join(memberJoinRequestDto);
              //then
              Assertions.assertThat(join.getStatus()).isEqualTo("200");
          }

          @Test
          @DisplayName("유저 id 조회")
          void test_getUserInfoById(){
              //given
              Long memberFakeId = 1L;
              Member member = Member.builder().id(memberFakeId).name("test").email("test").build();
              given(memberRepository.findById(memberFakeId)).willReturn(java.util.Optional.ofNullable(member));
              //when
              MemberInfo memberInfo = memberService.getUserInfoById(memberFakeId);
              //then
              Assertions.assertThat(memberInfo.getEmail()).isEqualTo("test");
          }

          @Test
          @DisplayName("유저정보 변경 및 프로필 업로드")
          void test_updateInfo() throws IOException {
              //given
              Long memberFakeId = 1L;
              Member member = Member.builder().id(memberFakeId).name("test").email("test").build();
              MemberUpdateInfoRequestDto memberUpdateDto = MemberUpdateInfoRequestDto.builder().gender(Gender.MAN).nickname("update").build();
              given(memberRepository.findById(memberFakeId)).willReturn(java.util.Optional.ofNullable(member));
              //when
              when(memberRepository.save(Objects.requireNonNull(member).updateMyInfo(memberUpdateDto.getNickname(),memberUpdateDto.getGender(),null,memberUpdateDto.getIntroduce())))
                      .thenReturn(member);
              MemberInfo memberInfo = memberService.updateInfo(memberFakeId, memberUpdateDto);
              //then
              Assertions.assertThat(memberInfo.getNickname()).isEqualTo("update");
          }

          @Test
          @DisplayName("유저 패스워드 변경")
          void test_updatePassword(){
              //given
              Long memberFakeId = 1L;
              Member member = Member.builder().id(memberFakeId).name("test").email("test").password(bCryptPasswordEncoder.encode("1234")).build();
              MemberUpdatePasswordDto passwordDto = MemberUpdatePasswordDto.builder().checkPassword("12345").password("12345").build();
              String updatePassword = bCryptPasswordEncoder.encode(passwordDto.getPassword());
              given(memberRepository.findById(memberFakeId)).willReturn(java.util.Optional.ofNullable(member));
              //when
              when(memberRepository.save(Objects.requireNonNull(member).updatePassword(updatePassword))).thenReturn(member);
              ApiCommonResponse password = memberService.updatePassword(memberFakeId, passwordDto);
              //then
              Assertions.assertThat(password.getData()).isEqualTo(1L);
          }

}

### Mock

실제 사용하는 모듈을 사용하지 않고 실제의 모듈을 "흉내"내는 "가짜" 모듈을 작성하여 테스트의 효용성을 높이는 데 사용하는 객체이다.

@Mock은 @InjectMocks에 대해서만 해당 클래스안에서 정의된 객체를 찾아서 의존성을 해결합니다.

### @InjectMocks

@InjectMocks 라는 어노테이션을 사용한다면 해당 클래스가 필요한 의존성과 맞는 Mock 객체들을 감지하여 해당 클래스의 객체가 만들어질때 사용하여 객체를 만들고 해당 변수에 객체를 주입하게 됩니다. 내 코드에선 MemberService에 @InjectMocks로 @Mock에서 만들어진 객체들을 사용해여 MemberService를 생성한다.

### @Mockito

mock을 쉽게 만들고 mock의 행동을 정하는 stubbing, 정상적으로 작동하는지에 대한 verify 등 다양한 기능을 제공해주는 프레임워크입니다.

## 트러블슈팅

MemberService는 3개의 객체와 의존관계를 맺고있는데  @Mock이라는 어노테이션을 알기 전 까지 어떤 방식으로 의존성을 주입해서 MemberService만 테스트를 하는지 잘 몰랐다. @Mock은  통해 어떠한 객체로든 변신이 가능한 객체를 만들어준다.
@Mock를 의존관계를 맺고있는 객체들에게 어노테이션을 추가해서 가짜 객체를 만들어 의존성을 주입해서 단위테스트를 진행할 수 있다.



