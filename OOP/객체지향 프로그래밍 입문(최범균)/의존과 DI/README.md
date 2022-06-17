# 의존과 DI

## 의존

- 기능 구현을 위해 다른 구성 요소를 사용하는 것
  - 의존의 예: 객체 생성, 메서드 호출, 데이터 사용

- 의존은 변경이 전파될 가능성을 의미
  - 의존하는 대상이 바뀌면 바뀔 가능성이 높아짐
    - ex) 호출하는 메서드의 파라미터가 변경
    - ex) 호출하는 메서드가 발생할 수 있는 익셉션 타입이 추가

### 순환 의존

순환의존은 아래 그림과 같은 관계이다.

    A --→ B --→ C
    ↑           ↓
    ←------------

A가 B에 의존하고 B는 C 그리고 C는 다시 A에 의존하고 있다. 만약 A에 변경이 일어났다면, B에 영향을 주고 이어서 C에 영향을 주고 다시 A에 영향을 줄 수 있다.

즉 변경이 연쇄 전파 가능성 존재함으로 클래스, 패키지, 모듈 등 모든 수준에서 순환 의존이 없도록 해야한다.


### 의존하는 대상이 많다면?



             
    A ←--|           |--→ D 
    B ←--| ←-- X --→ |--→ E
    C ←--|           |--→ F
    

  
위 코드를 보면 X는 A,B,C,D,E,F를 의존하고 있어 A ~ F중에 변경이 발생하면 A는 해당 변경에 영향을 받을 수 있기에 의존대상을 최소한이 되도록 설계해야한다.

- 의존하는 대상이 많으면 변경될 확률이 높음

- 의존하는 대상은 적을수록 좋음

### 의존하는 대상이 많을 때 1, 기능이 많은 경우

    public class UserService {

      public void regist(RegReq regReq) {
        ....
      }

      public void changePw(ChangeReq chgReq) {
        ....
      }

      public void blockuser(String id, String reason) {
        ....
      }


    }



한 클래스에서 많은 기능을 제공하는 경우
- 각 기능마다 의존하는 대상이 다를 수 있음(위 코드에서는 regist()와 changePw()가 의존하는 대상이 각각 RegReq, ChangeReq로 다르다.)
- 한 기능 변경이 다른 기능에 영향을 줄 수 있음


#### 이러한 문제를 해결하기 위해  ```기능 별로 분리 고려```

    //기능분리 전
    public class UserService {
      public void regist(RegReq regReq) {
        ....
      }
      public void changePw(ChangeReq chgReq) {
        ....
      }
      public void blockuser(String id, String reason) {
        ....
      }
    }
           
                       ↓
                       
    //기능 분리            
    public class UserRegisterService {                           
      public void regist(...) {
        ....
      }
    }
                                               
    public class ChangePwService {
      public void cangePw(...) {
        ...
      }
    }
  
    public class UserBolckService {
      public void blockUser(...) {
        ...
      }
    }


- 기능 별로 분리를 고려

    - 클래스는 증가하지만 각 클래스는 의존하는 대상이 줄어들게 됨
    - 한 기능 변경이 다른 기능에 영향을 주지 않음
    - 개별 클래스를 테스트하기 쉬워짐


### 의존 대상이 많을 때 2, 묶어 보기

[사진]

몇 가지 의존 대상을 단일 기능으로 묶어서 생각하게 된다면 의존 대상을 줄일 수 있다.



## DI

DI란?? 

    DI는 의존성 주입을 의미하며 객체가 다른 객체를 사용하기 위해서 본인의 내부 로직에서 외부 객체에 대한 인스턴스를 생성하는 것이 아닌, 외부로부터 인스턴스를 주입받아 사용하는 것을 의미(외부에서 의존 객체를 주입).

    DI는 생성자 주입과 필드주입이 존재하며, 대체로 외부에서 변경이 가능한 생성자 주입을 사용하는 것을 권고


### 의존 객체를 직접 생성하면??

생성 클래스가 바뀌면 의존하는 코드도 바뀌게 된다(추상화에서 언급).

