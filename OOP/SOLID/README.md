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

 소프트웨어 요소는 확장에는 열려있고 변경에는 닫혀있어야한다. 
 클래스는 확장에는 개방적이어야 하고, 변경에는 폐쇄적이어야 한다.

확장을 하는데 어떻게 코드를 변경하지 않을까??? ```인터페이스 안에 필요 기능을 작성한다면 인터페이스를 구현하는 구현클래스는 다형성을 통해서 새로운 기능의 확장이 가능하다.```




