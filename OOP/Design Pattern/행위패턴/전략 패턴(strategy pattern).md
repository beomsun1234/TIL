# 전략 패턴 (strategy pattern)

"The strategy pattern is a behavioral software design pattern
that enables selecting an algorithm at runtime."

해석하면 전략패턴은 런타임 시점에 알고리즘을 선택할 수 있게 해주는 행동 패턴이다.

행위를 클래스로 캡슐화해 동적으로 행위를 자유롭게 바꿀 수 있게 해준다. 

  - 같은 문제를 해결하는 여러 알고리즘이 클래스별로 캡슐화되어 있고 이들이 필요할 때 교체할 수 있도록 함으로써 동일한 문제를 다른 알고리즘으로 해결할 수 있게 하는 디자인 패턴


## 스트리트파이터 게임을 만든다고 가정해보자!

[https://www.geeksforgeeks.org/strategy-pattern-set-1/]

단순하게 캐릭터들은 킥, 펀치, 점프 3가지 동작만 한다고 가정하고 Fighter 클래스를 만들어보자!

    public abstract class Fighter {

      public abstract void display();
      public abstract void kick();
      public abstract void jump();

      public void punch()
      { 
         System.out.println("Default Punch");
      }
    }


켄

    public class Ken extends Fighter {

      @Override
      public void display(){
        System.out.println("나는 켄");
      }
      @Override
      public void kick(){
        .......
      }
      @Override
      public void jump(){
        .....
      }
    }

류

    public class Ryu extends Fighter {

      @Override
      public void display(){
        System.out.println("나는 류");
      }
      @Override
      public void kick(){
        .......
      }
      @Override
      public void jump(){
        .....
      }
    }

춘리

    public class ChunLi extends Fighter {

      @Override
      public void display(){
        System.out.println("나는 춘리");
      }
      @Override
      public void kick(){
        .......
      }
      @Override
      public void jump(){
        .....
      }
    }


켄, 류, 춘리가 있다고 하면 Fighter를 상속받아 구현하게 된다. 


만약 시간이 흘러 켄이 킥이나 점프를 하지 않는다면?? 켄이 킥이나 점프를 할 수 없도록 코드를 수정하면 됩니다. 하지만 만약 점프나 킥을 하지 않는 다른 캐릭터들이 만들어진다면?? 해당 캐릭터들에서 이를 처리해야 해서 유지보수를 어렵게 합니다. 

리팩토링을 진행해 봅시다! 

우선 Fighter 클래스에서 일부 캐릭터가 수행하지 않을 수 있는 킥과 점프 메소드를 제거하고 인터페이스로 만들어 봅시다!

Fighter
  
    public abstract class Fighter {

      public abstract void display();
   
      public void punch()
      { 
         System.out.println("Default Punch");
      }
    }

Jump

    public interface Jump{
      public void jump();
    }

Kick

    public interface kick{
      public void kick();
    }
  
켄은 점프를 하지 못한다.

켄

    public class Ken extends Fighter implements Kick  {

      @Override
      public void display(){
        System.out.println("나는 켄");
      }
      @Override
      public void kick(){
        .......
      }
     
    }

류

    public class Ryu extends Fighter implements Kick, Jump {

      @Override
      public void display(){
        System.out.println("나는 류");
      }
      @Override
      public void kick(){
        .......
      }
      @Override
      public void jump(){
        .....
      }
    }

춘리

    public class ChunLi extends Fighter implements Kick, Jump {

      @Override
      public void display(){
        System.out.println("나는 춘리");
      }
      @Override
      public void kick(){
        .......
      }
      @Override
      public void jump(){
        .....
      }
    }

이렇게 구현하면 킥이나 점프를 할 수 있는 캐릭터들만 킥이나 점프를 구현하면 됩니다! 하지만 위 디자인에는 문제점이 있습니다.. 바로 코드의 재사용 입니다. 점프와 킥 동작에 기본 구현이 없기 때문에 많은 하위 클래스에서 동일한 동작의 점프를 계속해서 다시 작성해야 할 수 있습니다.. 

전략 패턴을 사용해서 리팩토링 해 봅시다! 

    1. 알고리즘 제품군을 정의하고
    2. 각 알고리즘을 캡슐화하고
    3. 해당 제품군 내에서 알고리즘을 교환할 수 있습니다.

현재 점프는 짧은 점프, 긴 점프, 점프x 3가지 방식이 있고 킥은 토네이도킥, 번개 킥 두가지 방식이 있습니다. 

점프는 jumpBehavior, kickBehavior 인터페이스를 만들어 줍니다.

jump

    interface JumpBehavior
    {
        public void jump();
    }

짧은 점프

    class ShortJump implements JumpBehavior
    {
        public void jump()
        {
            System.out.println("Short Jump");
        }
    }

긴 점프

    class LongJump implements JumpBehavior
    {
        public void jump()
        {
            System.out.println("Long Jump");
        }
    }

점프 못함


    class NoJump implements JumpBehavior
    {
        public void jump()
        {
            System.out.println("No Jump");
        }
    }

kick

    interface KickBehavior
    {
        public void kick();
    }


번개킥

    class LightningKick implements KickBehavior
    {
        public void kick()
        {
            System.out.println("Lightning Kick");
        }
    }
    
토네이도킥

    class TornadoKick implements KickBehavior
    {
        public void kick()
        {
            System.out.println("Tornado Kick");
        }
    }
    
Fighter 클래스는 해당 전략들을 상속받지 않고 조립해서 사용한다.(다중상속 방지)

    public abstract class Fighter {
      
      private KickBehavior kickBehavior;
      private JumpBehavior jumpBehavior;
      
      public Fighter(KickBehavior kickBehavior,
                   JumpBehavior jumpBehavior){
        this.jumpBehavior = jumpBehavior;
        this.kickBehavior = kickBehavior;
      } 
      
      public void setKickBehavior(KickBehavior kickBehavior){
        this.kickBehavior = kickBehavior;
      }
      
      public void setJumpBehavior(JumpBehavior jumpBehavior){
        this.jumpBehavior = jumpBehavior;
      }      
      
      public abstract void display();
      
      public void punch() {
        System.out.println("Default Punch");
      } 
      
      public void kick() {
        //delegate to kick behavior
        kickBehavior.kick();
      }
      
      public void jump() {
        //delegate to jump behavior
        jumpBehavior.jump();
      }
    }
 
류

    public class Ryu extends Fighter {

        public Ryu(KickBehavior kickBehavior,
                   JumpBehavior jumpBehavior){
            super(kickBehavior,jumpBehavior);
        }
        public void display() {
            System.out.println("Ryu");
        }
    }


켄


    class Ken extends Fighter {

        public Ken(KickBehavior kickBehavior,
                   JumpBehavior jumpBehavior) {
            super(kickBehavior,jumpBehavior);
        }
        public void display() {
            System.out.println("Ken");
        }
    }

춘리 

    class ChunLi extends Fighter {

        public ChunLi(KickBehavior kickBehavior,
                      JumpBehavior jumpBehavior) {
            super(kickBehavior,jumpBehavior);
        }
        public void display() {
            System.out.println("ChunLi");
        }
    }

위처럼 Fighter는 행동을 구현하는 대신 킥,과 점프를 kickBehavior, jumpBehavior이라는 전략에 위임합니다.

public class StreetFighter
{
    public static void main(String args[])
    {
        Fighter ken = new Ken(new TornadoKick(), new LongJump());
        ken.display();
        // Test behaviors
        ken.punch();
        ken.kick();
        ken.jump();
        // 켄이 롱 점프에서 -> 점프를 못하게 밸런스 조절
        ken.setJumpBehavior(NoJump);
        ken.jump();
    }
}

전략 패턴을 사용하면 위 코드처럼 기존 코드에 영향을 주지 않고 행동을 중간에 변경할 수 있습니다. 프로그램 상으로 로직이 변경되거나 추가 되었을 때, 유연하게 대처 할 수 있습니다.
