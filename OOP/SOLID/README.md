# SOLID

객체 지향 프로그래밍 및 설계의 다섯 가지 기본 원칙

SRP(단일 책임 원칙), OCP(개방-폐쇄 원칙), LSP(리스코프 치환 원칙), DIP(의존 역전 원칙), ISP(인터페이스 분리 원칙)을 말하며, 앞자를 따서 SOILD 원칙이라 부른다.

## SRP (Single Responsibility Principle) 단일 책임 원칙

```어떤 클래스를 변경해야 하는 이유는 오직 하나뿐이어야 한다. - 로버트 C.마틴```


    소프트웨어의 설계 부품(클래스, 함수 등)은 단 하나의 책임만을 가져야 한다. 
    작성된 클래스는 하나의 기능만 가지며 클래스가 제공하는 모든 서비스는 그 하나의 책임을 수행하는데 집중해야한다. 이는 어떤 변화에 의해 클래스를 변경해야 하는 이유는 오직 하나 뿐이어야함을 의미한다. 
    변경의 이유가 한가지라는 것은 해당 모듈이 여러 대상 또는 액터들에 대해 책임을 가져서는 안되고, 
    오직 하나의 액터(사용자가 특정 역활을 수행)에 대해서만 책임을 져야 한다는 것을 의미한다.


```하나의 모듈은 하나의, 오직 하나의 액터에 대해서만 책임져야 한다.```

모듈이 하나의 객체 혹은 소스 파일로 볼 수 있다. 여기서 액터는 개발자/팀이라고 볼 수 있다. 그렇다면, 하나의 소스 파일은 개발자/팀이 책임 져야 한다는 것이다. 분리된 팀이 하나의 소스 파일을 건드린다면 팀을 합치거나 혹은 파일을 분리해야 한다는 이야기로 이해할 수 있다.

