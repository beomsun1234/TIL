# 추상화

## 다형성과 추상화


  다형성이란  여러(poly) 모습(morph)을 갖는 것이며 객체 지향에서는 한 객체가 여러 타입을 갖는 것 이다. 즉, 한 객체가 여러 타입의 기능을 제공한다는 의미다.
  타입 상속으로 다형성 구현이 가능하다.(하위 타입은 상위 타입도 됨)


```타입상속에는 클래스상속과 인터페이스 상속이 있다.```

Timer

    public class Timer {
      public void start() {...}
      public void stop() {...}
    }

Rechargeable

    public interface Rechargeable {
      void charge();
    }

IotTimer

    public class IotTimer extend Timer implements Rechargeable {

      public void charge(){
        ....
      }

    }
    
구현코드

    IotTimer it = new IotTimer()
    it.start();
    it.stop();
    
    Timer t = it;
    t.start();
    t.stop();
    
    Rechargeable r = it;
    r.charge();
    
    
IotTimer 클래스는 Timer 클래스와 Rechargeable 인터페이스를 상속하며 IotTimer 객체는 Timer 타입과 Rechargeable 타입으로 형 변환이 가능하다. 구현 코드를 보면
IotTimer 객체를 Timer 타입과 Rechargeable 타입에 할당하여 각 타입의 기능을 사용하고 있다.


## 추상화

  데이터나 프로세스 등을 의미가 비슷한 개념이나 의미있는 표현으로 정의하는 과정

```두 가지 방식의 추상화```

#### 1. 특정한 성질 묶기

- 사용자에서 아이디, 이름, 이메일을 묶어서 유저 테이블로 추상화
- 통화, 금액을 Money 클래스로


#### 2. 공통 성질 추출

- 지포스, 라데온의 공통점은 GPU
- HP, 삼성의 공통점은 프린터

### 타입 추상화


![다형성추상화1](https://user-images.githubusercontent.com/68090443/175808471-fd8a8282-ae8c-48d9-b5d1-2fb87e4e2be2.PNG)



- 여러 구현 클래스를 대표하는 상위 타입 도출(공통 성질 추출)
- 흔히 인터페이스 타입으로 추상화
- 추상화 타입과 구현 타입(콘크리트 클래스) 상속으로 연결

사진에 EmailNotifier, SMSNotifier, KakaoNotifier 클래스의 공통점은 Notifier이다. 이를 아래의 과정으로 추상화한다.

    1.Notifier 인터페이스를 만든다.(상위타입 도출)
    2.Notifier를 상속한 구현 클래스(EmailNotifier, SMSNotifier, KakaoNotifier)를 만든다. (추상화 타입과 구현 타입 상속으로 연결)


#### 타입 추상화 사용

콘크리트 클래스에서 추상 타입을 도출하면 추상 타입을 이용한 프로그래밍이 가능하다.

    Notifier notifier = getNotifier(...);
    notifier.notify(someNoti);

추상 타입은 구현을 감춘다. 기능의 구현이 아닌 의도를 더 잘 드러낸다.

ex)

    Notifier notifier = getNotifier(...);
    notifier.notify(someNoti);

위 코드는 Notifier 타입으로 getNotifier() 를 통해 객체를 꺼내옴으로써 알림을 보내겠다는 의도를 잘 드러낸다.

#### 추상 타입 사용 이점 : 유연함

변경에 유연하기 때문이다.(유연함)

추상화 미적용 예제를 확인해 보자!!(콘크리트 클래스 직접사용)

최초 요구사항 - '주문 취소시 SMS에 알림 전송해주세요~'

아래는 처음 요구사항에 대한 코드이다.

      //주문 취소시 SMS 알림 전송
      private SmsSender smsSender;

      public void cancel(String ono) {
        ...주문 취소 처리

        smsSender.sendSms(...);
      }

두번째 요구사항이 들어왔다. '...씨 Kakao 알림이 가능하면 Kakao로 알림 전송해 주세요~'

아래는 다음 요구사항을 추가한 코드이다.

      private SmsSender smsSender;
      private KakaoPush kakaoPush;

      public void cancel(String ono) {
        ... 주문 취소 처리

        if (pushEnabled) {
          kakaoPush.push(...);
        } else {
          smsSender.sendSms(...);
        }
      }

마지막 요구사항 - '항상 이메일 알림 전송해주세요~'

아래는 마지막 요구사항을 추가한 코드이다.

      private SmsSender smsSender;
      private KakaoPush kakaoPush;
      private MailService mailSvc;

      public void cancel(String ono) {
        ... 주문 취소 처리

        if (pushEnabled) {
          kakaoPush.push(...);
        } else {
          smsSender.sendSms(...);
        }
        mailSvc.sendMail(...);

      }

위 예제 처럼 요구사항 변경에 따른 주문취소 코드도 함께 변경된다.

해당 코드에 추상화를 적용해보자!!

공통점을 도출하면

      sms전송         추상화   
      카카오톡 보냄   ------>    통지
      이메일 발송

도출한 추상타입 사용

    public void cancel(String ono) {
      ... 주문 취소 처리
      Notifier notifier = getNotifier(...);
      notifier.notify(...);
    }

    private Notifier getNotifier(...){
      if(pushEnabled) {
        return new KakaoNotifier();
      }
      else {
        return new SmsNotifier();
      }
    }
  
Notifier 객체를 이용해 알림을 보낸다는 의도를 명확하게 전달하고 getNotifier()를 이용해 상황에 맞는 알림 구현체를 생성했다. 이제 요구사항이 들어와도 getNotifier()만 수정하면 된다.

사용할 대상 접근도 추상화 해보자! 

    private Notifier getNotifier(...){
      if(pushEnabled) {
        return new KakaoNotifier();
      }
      else {
        return new SmsNotifier();
      }
    }
  
위 코드를 추상화하여 다형성을 적용할 수 있다.

    public void cancel(String ono) {
      ... 주문 취소 처리
      Notifier notifier = NotifierFactory.instance().getNotifier(...);
      notifier.notify(...);
    }


NotifierFactory 인터페이스

    public interface NotifierFactory {
      Notifier getNotifier(...);

      static NotifierFactory instance() {
        return new DefaultNotifierFactory();
      }
    }

NotifierFactory 인터페이스를 상속한 DefaultNotifierFactory 클래스

    public class DefaultNotifierFactory implements NotifierFactory {
      public Notifier getNotifier(...) {
        if (pushEnabled) return new KakaoNotifier();
        else return new SmsNotifier();
      }
    }

DefaultNotifierfactory 클래스는 NotifierFactory 인터페이스의 구현 클래스이다.

NotifierFactory 인터페이스는 알림 방식을 지정하는 기능과 알림 방식 구현 클래스(DefaultNotifierfactory)를 반환한다.


#### 추상화는 의존 대상이 변경하는 시점에 진행

- 추상화 -> 추상 타입 증가 -> 복잡도 증가

- 아직 존재하지 않는 기능에 대한 추상화는 주의! -> 잘못된 추상화 가능성이 있고, 복잡도만 증가

- 실제 변경 및 확장이 발생할 때 추상화 시도

#### 추상화를 잘 하려면

- 구현을 한 이유가 무엇 때문인지 생각하기


