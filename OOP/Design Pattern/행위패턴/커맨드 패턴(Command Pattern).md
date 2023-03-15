# 커맨드 패턴(Command Pattern)


특정 작업을 수행하는 객체와 이 객체를 호출하는 객체 사이의 관계를 정의 합니다. 

보통 시스템에서 특정 기능을 수행하는 메서드를 직접 호출하는 것보다, Command Pattern을 사용하면 이 기능을 수행하는 객체를 캡슐화하고, 호출하는 객체와 수행하는 객체 간의 결합도를 낮출 수 있습니다. 



Command Pattern의 핵심 요소는 "Command" 인터페이스입니다. 이 인터페이스는 수행될 작업을 정의하는 execute() 메서드를 포함하고 있습니다. 이 인터페이스를 구현한 구체적인 Command 클래스는 특정 작업을 수행하는 객체입니다.

호출하는 객체는 Command 인터페이스를 이용하여 특정 Command 객체를 생성하고, 이 객체를 사용하여 작업을 수행합니다. 이를 통해 호출하는 객체는 실제 작업을 수행하는 객체와 간접적으로 상호작용하게 되며, 이를 통해 호출하는 객체는 작업을 수행하는 객체의 내부 구현 상세를 알 필요가 없습니다.




ex) 불을 끄고 

    Command: 작업을 실행하기 위한 인터페이스를 정의합니다. 여기에는 ConcreteCommand에 의해 구현되는 execute() 메서드가 포함됩니다.
    
    ConcreteCommand: Command 인터페이스의 execute() 메서드를 구현합니다. Receiver 개체와 수행할 작업 간의 바인딩을 정의합니다.
    
    Receiver: ConcreteCommand의 execute() 메서드 호출 시 액션을 수행하는 객체.

### 코드
    public interface Command {
        void execute();
    }

    // Concrete command
    public class LightOnCommand implements Command {
        private Light light;

        public LightOnCommand(Light light) {
            this.light = light;
        }

        @Override
        public void execute() {
            light.turnOn();
        }
    }

    // Receiver
    public class Light {
        public void turnOn() {
            System.out.println("The light is on");
        }

        public void turnOff() {
            System.out.println("The light is off");
        }
    }

    // Client
    public class RemoteControl {
        private Command command;

        public void setCommand(Command command) {
            this.command = command;
        }

        public void pressButton() {
            command.execute();
        }
    }

    // Usage
    public static void main(String[] args) {
        RemoteControl remoteControl = new RemoteControl();

        Light light = new Light();
        LightOnCommand lightOnCommand = new LightOnCommand(light);

        remoteControl.setCommand(lightOnCommand);
        remoteControl.pressButton();
    }











