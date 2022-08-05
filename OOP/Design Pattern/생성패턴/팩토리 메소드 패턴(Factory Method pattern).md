# 팩토리 메소드 패턴(Factory Method pattern)

객체를 생성하기 위한 인터페이스를 정의하는데, 어떤 클래스의 인스턴스를 만들지는 서브클래스에서 결정하게 만든다. 즉 팩토리 메소드 패턴을 이용하면 클래스의 인스턴스를 만드는 일을 서브클래스에게 맡기는 것.

즉 해 여러 개의 서브 클래스를 가진 슈퍼 클래스가 있을 때 인풋에 따라 하나의 자식 클래스의 인스턴스를 리턴해주는 방식


팩토리 패턴에서는 클래스의 인스턴스를 만드는 시점을 서브 클래스로 미룹니다.

이 패턴은 인스턴스화에 대한 책임을 객체를 사용하는 클라이언트에서 팩토리 클래스로 가져옵니다. 



ex) 카드 사용


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

   
Factory Class

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


Client

    public class Store {
        public static void main(String[] args) {
            .....
            
            //신한카드 결제
            Card card = CardFactory.getCard("sinhan").pay();
            //kb카드 결제
            Card card = CardFactory.getCard("kb").pay();
            
            ....
        }

    }



## 장점

팩토리 패턴은 클라이언트 코드로부터 서브 클래스의 인스턴스화를 제거하여 서로 간의 종속성을 낮추고, 결합도를 느슨하게 하며(Loosely Coupled), 확장을 쉽게 합니다.

위 예제에서 작성한 클래스 중 Sinhan class에 대해 수정 혹은 삭제가 일어나더라도 클라이언트는 알 수 없기 때문에 코드를 변경할 필요도 없습니다.

팩토리 패턴은 클라이언트와 구현 객체들 사이에 추상화를 제공합니다.

## 참고

https://readystory.tistory.com/m/117
