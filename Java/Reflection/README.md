# Java Reflection

[grpc-spring-boot-starter](https://github.com/yidongnan/grpc-spring-boot-starter) 를 참고해서 현재 Annotation 기반의 GRPC Error Advice 기능을 만들어 보고 있다. 

@GrpcAdvice 어노테이션을 스프링 컨테이너에 등록해준다. 해당 어노테이션을 사용하는 클래스들을 스프링컨테이너에서 가져와서 해당 클래스에서 @GrpcExceptionHandler 어노테이션을 가지는 Method를 찾아 invoke 하여 값을 얻는다. @GrpcExceptionHandler 어노테이션의 value는 error class이며, 인터셉터에서 GrpcExceptionHandler에서 설정한 에러가 발생했을 때 값을 리턴해주기 위해 map을 만들어서 키를 해당 어노테이션을 가지는 method의 error 클래스로 설정하고 value를 해당 method를 invoke 시킨 값을 넣어준다. 이후 인터셉터에서 에러를 잡아내면 설정항 map에 있는지 확인해서 있으면 value를 불러서 error를 컨트롤 한다.

## @GrpcAdive

    @Target({ElementType.TYPE, ElementType.METHOD})
    @Retention(RetentionPolicy.RUNTIME)
    @Component
    public @interface GrpcAdvice {

    }


## @GrpcExceptionHandler


    @Target(ElementType.METHOD)
    @Retention(RetentionPolicy.RUNTIME)
    public @interface GrpcExceptionHandler {
        Class<? extends Throwable> value();
    }


@GrpcAdive로 선언된 클래스들을 가져와서 해당 클래스에 메소들 중에 @GrpcExceptionHandler 붙은 method를 추출해보자!

    
    
    //@GrpcAdive 어노테이션으로 선언된 오브젝트
    private Map<String, Object> annotatedBeans;
    
    //@GrpcAdivce가 선언된 클래스 안에  @GrpcExceptionHandler가 선언된 메소드
    private Set<Method> annotatedMethods;
    
    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
        
        //@GrpcAdive 어노테이션으로 선언된 오브젝트 가져오기
        Map<String, Object> annotatedBeans = applicationContext.getBeansWithAnnotation(GrpcAdvice.class);
        
        
        annotatedBeans.values().forEach(value-> log.info(String.valueOf(value.getClass())));
        annotatedBeans.forEach(
                (key, value) -> log.debug("Found gRPC advice: " + key + ", class: " + value.getClass().getName()));

        ///@GrpcAdive 어노테이션으로 선언된 오브젝트의 클래스에 @GrpcExceptionHandler 어노테이션이 붙은 method 추출, @GrpcExceptionHandler 타겟 타입은 메소드이다.
        annotatedMethods = annotatedBeans
                .values()
                .stream()
                .map(obj -> obj.getClass())
                .map(objClass -> findAnnotatedMethods(objClass))
                .flatMap(Collection::stream)
                .collect(Collectors.toSet());

    }
    
        
    //@GrpcAdive 어노테이션으로 선언된 오브젝트의 클래스에 @GrpcExceptionHandler 어노테이션이 붙은 method 추출
    private Set<Method> findAnnotatedMethods(final Class<?> clazz) {
        return MethodIntrospector.selectMethods(clazz, new ReflectionUtils.MethodFilter() {
            @Override
            public boolean matches(Method method) {
                return AnnotatedElementUtils.hasAnnotation(method,GrpcExceptionHandler.class);
            }
        });
    }


    //@GrpcExceptionHandler가 선언된 메소드들를 invoke 해서 return 타입을 가져오자
    public void getObject() {
        Assert.state(annotatedMethods != null, "@GrpcExceptionHandler annotation scanning failed.");
        
        // annotatedMethods = @GrpcExceptionHandler 선언된 메소들들
        for (Method annotatedMethod : annotatedMethods) {            
            GrpcExceptionHandler annotation = annotatedMethod.getDeclaredAnnotation(GrpcExceptionHandler.class);
            
            Object newInstance = annotatedMethod.getDeclaringClass().newInstance();
            try {
                Object invoke = annotatedMethod.invoke(newInstance);
                
                // 해당 메소드의 return 타입이 Status면
                if (invoke instanceof Status){
                    // 해당 메소드를 수행하고 리턴된 코드를 출력
                    log.info(String.valueOf(((Status) invoke).getCode()));
                
                // 해당 메소드의 retun 타입이 StatusRuntimeException 이면
                } else if (invoke instanceof StatusRuntimeException) {
                    // 해당 메소드를 수행하고 리턴된 코드를 출력
                    log.info(String.valueOf(((StatusRuntimeException) invoke).getStatus().getCode()));
                }
            } catch (IllegalAccessException e) {
                throw new RuntimeException(e);
            } catch (InvocationTargetException e) {
                throw new RuntimeException(e);
            }    
        }
    }
    
    
