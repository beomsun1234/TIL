# 어댑터 패턴(Adapter Pattern) 

어댑터 패턴은 클래스의 인터페이스를 사용자가 기대하는 인터페이스 형태로 변환시키는 패턴입니다.

어댑터 패턴은 서로 일치하지 않는 인터페이스를 갖는 클래스들을 함께 동작시킵니다.

예제를 만들어 봅시다! 고양이와 강이지가 있고 Animal이라는 인터페이스를 사용하고있습니다.

    public interface Animal {

        public void sound();

    }

Cat

    public class Cat implements Animal {

        @Override
        public void sound() {
            System.out.println("Cat 야옹");
        }


    }


Dog

    public class Dog implements Animal {

        @Override
        public void sound() {
            System.out.println("Dog 멍멍");
        }

    }


여기서 호랑이를 만드는데 호랑이는 Animal 인터페이스를 사용하지 않기로 협의했다.

    public class Tiger {
        
        public void roar(){
            System.out.println("으르렁")
        }

    }
    
    
시간이 지나 동물의 소리를 출력할 때 호랑이의 으르렁 소리도 포함 되어야한다고 했다. Tiger는 Animal 인터페이스를 사용하지 않기로 합의 했기에 방법을 찾아야한다.

어댑터 패턴을 사용해 보자!

Tiger 어댑터를 만들어보자!(Object Adapter 방식)

    public class TigerAdapter implements Animal {
        private Tiger tiger;
        
        @Override
        public void sound() {
            tiger.roar();
        }

    }


Client


    public class AppMain {

      public static void main(String[] args) {
          ArrayList<Animal> animals = new ArrayList<Animal>();
          animals.add(new Dog());
          animals.add(new Cat());
          animals.add(new TigerAdapter());

          aniamls.forEach(animal -> {
            animal.sound();
          });
      }

    }


요구사항대로 타이거 울음소리도 함께 출력 할 수 있게 되었다.

다음 예제를 더 알아보자!

ex) 볼트 변환기

    public class Volt {

        private int volts;

        public Volt(int v){
            this.volts=v;
        }

        public int getVolts() {
            return volts;
        }

        public void setVolts(int volts) {
            this.volts = volts;
        }

    }

Socket 클래스는 120 볼트만 제공하는 클래스여서, 다른 볼트로 호환되려면 볼트 변환기가 필요하다

    public class Socket {

        public Volt getVolt(){
            return new Volt(120);
        }
    }


이제 우리는 120볼트뿐만 아니라 3볼트와 12볼트도 추가로 생성하는 어댑터를 만들어보자!


    public interface SocketAdapter {

        public Volt get120Volt();

        public Volt get12Volt();

        public Volt get3Volt();
    }

어댑터 패턴을 구현하기 위해서는 Class Adapter와 Object Adapter 두 가지 방법이 있습니다.

어떤 방법으로 구현하던 결과는 같습니다.


    Class Adapter - 자바의 상속(Inheritance)을 이용한 방법입니다.
    Object Adapter - 자바의 합성(Composite)을 이용한 방법입니다.
    

```Class Adpater 방식```

    public class SocketClassAdapterImpl extends Socket implements SocketAdapter{

        @Override
        public Volt get120Volt() {
            return getVolt();
        }

        @Override
        public Volt get12Volt() {
            Volt v= getVolt();
            return convertVolt(v,10);
        }

        @Override
        public Volt get3Volt() {
            Volt v= getVolt();
            return convertVolt(v,40);
        }

        private Volt convertVolt(Volt v, int i) {
            return new Volt(v.getVolts()/i);
        }

    }

```Object Adapter 방식```

    public class SocketObjectAdapterImpl implements SocketAdapter{

        private Socket sock = new Socket();

        @Override
        public Volt get120Volt() {
            return sock.getVolt();
        }

        @Override
        public Volt get12Volt() {
            Volt v= sock.getVolt();
            return convertVolt(v,10);
        }

        @Override
        public Volt get3Volt() {
            Volt v= sock.getVolt();
            return convertVolt(v,40);
        }

        private Volt convertVolt(Volt v, int i) {
            return new Volt(v.getVolts()/i);
        }
    }
    
    

Test

    public class TestAdapterPattern2 {

        public static void main(String[] args) {

            testClassAdapter();
            testObjectAdapter();
        }

        private void testObjectAdapter() {
            SocketAdapter sockAdapter = new SocketObjectAdapterImpl();
            Volt v3 = sockAdapter.get3Volt();
            Volt v12 = sockAdapter.get12Volt();
            Volt v120 = sockAdapter.get120Volt();
            System.out.println("v3 ->" + v3.getVolts());
            System.out.println("v12 ->" + v12.getVolts());
            System.out.println("v120 ->" +v120.getVolts());
        }

        private void testClassAdapter() {
            SocketAdapter sockAdapter = new SocketClassAdapterImpl();
            Volt v3 = sockAdapter.get3Volt();
            Volt v12 = sockAdapter.get12Volt();
            Volt v120 = sockAdapter.get120Volt();
            System.out.println("v3 ->" + v3.getVolts());
            System.out.println("v12 ->" + v12.getVolts());
            System.out.println("v120 ->" +v120.getVolts());
        }
    }

## Class Adapter 

- 오버라이드를 이용하여 기능을 추가 할 수 있다.
- 어댑터를 하나로 사용할 수 있다.
- 특정 클래스에서만 적용된다.(단점)
- 다중상속 문제. (단점)


## Object Adapter 

- 모든 서브클래스에 적용된다.
- 유연성이 높다.
- 어댑터 하나만으로 사용할 수 없다.(단점) 

## 참고

- https://readystory.tistory.com/m/125
- https://www.slideshare.net/chihwanchoi90/4-62960235

