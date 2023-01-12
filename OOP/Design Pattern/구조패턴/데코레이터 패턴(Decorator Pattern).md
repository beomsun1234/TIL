# 데코레이터 패턴(Decorator Pattern)

객체들을 새로운 행동들을 포함한 특수 래퍼 객체들 내에 넣어서 위 행동들을 해당 객체들에 연결시키는 구조적 디자인 패턴입니다. 즉 객체의 결합을 통해 기능을 동적으로 유연하게 확장 할 수 있게 해주는 패턴이다. 

ex1)


![image](https://user-images.githubusercontent.com/68090443/212064000-096b679b-bb39-4df2-9e1c-f4d39cadbb81.png)




Shape


    public interface Shape {
       void draw();
    }
    

Rectangle


    public class Rectangle implements Shape {

       @Override
       public void draw() {
          System.out.println("Shape: Rectangle");
       }
    }
    
Circle

    public class Circle implements Shape {

       @Override
       public void draw() {
          System.out.println("Shape: Circle");
       }
    }
    
ShapeDecorator

    public abstract class ShapeDecorator implements Shape {
       protected Shape decoratedShape;

       public ShapeDecorator(Shape decoratedShape){
          this.decoratedShape = decoratedShape;
       }

       public void draw(){
          decoratedShape.draw();
       }	
    }
    
RedShapeDecorator

    public class RedShapeDecorator extends ShapeDecorator {

       public RedShapeDecorator(Shape decoratedShape) {
          super(decoratedShape);		
       }

       @Override
       public void draw() {
          decoratedShape.draw();	       
          setRedBorder(decoratedShape);
       }

       private void setRedBorder(Shape decoratedShape){
          System.out.println("Border Color: Red");
       }
    }

Client

    public class Client {
       public static void main(String[] args) {

          Shape circle = new Circle();

          Shape redCircle = new RedShapeDecorator(new Circle());

          Shape redRectangle = new RedShapeDecorator(new Rectangle());
          System.out.println("Circle with normal border");
          circle.draw();

          System.out.println("\nCircle of red border");
          redCircle.draw();

          System.out.println("\nRectangle of red border");
          redRectangle.draw();
       }
    }
    
결과

    Circle with normal border
    Shape: Circle

    Circle of red border
    Shape: Circle
    Border Color: Red

    Rectangle of red border
    Shape: Rectangle
    Border Color: Red