@GrpcAdivce가 선언된 클래스 안에  @GrpcExceptionHandler가 선언된 메소드의 리턴 값 들을 확인해 볼 수 있었다. 아래 코드는 @GrpcAdivce, @GrpcExceptionHandler가 선언된  클래스이다.


    @GrpcAdvice
    public class GrpcAnoTest {

        @GrpcExceptionHandler(NoSuchElementException.class)
        public Status noSuchElementException(){
            return Status.NOT_FOUND.withDescription("test");
        }

        @GrpcExceptionHandler(IllegalArgumentException.class)
        public StatusRuntimeException illegalArgumentException(){
            return Status.INVALID_ARGUMENT.withDescription("test").asRuntimeException();
        }
    }

@GrpcExceptionHandler 어노테이션의 value인 error class를 가져와 비교해보자!


    public void get throws InstantiationException, IllegalAccessException {
        Assert.state(annotatedMethods != null, "@GrpcExceptionHandler annotation scanning failed.");
  
        for (Method annotatedMethod : annotatedMethods) {
            
            //해당 메소드에서 @GrpcExceptionHandler 어노테이션을 가져온다.
            GrpcExceptionHandler annotation = annotatedMethod.getDeclaredAnnotation(GrpcExceptionHandler.class);
            Assert.notNull(annotation, "@GrpcExceptionHandler annotation not found.");
            
            
            //@GrpcExceptionHandler 어노테이션의 value인 error class를 가져온다.
            Class<? extends Throwable> error = annotation.value();
            
            Object newInstance = annotatedMethod.getDeclaringClass().newInstance();

            try {
                Object invoke = annotatedMethod.invoke(newInstance);
                if (invoke instanceof Status){
                    
                    //해당 메소드의 @GrpcExceptionHandler 어노테이션에 value에 IllegalArgumentException.class 가 있는지 확인
                    if (!error.equals(IllegalArgumentException.class)) {
                        log.info("IllegalArgumentException 에러는 없다.");
                        continue;
                    }
                    log.info("IllegalArgumentException 에러가 있다.");
                    log.info(String.valueOf(((Status) invoke).getCode()));
                } else if (invoke instanceof StatusRuntimeException) {
                
                    //해당 메소드의 @GrpcExceptionHandler 어노테이션에 value에 IllegalArgumentException.class 가 있는지 확인
                    if (!error.equals(IllegalArgumentException.class)) {
                        log.info("IllegalArgumentException 에러는 없다.");
                        continue;
                    }
                    log.info("IllegalArgumentException 에러가 있다.");
                    log.info(String.valueOf(((StatusRuntimeException) invoke).getStatus().getCode()));
                }

            } catch (IllegalAccessException e) {
                throw new RuntimeException(e);
            } catch (InvocationTargetException e) {
                throw new RuntimeException(e);
            }
        }
    }

Map 을 만들어서 key를 error class로 설정하고 value를 구성해주면 error를 컨트롤 할 수 있다. 