[사진](https://moons-memo.tistory.com/218)

위는 클래스에 단일 책임원칙을 적용한 예 이다.

다른 예로 개발 회사의 직원을 예로 들어보겠다. SUN 회사의 직원은 backend, frontend, designer, dba, devops 등이 있다고 하자! 


![srp1](https://user-images.githubusercontent.com/68090443/178032529-b54d156d-607e-4888-85cf-4179e9b6171d.PNG)



코드


        public class Employee{

            public void workBackend(){
                system.out.println("백엔드 작업")
            }

            public void workFrontend(){
                system.out.println("프론트엔드 작업")
            }

            public void workDesigner(){
                system.out.println("디자이너 작업")
            }

            ......

        }

위 코드는 SRP를 지키지 않았다. employee가 너무 많은 책임을 가지고 있다.. 이를 리팩토링 해보자!


![srp2](https://user-images.githubusercontent.com/68090443/178032556-d6b5dfa6-860a-4618-9b5a-1f1fe07af172.PNG)


코드

        public interface Employee{
            void doWork();
        }
        
        ---------------------------------------
        
        public class Backend implement Employee{
            @Override
            public void doWork(){
                system.out.println("백엔드 작업")
            }
        }
        
        public class Frontend implement Employee{
            @Override
            public void doWork(){
                system.out.println("프론트엔드 작업")
            }
        }
        
        public class Designer implement Employee{
            @Override
            public void doWork(){
                system.out.println("디자이너 작업")
            }
        }



각자의 역활을 하도록 분리하여 구현하였다. 객체 지향 4대 특성 중, 단일 책임 원익과 가장 관계가 깊은 특성은 모델링을 담당하는 '추상화'이다.


## OCP (Open-Closed Principle) 개방-폐쇄 원칙

![ocp4](https://user-images.githubusercontent.com/68090443/178033275-a72e14e9-27c5-494a-8d19-6b9d8f29cdce.PNG)

 소프트웨어 요소는 확장에는 열려있고 변경에는 닫혀있어야한다. 
 클래스는 확장에는 개방적이어야 하고, 변경에는 폐쇄적이어야 한다.

확장을 하는데 어떻게 코드를 변경하지 않을까??? ```인터페이스 안에 필요 기능을 작성한다면 인터페이스를 구현하는 구현클래스는 다형성을 통해서 새로운 기능의 확장이 가능하다.```

다형성을 활용하자!!

ex1) JDBC

![ocp1](https://user-images.githubusercontent.com/68090443/178032696-307a15a1-df7e-4b49-a50c-355074cab008.PNG)


JDBC 는 데이타 커넥션 부분만 변경하면, 어떤 DB 에서도 동일하게 사용할 수 있다.
(JDBC 는 DB 에 개방적이다.) 다르게 표현해보면, JDBC 는 DB가 중간에 변경되더라도 영향을 받지 않게 설계되어 있다.
(JDBC 는 DB의 변경에 닫혀있다.)
  

ex2) 송금시 신한은행을 사용하고 있었다.

코드

        public class TransferService(){
            private SinhanTransfer sinhanTransfer

            public TransferService(SinhanTransfer sinhanTransfer){
                this.sinhanTransfer = sinhanTransfer
            }

            public void transfer(){
                sinhanTransfer.transfer()
            }

        }

        public class SinhanTransfer {
            public void transfer(){
                system.out.println("신한은행 송금");
            }
        }

신한은행에서 국민으로 바뀐다면??

![ocp2](https://user-images.githubusercontent.com/68090443/178032840-0e82dbe9-1bc0-47ba-8e14-034bf2d7bb3e.PNG)


코드

        public class KBTransfer {
            public void transfer(){
                system.out.println("국민은행 송금");
            }
        }
        
        public class TransferService(){
            private KBTransfer kbTransfer

            public TransferService(SinhanTransfer kbTransfer){
                this.sinhanTransfer = sinhanTransfer
            }

            public void transfer(){
                kbTransfer.transfer()
            }

        }



만약 다른 은행이 또 추가된다면 기존의 코드를 수정해야 하기 때문에 위 코드는 OCP를 위반하는 코드이다. 이를 해결해보자!!


![ocp3](https://user-images.githubusercontent.com/68090443/178033123-8cc9517f-2947-4c04-8481-bba29a21104c.PNG)


코드

        public interface TransferMethod {
            void transfer();
        }
        
        public class KBTransfer implement TransferMethod{
            @Override
            public void transfer(){
                system.out.println("국민은행 송금");
            }
        }

        public class SinhanTransfer implement TransferMethod{
            @Override
            public void transfer(){
                system.out.println("신한은행 송금");
            }
        }
        
        public class TransferService(){
            private   transferMethod

            public TransferService(TransferMethod transferMethod){
                this.transferMethod = transferMethod
            }

            public void transfer(){
                transferMethod.transfer()
            }
        }
        
이제 송금방식에 다른 은행이 추가 되더라도 TransferService를 변경하지 않아도 된다!!
 
### LSP (Liskov Substitution Principle) 리스코프 치환 원칙

- 자식 클래스는 언제나 자신의 부모 클래스를 대체할 수 있다는 원칙이다. 즉 부모 클래스가 들어갈 자리에 자식 클래스를 넣어도 계획대로 잘 작동해야 한다.
- 자식클래스는 부모 클래스의 책임을 무시하거나 재정의하지 않고 확장만 수행하도록 해야 LSP를 만족한다.


        만약 S가 T의 서브타입이라면, T는 어떠한 경고도 내지 않으면서, S로 대체(치환) 가능해야하한다.
        
        
![lsp1](https://user-images.githubusercontent.com/68090443/178033322-85f5b859-773d-4a9f-b682-0cd086785dde.PNG)



자식 클래스가 부모클래스의 기능을 똑같이 수행할 수 없을때, 이는 버그를 발생시키는 요인이 .

ex) 대표적인 예제로 사각형 예제

        public class Rectangle {
            private int width;
            private int height;

            public void setHeight(int height) {
                this.height = height;
            }

            public int getHeight() {
                return this.height;
            }

            public void setWidth(int width) {
                this.width = width;
            }

            public int getWidth() {
                return this.width;
            }

            public int area() {
                return this.width * this.height;
            }
        }

위는 넓이와 높이를 가지는 Rectangle(직사각형) 클래스가 이며 Rectangle을 상속받는 Square(정사각형)를 만들어보자!

        public class Square extends Rectangle {
            @Override
            public void setHeight(int value) {
                this.width = value;
                this.height = value;
            }

            @Override
            public void setWidth(int value) {
                this.width = value;
                this.height = value;
            }
        }

위 코드와 같이 정사각형(Square)은 넓이와 높이가 같다. 이제 너비 4 높이 9로 설정하고 넓이를 확인하는 getArea() 함수의 값을 확인해보자!
    
    Rectangle r = new Rectangle();
    Rectangle r2 = new Square();
     
    r.setHeight(3);
    r.setWidth(4);
    
    r2.setHeight(3);
    r2.setWidth(4);
    
    assertThat(r.getArea()).isEqualTo(r2.getArea());
    
부모의 값(Rectangle)과 자식의 값(Square)이 다르게 나온다. 이는 LSP에 위배된다. 따라서, 부모클래스를 상속하는 자식클래스는 부모 클래스의 규약을 무시하거나 오버라이딩을 자제해야하는 것이 LSP이다. 


```부모 클래스와 자식 클래스 사이의 행위가 일관성 있어야 한다. LSP를 만족하면 프로그램에서 부모 클래스의 인스턴스 대신에 자식 클래스의 인스턴스로 대체해도 프로그램의 의미는 변화되지 않는다.```


LSP의 핵심은 자식 클래스가 항상 부모 클래스의 역할을 충실히 수행하는 것 이다.

### ISP (Interface Segregation Principle) 인터페이스 분리 원칙

    "클라이언트는 자신이 사용하지 않는 메서드에 의존 관계를 맺으면 안된다. - 로버트 C 마틴" 

ex) ISP 위반




    pulbic interface SmartDevice
    {
        void print();
        void fax();
        void scan();
    }

AllInOnePrinter는 복사, 팩스, 스캔의 모든 기능을 사용할 수 있다.

        public class AllInOnePrinter implement SmartDevice{
            @Override
            void print(){
                //can Print
            }
            @Override
            void fax(){
                //can Fax
            }
            @Override
            void scan(){
                //can Scan
            }
        }

EconomicPrinter는 복사기능만 사용한다.

        public class EconomicPrinter implement SmartDevice{
            @Override
            void print(){
                //can Print
            }
            @Override
            void fax(){
                throw new NotSupportedException();
            }
            @Override
            void scan(){
                throw new NotSupportedException();
            }
        }




![isp1](https://user-images.githubusercontent.com/68090443/178036203-b28dec75-be87-466e-a48d-e8c4238a42ca.PNG)


SmartDevice에 함수를 다 정의해놓고 의존하다 보니 EconomicPrinter같이 자신이 사용하지 않는 다른 메소드에도 의존하게 된다. EconomicPrinter같이 프린터 기능만 이용하는 클라이언트가 팩스 기능 및 스캔 기능의 변경으로 인해 발생하는 문제의 영향을 받지 않도록 해야한다. 위 코드를 좋은 예로 바꿔보자!


        pubilc interface Printer{
            void print();
        }

        interface Fax{
            void fax();
        }

        interface Scanner{
            void scan();
        }

EconomicPrinter

        public class EconomicPrinter implement Printer{
            @Override
            void print(){
                //can Print
            }
        }  
  
AllInOnePrinter

        public class AllInOnePrinter implement Printer, Fax, Scanner {
            @Override
            void print(){
                //can Print
            }
            @Override
            void fax(){
                //can Fax
            }
            @Override
            void scan(){
                //can Scan
            }
        }



![isp2](https://user-images.githubusercontent.com/68090443/178036245-5a277881-d26c-4505-bab7-f37e20869985.PNG)


AllInOnePrinter 클라이언트는 Printer, Fax, Scanner 인터페이스, EconomicPrinter 클라이언트는 Printer 인터페이스를 각자 클라이언트들은 자신이 관심을 갖는 메서드들만 있는 각각의 인터페이스로 정의하여 사용하도록 한다.

## DIP (Dependency Inversion Principle) 의존성 역전 원칙

    고수준 모듈은 저수준 모듈의 구현에 의존해서는 안 된다. 저수준 모듈이 고수준 모듈에서 정의한 추상 타입에 의존해야 한다.

즉 ```자신보다 변하기 쉬운 것에 의존하지 마라```

ex) 계산기

        public class Calculator
        {
            public double Add(double x, double y)
            {
                return x + y;
            }

            public double Subtract(double x, double y)
            {
                return x - y;
            }
        }

여기서 곱하기를 추가해보자!

        public class Calculator
        {
            public double add(double x, double y)
            {
                return x + y;
            }

            public double subtract(double x, double y)
            {
                return x - y;
            }
            
            public double multiply(double x, double y)
            {
                return x * y;
            }
        }

Calculator 클래스에 새 작업을 추가하면 현재 클래스가 수정됩니다. 이것은 OCP에 위배된다.. DIP를 사용해서 OCP를 지켜보자!
 
구체화된 클래스에 의존하는 것 보다 추상화된 클래스에 의존하게 하자!


        public interface CalculatorOperation
        {
            double Calculate(double x, double y);
        }


Add

        public class AddCalculatorOperation implements CalculatorOperation
        {
            @Override
            public double calculate(double x, double y)
            {
                return x + y;
            }
        }     
        
Subtract

        public class SubtractCalculatorOperation implements CalculatorOperation
        {
            @Override
            public double calculate(double x, double y)
            {
                return x - y;
            }
        }   

Multiply

        public class MultiplyCalculatorOperation implements CalculatorOperation
        {
            @Override
            public double calculate(double x, double y)
            {
                return x * y;
            }
        }

Calculator

        public class Calculator {

            private CalculatorOperation calculatorOperation;

            public Calculator(CalculatorOperation calculatorOperation)
            {
                this.calculatorOperation = calculatorOperation;
            }    

            public double Solve(double x, double y)
            {
                //계산은 주입된 CalculatorOperation을 따른다.
                return calculatorOperation.calculate(x, y);
            }

        }

만약 아래와 같이 나누기가 추가되어도 Calculator 클래스를 변경하지 않아도 된다.

        public class DivideCalculatorOperation implements CalculatorOperation
        {
            public double calculate(double x, double y)
            {
                return x / y;
            }
        }
        
test해보자!

        public class CalculatorTest
        {
            @Test
            public void 1+1=2()
            {
                Calculator calculator = new Calculator(new AddCalculatorOperation());
                double result = calculator.solve(1, 1);
                // Result is 2.
                assertThat(result).isEqualTo(2);
            }

            @Test
            public void 1-1=0()
            {
                Calculator calculator = new Calculator(new SubtractCalculatorOperation());
                double result = calculator.solve(1, 1);
                // Result is 0.
                assertThat(result).isEqualTo(0);
            }

            @Test
            public void 1*2=2()
            {
                Calculator calculator = new Calculator(new MultiplyCalculatorOperation());
                double result = calculator.solve(1, 2);
                // Result is 2.
                assertThat(result).isEqualTo(2);
            }

            @Test
            public void 10/5=2()
            {
                Calculator calculator = new Calculator(new DivideCalculatorOperation());
                double result = calculator.solve(10, 5);
                // Result is 2.
                assertThat(result).isEqualTo(2);
            }
        }
        
![dip1](https://user-images.githubusercontent.com/68090443/178033455-6947d5b6-9581-477a-828c-f7700b4e5325.PNG)

