# AOP를 활용하여 메소드 실행 시간 측정

## AOP란?

AOP(Aspect-Oriented Programming) 는 OOP를 보완하는 수단으로, 흩어진 Aspect 를 모듈화 할 수 있는 프로그래밍 기법이다.
즉, 여러 곳에서 쓰이는 공통 기능을 모듈화하고, 쓰이는 곳에 필요할 때 연결함으로써, 유지 보수 혹은 재사용에 용이하도록 프로그래밍 하는 것.


### 주요개념

Aspect : 흩어진 관심사를 모듈화 한 것. 주로 부가기능을 모듈화함.

Target : Aspect를 적용하는 곳 (클래스, 메서드 .. )

Advice : Aspect 모듈이 실행해야 하는 일, 실질적으로 어떤 일을 해야할 지에 대한 것, 실질적인 부가기능을 담은 구현체

JointPoint : Advice가 적용될(실행) 위치, 끼어들 수 있는 지점. 메서드 진입 지점, 생성자 호출 시점, 필드에서 값을 꺼내올 때 등 다양한 시점에 적용가능

Point cut : Joint point 의 상세 스펙을 정의한 것

Proxy:  타겟을 감싸서 타겟의 요청을 대신 받아주는 랩핑(Wrapping) 오브젝트, 호출자 (클라이언트)에서 타겟을 호출하게 되면 타겟이 아닌 타겟을 감싸고 있는 프록시가 호출되어, 타겟 메소드 실행전에 선처리, 타겟 메소드 실행 후, 후처리를 실행시키도록 구성되어있습니다.

### 구현

의존성을 추가한다.

	implementation "org.springframework.boot:spring-boot-starter-aop"

그다음 @EnableAspectJAutoProxy 어노테이션을 

	@EnableAspectJAutoProxy
	@SpringBootApplication
	public class AopApplication {
		public static void main(String[] args) {

			SpringApplication.run(HAopApplication.class, args);
		}

	}

위 와 같이 작성해 준다. 모든 서비스에 Aspect을 적용해보자.

	@Aspect
	@Component
	@Slf4j
	public class TimeAop {
		@Around("execution(* com.bs.aop.service..*(..))")
		public Object execute(ProceedingJoinPoint joinPoint) throws Throwable{
			StopWatch stopWatch = new StopWatch();
			log.info("-----START "+ joinPoint.getSignature().getName()+"------");
			stopWatch.start();
			Object returnObj = joinPoint.proceed();
			stopWatch.stop();
			log.info("-----END------");
			log.info("Performance time : " + stopWatch.getTotalTimeMillis()+"(ms)");
			return returnObj;
		}
	}
	
Aspect 모듈임을 알려주기 위한 @Aspect를 명시하고, @Component를 통해 bean으로 등록해준다.
메소드의 매개변수인 ProceedingJoinPoint는 advice가 적용되는 대상이다. 

	joinPoint.proceed();
	
 proceed()를 통해 메소드를 실행해 주고, 실행 결과를 리턴해준다.
 
 @Around 어노테이션은 메소드를 감싸는 형태로 정의된다.
메소드 호출 이전, 이후에도 advice를 적용할 수 있고, 예외 처리도 할 수 있는 다용도 어노테이션이다.

참고

	@Around는 메서드의 실행 전/후에 공통로직을 적용하고 싶을 때 사용하고 
	@Before는 메서드 실행 전에, 
	@After는 메서드 실행 후에 공통 로직을 적용하고 싶을 때 사용한다.


우리는 @Around 어노테이션에 이 advice를 어디에 적용할 지 JoinPoint를 지정해 줄 수 있다.
	
	@Around("execution(* com.bs.aop.service..*(..))")

service 패키지의 모든 메서드를 지정해 주었다.


## PointCut 표현식

 advice가 어떤 JoinPoint에 사용될 것인지를 지정하는 PointCut 표현식
 
 
|명시자|설명|
|------|---|
|execution|Advice를 적용할 메서드를 명시할 때 사용합니다.|
|within|특정 타입에 속하는 메서드를 JoinPoint로 설정되도록 명시할 때 사용합니다.|
|bean|스프링 버전 2.5 버전부터 지원하기 시작했으며, 스프링 빈을 이용하여 JoinPoint를 설정합니다.|


### execution 명시자

execution([수식어] 리턴타입 [클래스이름].이름(파라미터)

- 수식어 : public, private 등 수식어를 명시. (생략 가능)
- 리턴타입 : 리턴 타입을 명시.
- 클래스이름 및 이름 : 클래스이름과 메서드 이름을 명시. (클래스 이름은 풀 패키지명으로 명시해야한다. 생략도 가능)
- 파라미터 : 메서드의 파라미터를 명시.
- " * " : 모든 값을 표현.
- " .. " : 0개 이상을 의미.
- (..) : 모든 타입 인자 허용

Ex)

	execution(* com.bs..*.get*(..))

	 - com.bs 패키지 및 하위 패키지에 속해있고, 이름이 get으로 시작하는 파라미터가 0개 이상인 모든 메서드 
	 

	execution(* com.bs.aop.service..*(..))

	 - com.bs.aop.service 패기지에 속한 파마리터가 0개 이상인 모든 메서드
	 
	
	execution(* com.bs.aop.service..*(..))

	 - com.bs.aop.service 패기지에 속한 파마리터가 0개 이상인 모든 메서드
	 

	execution(* com.bs.aop.service.CartService.cartInfo*(..))
	
	 -  com.bs.aop.service.CartService 패키지에 cartInfo메서드 호출
	 
	
	execution(* aoptest*(*, *))

	 - 메서드 이름이 aoptest로 시작하고 파라미터가 2개인 모든 메서드
	
	
-----

### 결과

	2021-10-22 13:45:30.856  INFO 6716 --- [nio-8080-exec-5] com.bs.aop.config.TimeAop           : -----START cartInfo------
	Hibernate: 
		select
			distinct cart0_.id as id1_0_0_,
			cartitems1_.id as id1_1_1_,
			cart0_.member_id as member_i2_0_0_,
			cartitems1_.cart_id as cart_id5_1_1_,
			cartitems1_.product_id as product_6_1_1_,
			cartitems1_.product_name as product_2_1_1_,
			cartitems1_.product_price as product_3_1_1_,
			cartitems1_.quantity as quantity4_1_1_,
			cartitems1_.cart_id as cart_id5_1_0__,
			cartitems1_.id as id1_1_0__ 
		from
			cart cart0_ 
		left outer join
			cart_item cartitems1_ 
				on cart0_.id=cartitems1_.cart_id 
		where
			cart0_.member_id=?
	2021-10-22 13:45:30.858  INFO 6716 --- [nio-8080-exec-5] com.bs.aop.config.TimeAop           : -----END------
	2021-10-22 13:45:30.859  INFO 6716 --- [nio-8080-exec-5] com.bs.aop.config.TimeAop           : Performance time : 1(ms)

	
