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

        /**
         * Exceptions handled by the annotated method.
         * <p>
         * If empty, will default to any exceptions listed in the method argument list.
         * <p>
         * <b>Note:</b> When exception types are set within value, they are prioritized in mapping the exceptions over
         * listed method arguments. And in case method arguments are provided, they <b>must</b> match the types declared
         * with this value.
         */
        Class<? extends Throwable>[] value() default {};
    }



@GrpcAdive로 선언된 클래스들을 가져와서 해당 클래스에 메소들 중에 @GrpcExceptionHandler 붙은 method를 추출해보자!

    

    //@GrpcAdive로 선언된 클래스 가져오기
    Map<String, Object> annotatedBeans = applicationContext.getBeansWithAnnotation(GrpcAdvice.class);
    
    annotatedMethods = findAnnotatedMethods();
    
    
    



