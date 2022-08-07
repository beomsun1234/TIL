# 추상 팩토리 패턴(Abstract Factory Pattern) 

팩토리 메소드 패턴에서는 하나의 팩토리 클래스가 인풋으로 들어오는 값에 따라 if-else나 switch 문을 사용하여 다양한 서브클래스를 리턴하는 형식으로 구현했었습니다.

```추상 팩토리 패턴에서는 팩토리 클래스에서 서브 클래스를 생성하는 데에 있어 이러한 if-else 문을 걷어냅니다.```

추상 팩토리 패턴은 인풋으로 서브클래스에 대한 식별 데이터를 받는 것이 아니라 또 하나의 팩토리 클래스를 받습니다.


팩토리 메소드 패턴에서 사용했던 예제와 동일하다.

Super Class


    public interface Card {

      public String pay();

    }

Sub Class 1 - 신한카드


    public class SinhanCard extends Card {

      @Override
      public String pay() {
        system.out.println("신한카드 결제")
      }
    }

SubClass 2 - 국민카드


    public class KBCard extends Card {

      @Override
      public String pay() {
        system.out.println("국민카드 결제")
      }
    }


여기까지 팩토리 메소드 패턴과 동일합니다.


이제 추상 팩토리의 역할을 하는 인터페이스 또는 추상 클래스가 필요합니다. 인터페이스로 만들어 보겠습니다!

    public interface CardAbstractFactory {

      public Card createCard();

    }

보시면 createCard의 리턴타입이 super class의 Card입니다! 이제 이 팩토리 인터페이스를 구현하는 클래스에서 createCard()를 오버라이딩하여 각각 서브 클래스에서 리턴합니다!

이는 자바의 다형성을 아주 잘 활용한 방식이라 볼 수 있습니다.

이제 sub class에 대한 팩토리 클래스르 만들어 봅시다! 


SinhanCardFactory


    public class SinhanCardFactory implements CardAbstractFactory {

      @Override
      public Card createCard() {
        return new SinhanCard();
      }
    }



KBCardFactory

    public class KBCardFactory implements CardAbstractFactory {

      @Override
      public Card createCard() {
        return new KBCard();
      }
    }
    
    
이제 마지막으로 이 sub class들을 생성하기 위해 클라이언트 코드에 접점으로 제공되는 컨슈머 클래스(consumer class)를 만들어보겠습니다.


    public class CardFactory {

      public static Card getCard(CardAbstractFactory cardFactory){
        return cardFactory.createCard();
      }
    }
    

이제 클라이언트는 이 CardFactory 클래스의 getCard()라는 static 메소드에 앞서 구현한 SinhanCardFactory나 KBCardFactory 인스턴스를 넣어줌으로써 
 

    팩토리 메소드 패턴 CardFactory 부분
 
    public class CardFactory {

        public static Card getCard(String type){
            if("sinhan".equalsIgnoreCase(type)){
              return new SinhanCard();
            }
            else if("kb".equalsIgnoreCase(type)){
              return new KBCard();
            }
            return null;
        }
    }
 
 
 if-else 없이도 각각 원하는 서브 클래스의 인스턴스를 생성할 수 있게 됐습니다.
 
 

Client

    public class Store {
        public static void main(String[] args) {
            .....

            //신한카드 결제
            Card card = CardFactory.getCard(new SinhanCardFactory()).pay();

            //kb카드 결제
            Card card = CardFactory.getCard(new KBCardFactory).pay();

            ....
        }

    }

## 장점

- 추상 팩토리 패턴은 구현(Implements)보다 인터페이스(Interface)를 위한 코드 접근법을 제공합니다.
위 예에서 getComputer() 메소드는 파라미터로 인터페이스를 받아 처리를 하기 때문에 getComputer() 에서 구현할 것이 복잡하지 않습니다.

- 추상 팩토리 패턴은 추후에 sub class를 확장하는 데 있어 굉장히 쉽게할 수 있습니다.
위 예에서 만약 Laptop 클래스를 추가하고자 한다면 getComputer()의 수정 없이 LaptopFactory만 작성해주면 됩니다.
이러한 특징에 기반하여 추상 팩토리 패턴은 "Factory of Factories"라고도 불립니다.
 
- ```추상 팩토리 패턴은 팩토리 패턴(팩토리 메소드 패턴)의 조건문(if-else, switch 등)으로부터 벗어납니다.```

## 참고

https://readystory.tistory.com/m/119
