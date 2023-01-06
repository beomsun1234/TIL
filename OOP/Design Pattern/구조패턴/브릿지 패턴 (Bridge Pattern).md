# 브릿지 패턴 (Bridge Pattern)


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
