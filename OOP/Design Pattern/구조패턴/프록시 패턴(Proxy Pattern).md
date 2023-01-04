# 프록시 패턴(Proxy Pattern)


    어떤 다른 객체로 접근하는 것을 통제하기 위해서 그 객체의 대리자(surrogate)나 자리표시자(placeholder)의 역할을 하는 객체를 제공하는 패턴입니다.



[사진](https://limkydev.tistory.com/79)


프록시(Proxy)를 번역하면 대리자, 대변인의 의미를 갖고 있습니다. 대리자, 대변인은 누군가를 대신해서 그 역할을 수행하는 존재입니다. 
프로그램에서 봤을 때도 똑같습니다. 프록시에게 어떤 일을 대신 시키는 것입니다. 

구체적으로 인터페이스를 사용하고 실행시킬 클래스에 대한 객체가 들어갈 자리에 대리자 객체를 대신 투입해 클라이언트 쪽에서 실제  실행시킬 클래스에 대한객체를 통해 메서드를 호출하고 반환 값을 받는지, 대리자 객체를 통해 메서드를 호출하고 반환 값을 받는지 전혀 모르게 처리하는 것입니다.

중요한 것은 흐름제어만 할 뿐 결과값을 조작하거나 변경시키면 안됩니다.

어떤 객체를 사용하고자 할때, 객체를 직접적으로 참조하는 것이 아닌 해당 객체를 대항하는 객체를 통해 대상 객체에 접근하는 방식을 사용하면 해당 객체가 메모리에 존재하지 않아도 기본적인 정보를 참조하거나 설정할 수 있고, 실제 객체의 기능이 필요한 시점까지 객체의 생성을 미룰 수 있습니다.

예를 들어, 우리가 시스템 명령어를 실행하는 객체를 갖고 있을 때 우리가 그 객체를 사용하는 것이라면 괜찮지만 만약 그 객체를 클라이언트에게 제공하려고 한다면 클라이언트 프로그램이 우리가 원치 않는 파일을 삭제하거나 설정을 변경하는 등의 명령을 내릴 수 있기 때문에 심각한 문제를 초래할 수 있습니다.

프록시 패턴은 클라이언트에게 접근에 대한 컨트롤을 제공하여 위와 같은 문제를 해결합니다.

## ex) 1

명령을 실행하는 CommandExecutor 인터페이스 정의

CommandExecutor.java

    public interface CommandExecutor {

        public void runCommand(String cmd) throws Exception;
    }

CommandExecutor를 구현한 클래스인 CommandExecutorImpl


    public class CommandExecutorImpl implements CommandExecutor {

      @Override
      public void runCommand(String cmd) throws IOException {
        //some heavy implementation
        Runtime.getRuntime().exec(cmd);
        System.out.println("'" + cmd + "' command executed.");
      }

    }
    
    
이제 우리는 admin 사용자에게만 위의 클래스에 대한 전체 액세스 권한을 제공하려고 합니다.

이를 위해 프록시 객체를 두어 Admin 사용자가 아닐 경우에는 rm 이라는 명령어에 대해 수행하지 못하도록 구현해보도록 하겠습니다.

CommandExecutorProxy

    public class CommandExecutorProxy implements CommandExecutor {

      private boolean isAdmin;
      private CommandExecutor executor;

      public CommandExecutorProxy(String user, String pwd){
        if("BeomSun".equals(user) && "admin_pwd".equals(pwd)) {
          isAdmin=true;
        }
        executor = new CommandExecutorImpl();
      }

      @Override
      public void runCommand(String cmd) throws Exception {
        if(isAdmin){
          executor.runCommand(cmd);
        }else{
          if(cmd.trim().startsWith("rm")){
            throw new Exception("rm command is not allowed for non-admin users.");
          }else{
            executor.runCommand(cmd);
          }
        }
      }
    }



Client

        public class ProxyPatternTest {

            public static void main(String[] args){
                CommandExecutor executor = new CommandExecutorProxy("BeomSun", "admin_pwd");
                try {
                    executor.runCommand("ls -ltr");
                    executor.runCommand("rm -rf abc.pdf");
                } catch (Exception e) {
                    System.out.println("Exception Message::"+e.getMessage());
                }	
            }
        }

클라이언트 코드에서 보았듯 클라이언트에서 직접 CommandExecutorImpl 클래스에 직접 접근하지 않고 CommandExecutorProxy에서 객체를 생성하여 권한에 따라 명령어를 수행하도록 했다.

프록시 패턴은 이렇듯 어떤 객체에 대하여 접근할 때에 Wrapper Class를 두어 접근에 대한 통제(Control access)를 위해 사용합니다.

## ex) 특정 주소에 접근 금지


InternetAccess 


    public interface InternetAccess {  
        public void connectTo() throws Exception;
    }  
    
    
InternetAccessService


    public class InternetAccessService implements InternetAccess {  
        private String siteAddress;  
        
        public InternetAccessService(String siteAddress) {  
            this.siteAddress = siteAddress;  
        }  
  
        @Override  
        public void connectTo() {  
            System.out.println("Connecting to "+ this.siteAddress);  
        }  
    }  
    
    
ProxyInternetAccessService


    public class ProxyInternetAccessService implements InternetAccess {  
        private String siteAddress;  
        
        private InternetAccessService  realInternetAccessService;  
        
        private static List<String> bannedSites;
        
        public ProxyInternetAccessService(String siteAddress) {
            this.siteAddress = siteAddress
        }
        
        static
        {
            bannedSites = new ArrayList<String>();
            bannedSites.add("abc.com");
            bannedSites.add("def.com");
            bannedSites.add("ijk.com");
            bannedSites.add("lnm.com");
        }
        
        @Override  
        public void connectTo() {  
            if(bannedSites.contains(siteAddress.toLowerCase())) {
                throw new Exception("Access Denied");
            }
            realInternetAccessService = new InternetAccessService(this.siteAddress)
            realInternetAccessService.connectTo()
        }  
    }      
    
    
Client

    public class Client
    {
        public static void main (String[] args)
        {
            Internet internet = new ProxyInternetAccessService("beomsun.kro.kr");
            Internet internet2 = new ProxyInternetAccessService("abc.com");
            try
            {
                internet.connectTo()
                internet2.connectTo()
            }
            catch (Exception e)
            {
                System.out.println(e.getMessage());
            }
        }
    }
    

## 참고

- https://www.digitalocean.com/community/tutorials/proxy-design-pattern
- https://www.geeksforgeeks.org/proxy-design-pattern/
- https://readystory.tistory.com/m/132
- https://www.geeksforgeeks.org/proxy-design-pattern/
- https://www.javatpoint.com/proxy-pattern
