# 퍼사드 패턴(Facade Pattern)

Facade는 "건물의 정면"을 의미하는 단어로 어떤 소프트웨어의 다른 커다란 코드 부분에 대하여 간략화된 인터페이스를 제공해주는 디자인 패턴을 의미합니다. 

서브시스템에 있는 인터페이스들에 대한 통합된 인터페이스를 제공한다. 퍼사드란 서브시스템을 더 쉽게 사용할 수 있도록 만드는 더 높은 수준의 인터페이스를 말합니다.


    Facade: 클라이언트의 요청을 적절한 서브시스템 클래스에 위임한다.
    Subsystem classes: 서브시스템 기능을 구현한다. 서브시스템 클래스는 facade에 의해서만 사용된다.
    Client: Facade에게 특정 행동을 수행해달라고 요청한다.
    
    
간단한 예를 들어보겠습니다! 

집의 가전제품들을 자동으로 제어하는 자동화 장치를 생각해보자! 

자동화 장치는 TV, Lights, AirConditioner을 제어합니다.

Subsystem을 TV, Lights, AirConditioner로 생각 할 수 있습니다. 클래스를 작성해보겠습니다!! 


코드


    public interface Appliance {
      public void turnOn();
      public void turnOff();
    }
  
TV


    public class TV implements Appliance {
        @Override
        public void turnOn() {
          System.out.println("TURN ON TV");
        }


        @Override
        public void turnOff() {
          System.out.println("TURN OFF TV");
        }
    }
  
Lights


    public class Lights implements Appliance {
        @Override
        public void turnOn() {
          System.out.println("TURN ON Lights");
        }


        @Override
        public void turnOff() {
          System.out.println("TURN OFF Lights");
        }
    }

AirConditioner


    public class AirConditioner implements Appliance {
        @Override
        public void turnOn() {
          System.out.println("TURN ON AirConditioner");
        }

        @Override
        public void turnOff() {
          System.out.println("TURN OFF AirConditioner");
        }
    }

이제 Facade 클래스를 정의합니다. Facade를 HomeFacade 클래스로 정의하고 집에 도착했을 때와 집을 나갈 때 두가지 작업을 진행합니다.

집에 도착하면 TV, Lights, AirConditioner을 키고, 집에서 나가면 TV, Lights, AirConditioner 끄는 작업을 수행합니다.


    public class HomeFacade {

      public void ArriveAtHome(){
        ArrayList<Appliance> appliances = Arrays.asList(new TV(), 
                                                        new Lights(),
                                                        new AirConditioner())

        appliances.forEach( appliance ->  appliance.turnOn() );

      }

      public void LeaveFromHome(){
        ArrayList<Appliance> appliances = Arrays.asList(new TV(), 
                                                        new Lights(),
                                                        new AirConditioner())

        appliances.forEach( appliance ->  appliance.turnOff() );

      }
    }


Client

    public class FacadePatternTest {

        @Test
        public void 집에도착하면가전기기가켜진다()
        {
            HomeFacade homeFacade = new HomeFacade();
            homeFacade.ArriveAtHome();
        }

        @Test
        public void 집을나가면가전기기가꺼진다()
        {
            HomeFacade homeFacade = new HomeFacade();
            homeFacade.LeaveFromHome();
        }
  
퍼사드 패턴을 사용하게 되면 클라이언트 부분에 무겁게 로직을 작성할 필요 없이 HomeFacade 객체의 ArriveAtHome(), LeaveFromHome() 메서드를 호출함으로써 간단하게 가전기기를 제어할 수 있습니다.

또한 쇼핑몰에서 주문할 때 인벤토리, 페이, 배송 등등 여러 프로세스가 존재하고 상호작용합니다. 여기에도 퍼사드 패턴을 적용하여 상호작용을 단순화 할 수 있습니다.

[사진](https://springframework.guru/gang-of-four-design-patterns/facade-pattern/)


## 퍼사드 패턴의 중요 포인트!

- 퍼사드 패턴은 클라이언트 어플리케이션의 헬퍼 역할을 하는 것이지, 서브시스템 인터페이스를 숨기는 것은 아닙니다.
- 퍼사드 패턴은 특정 기능에 대해 인터페이스의 수가 확장되고(위 예제로 치면 디비 종류나 리포트 종류가 늘어난다는 등), 시스템이 복잡해질 수 있는 상황에서 사용하기 적합합니다.
- 퍼사드 패턴은 비슷한 작업을 해야하는 다양한 인터페이스들 중 하나의 인터페이스를 클라이언트에 제공해야 할 때 적용하는 것이 좋습니다.
- 팩토리 패턴과 종종 함께 사용됩니다.

## 참고

- https://readystory.tistory.com/m/193
- https://springframework.guru/gang-of-four-design-patterns/facade-pattern/
- https://www.c-sharpcorner.com/article/quick-start-on-facade-design-pattern/
- https://lktprogrammer.tistory.com/42