의존 대상 객체를 직접 생성하지 않는 방법

    - 팩토리, 빌더
    - 의존성 주입 ( Dependency Injection )
    - 서비스 로케이터 ( Service Locator )
    
### 의존 주입( Dependecy Injection )

외부에서 의존 객체를 주입

  - 생성자나 메서드를 이용하여 주입


ex) 생성자나 메서드를 이용하여 주입

    public class ScheduleService {

      private UserRepository userRepository;
      private Calculator cal;

      public ScheduleService(UserRepository userRepository){
        this.userRepository = userRepository
      }

      public void setCalculator(Calculator cal){
        this.cal = cal;
      }
    }
    
초기화 코드
  
    UserRepository userRepository = new UserRepository();
    Calculator cal = new Calculator();

    ScheduleService scheduleService = new ScheduleService(userRepository);
    scheduleService.setCalculator(cal);


의존 주입 방식을 사용하면 UserRepository의 구현체가 변경되더라도 ScheduleService의 코드는 변경하지 않아도 된다.


### 조립기 ( Assembler )

조립기가 객체 생성, 의존성 주입을 처리

ex) : 스프링 프레임워크

    @Configuration
    public class Config {
      @Bean
      public ScheduleService scheduleService() {
        ScheduleService scheduleService = new ScheduleService(userRepository());
        scheduleService.set(cal());
        return scheduleService
      }

      @Bean
      public UserRepository userRepository(){
        ....
      }

      @Bean
      public Calculator cal() {
        ...
      }
    }

사용 코드

    //초기하
    ctx = new AnnotationConfigApplicationContext(config.class);
    
    //사용할 객체 구함
    ScheduleService scheduleService = ctx.getBean(ScheduleService.class);
    
    //사용
    scheduleService.getSchedule(...);


스프링은 위와 같이 설정을 통해 의존을 할 대상을 설정하고, 그것을 초기화하고 사용하게 된다.

스프링에서 가장 권장하는 방법은 생성자 주입이다.

ex)

    @Service
    public class TestService {

        private TestRepository testRepository;

        public TestService(TestRepository testRepository){
            this.testRepository = testRepository;
        }
    }

## DI의 장점

### 의존 대상이 바뀌면 조립기(설정)만 변경하면 된다.

[사진]

위 코드에서도 볼 수 있듯이, OrderService가 의존하고 있는 Notifier가 바뀌더라도 조립기의 코드만 변경하면 된다.

### 의존하는 객체 없이 대역 객체를 사용하여 테스트가 가능해진다

메서드를 이용한 주입방식(setter 주입)

    private MemoryUserRepository userRepo = new MemoryUserRepository()
    private ScheduleService svc = new ScheduleService();

    @BeforeEach
    public void init() {
      svc.setUserRepository(userRepo);
    }

    @Test
    public void givenUser_noCheckPoint_then_getExpectedSchedule() {
      userRepo.addUser("1", new User(...));
      Schedule schedule = svc.getSchedule("1");
      assertEquals(EXPECTED, schedule.getType());
    }

테스트를 진행할 때, UserRepository를 의존하고 있을 때 실제 DB와 연결하는 Repository가 아닌 MemoryUserRepository를 설정을 통해 테스트를 진행 할 수 있다.


생성자 주입방식(interface를 통해 확장성을 가지는 예)

    class Zoo {
      private final Animal animal;

      public Study(Animal animal){
        this.animal = animal;
      }
    }

BigAnimal 이라는 animal을 implements한 클래스가 있다고 가정하면 

Zoo 에서는 Animal이라는 존재만 알고 있어도 BigAnimal이라는 구현체를 받아서 사용할 수 있게 된다.

    Animal bigAnimal = new BigAnimal();
    Zoo zoo = new Zoo(bigAnimal);
    .....

반대로 Zoo클래스 내부에서 의존 객체인 Animal을 생성할 경우

    class Zoo {
      private final Animal animal;

      public Zoo(){
        this.animal = new BigAnimal();
        ....
      }
    }

Zoo는 Animal을 implements한 모든 구현체를 직접 Zoo안에서 수정해야 하는 불편함을 겪게 된다.


DI를 습관처럼 사용하기
- 의존 객체는 주입받도록 코드를 작성하는 습관을 들이자
