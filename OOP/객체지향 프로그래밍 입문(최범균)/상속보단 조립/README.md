# 상속보단 조립

## 상속

상위 클래스의 기능을 재사용(상위 클래스의 public 또는 protected로 선언된 모든 변수와 메소드를 사용할 수 있다.), 확장하는 방법으로 활용

### 상속의 단점

'''상위 클래스 변경 어렵다'''

    - 상위 클래스를 조금만 변경해도 하위 클래스가 모두 영향을 받는다.
    - 하위 클래스는 기능 재사용을 위해 상위 클래스의 동작을 알고 있어야한다.
    - 상위 클래스는 하위 클래스에 대한 캡슐화가 약해질 수 있다.
 
 
```클래스 증가```

    - 새로운 조합이 생기면 하위 클래스가 증가한다.
    - 어떤 것을 상속 받아야 하는지 애매해진다.

```상속 오용```

    - 불필요한 기능까지 모두 상속되서 꼬일 수 있다.
    
    
ex) ArrayList를 상속받은 Container 클래스


    public class Container extends ArrayList<Luggage> {
      private int maxSize;
      private int currentSize;

      public Container(int maxSize) {
        this.maxSize = maxSize;
      }


      public void put(Luggage lug) throws NotEnoughSpaceException {
        if (!canContain(lug)) throw new NotEnoughSpaceException();
        super.add(lug);
        currentSize += lug.size();
      }

      public void extract(Luggage lug) {
        super.remove(lug);
        this.currentSize -= lug.size();
      }

      public boolean canContain(Luggage lug) {
        return maxSize >= currentSize + lug.size();
      }
    }


구현

   
    Luggage Size3Lug = new Luaggage(3)
    Luggage Size2Lug = new Luaggage(2)
    Luggage Size1Lug = new Luaggage(1)
    
    Container c = new Container(5);
    
    //정상사용
    if c.canContain(size3Luggage)){
      c.put(size3Luggage);
    }

 Container 클래스는 Luggage 목록을 관리하는 클래스이다. 목록 관리 기능은 직접 구현하지 않고 ArrayList를 상속받아서 구현하였다.
 
 문제는 
 
    Luggage size3Lug = new Luaggage(3)
    Luggage size2Lug = new Luaggage(2)
    Luggage size1Lug = new Luaggage(1)
    
    Container c = new Container(5);
    

    if c.canContain(size3Lug)){
      c.put(size2Luggage); //정상사용 -> 컨테이너 여분이 2로 줄어듬
    }
    
    if c.canContain(size2Lug)){
      c.add(size2Luggage); //비정상 사용 -> 컨터에너 여분이 줄지 아늠
    }

    if c.canContain(size2Lug)){
      //통과되면 안되지만 통과되서 로직을 탄다...
      c.put(size2Luggage);
    }
 
 상위클래스의 메소드를 사용할 경우 가용량이 줄지 않아 무한정 컨테이너에 넣게된다..
 
 
 ## 조립
