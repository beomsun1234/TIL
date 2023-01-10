# 브릿지 패턴 (Bridge Pattern)

 큰 클래스 또는 밀접하게 관련된 클래스들의 집합을 두 개의 개별 계층구조(추상화 및 구현)로 나눈 후 각각 독립적으로 개발할 수 있도록 하는 구조 디자인 패턴입니다.

Circle​(원) 및 Square​(직사각형)​라는 한 쌍의 자식 클래스들이 있는 기하학적 Shape​(모양) 클래스가 있다고 가정해 봅시다. 이 클래스 계층 구조를 확장하여 색상을 도입하기 위해 Red​(빨간색) 및 Blue​(파란색) 모양들의 자식 클래스들을 만들 계획입니다. 그러나 이미 두 개의 자식 클래스가 있으므로 Blue­Circle​(파란색 원) 및 Red­Square​(빨간색 직사각형)​와 같은 네 가지의 클래스 조합을 만들어야 합니다.

![image](https://user-images.githubusercontent.com/68090443/211506695-13b7ea01-5d7a-4b23-9f42-c1951fc9baa3.png)

새로운 모양 유형들과 색상 유형들을 추가할 때마다 계층 구조는 기하급수적으로 성장합니다. 예를 들어, 삼각형 모양을 추가하려면 각 색상별로 하나씩 두 개의 자식 클래스들을 도입해야 합니다. 그리고 그 후에 또 새 색상을 추가하려면 각 모양 유형별로 하나씩 세 개의 자식 클래스를 만들어야 합니다. 유형들이 많아지면 많아질수록 코드는 점점 복잡해집니다.

![image](https://user-images.githubusercontent.com/68090443/211506914-127d18eb-e3d6-44ed-8a96-3989a7aaac51.png)


        브리지 패턴은 상속에서 객체 합성으로 전환하여 이 문제를 해결하려고 시도합니다.



![image](https://user-images.githubusercontent.com/68090443/211006915-30f8b50d-761c-4665-ba2e-14dbb4bd346e.png)



UML diagram

![image](https://user-images.githubusercontent.com/68090443/211007021-a2830d6a-630f-4c32-8ac9-18cfe528345e.png)




## code

Color
        

    public interface Color {

      public void applyColor();
    }


RedColor 


    public class RedColor implements Color{

      public void applyColor(){
        System.out.println("red.");
      }
    }


GreenColor 



    public class GreenColor implements Color{

      public void applyColor(){
        System.out.println("green.");
      }
    }



Shape 



    public abstract class Shape {
      //Composition - implementor
      protected Color color;

      //constructor with implementor as input argument
      public Shape(Color c){
        this.color=c;
      }

      abstract public void applyColor();
    }



Triangle
    
    
    
    public class Triangle extends Shape{

      public Triangle(Color c) {
        super(c);
      }

      @Override
      public void applyColor() {
        System.out.print("Triangle filled with color ");
        color.applyColor();
      } 

    }   



Pentagon



    public class Pentagon extends Shape{

      public Pentagon(Color c) {
        super(c);
      }

      @Override
      public void applyColor() {
        System.out.print("Pentagon filled with color ");
        color.applyColor();
      } 

    } 


Client


      public class Client {
        public static void main(String[] args) {
          Shape tri = new Triangle(new RedColor());
          tri.applyColor();

          Shape pent = new Pentagon(new GreenColor());
          pent.applyColor();
        }
      }
