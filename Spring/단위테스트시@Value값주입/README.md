# 단위테스트시 @Value 값 주입

프로젝트 진행 중에 jwt토큰관련 단위테스트 중 프로퍼티로 주입받은 key값에 대한 오류가 발생했다...(null)

SpringBootTest 어노테이션이 없는 단위 테스트시 @value값이 주입되지 않는 경우 발생하는 오류이다.


    @ContextConfiguration(
    initializers = {ConfigFileApplicationContextInitializer.class}
    )
    @ExtendWith(MockitoExtension.class)
    class JwtUtilTest {
    	......testcode......
    }


해당 방식을 시도하였지만 실패하였다... 값이 채워지지 않는다.. 즉 @Value로 주입받은 값이 null이 나온다..

열심히 검색 중 stackoverflow에서 아래와 같이 생성자 매개변수로 값을 넣어보라는 글을 보았다. 해당 방식으로 클래스를 단일 및 통합 모두에서 테스트 가능하게 만들라는 말이 었다.


기존 코드


  	@Component
  	public class Foo{   
    	  @Value("${property.value}") private String property;
    	  //...
  	}

변경 코드

  	@Component
  	public class Foo{   
    	private String property;

      	public Foo(@Value("${property.value}") String property){
         	this.property = property;
      	}

      	//...         
  	}


### 내 코드


기존

	@Component
	public class JwtUtil {

    	public final static long TOKEN_VALIDATION_SECOND = 1000L * 60L * 60L;

  
    	@Value("${secret.key}")
        String secretKey
       
        ...............
      
    }
        

변경

	@Component
	public class JwtUtil {

    	public final static long TOKEN_VALIDATION_SECOND = 1000L * 60L * 60L;

  
    	private String secretKey;
        
        public JwtUtil(@Value("${secret.key}") String secretKey){
        	this.secretKey = secretKey;        
        }
        
        ...............
      
    }
        
     
변경 후 오류가 해결됐다:)



### 참고 사이트

https://stackoverflow.com/questions/17353327/populating-spring-value-during-unit-test
