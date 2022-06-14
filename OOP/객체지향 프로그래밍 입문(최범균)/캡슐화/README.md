최범균님의 인프런 강의를 학습한 내용을 기록했습니다.

# 캡슐화

- 데이터 + 관련 기능 묶는 것이다.
- 객체가 기능을 어떻게 구현했는지는 외부에서는 알 수 없다. 실제 구현에 사용된 데이터가 어떤 타입인지 그 데이터 값을 어떻게 사용하는지 등에 대한 것은 외부에서 알 수 없다.
- 정보 은닉(Information Hiding) 의미 포함


## 캡슐화를 하는 이유

    외부에 영향 없이 객체 내부 구현 변경 가능


### 캡슐화를 하지 않으면??


ex) 아래 코드는 membership이 REGULAR이면서 회원의 만료일이 현재 시간 이후라면 정회원의 기능을 실행한다. 

    if(account.getMembership() == REGULAR && account.getExpDate().isAfter(now())){
      ...정회원 기능
    }
    
  
시간이 7년이나 흘러 5년이상 서비스를 이용한 회원에게 정회원 혜택 1개월 무상 이벤트를 제공 하게되서 아래와 같이 코드가 변경하였다.

    if(account.getMembership() == REGULAR && 
       (
        (account.getServiceDate().isAfter(fiveYearAgo) && account.getExpDate().isAfter(now())) ||
        (account.getServiceDate().isBefore(fiveYearAgo) && addMonth(account.getExpDate()).isAfter(now())))
       )
    ){
      ...정회원 기능
    }
    
기존과 다르게 ServiceDate의 값을 사용하면서 ServiceDate의 값에 따라서 expDate를 사용하는 방식도 바뀌게 되었다. 이와 같은 조건(정회원 기능을 실행하는 로직)에 해당하는 모든 코드를 찾아서 수정해야한다. 즉 데이터를 사용하는 코드 A,B,C의 수정이 필요하다.


요구사항 예시

- 장기 사용자에게 특정 기능 실행 권한을 연장 (단, 유효 일자는 그대로 유지)
- 계정을 차단하면 모든 실행 권한이 없음
- Date를 LocalDateTime으로 변경

### 캡슐화를 한다면??

정회원인지 검사하는 기능을 하나의 객체로 묶는다.
    
        public class Account {

            private MemberShip memberShip;
            private LocalDate expDate;

            ...

            public boolean hasRegularPermission(){
                return memberShip == REGULAR && expDate.isAfter(LocalDate.now());
            }

            ...
        }
        
내부 구현은 바뀌었지만 hasRegularPermission()을 사용하는 코드는 바뀌지 않는다(요구 사항의 변화가 내부 구현을 변경).

        if(account.hasRegularPermission()){
            ..정회원 기능
        }

캡슐화를 잘해두면 요구사항이 변해도 코드가 변경되는 부분을 최소화할 수 있다.

### 캡슐화를 위한 규칙

#### ```1. Tell, Don’t Ask```

    데이터를 달라하지 말고 해달라고 하기


기존

    if(account.getMembership() == REGULAR && account.getExpDate().isAfter(now())){
          ...정회원 기능
    }
   
캡슐화 후

    if(account.hasRegularPermission()){
            ..정회원 기능
        }
        
기존 코드는 Account의 membership 값을 가져와 조건을 판단하고있다. 이보다는 캡슐화 후 코드 처럼 membership을 가지고 있는 객체인 Account에 처리를 맡겨 처리해라!!


#### ```2. Demeter's Law```

    노출 범위를 제한하기 위해 객체의 모든 메서드는 다음에 해당하는 메서드만을 호출해야 한다.
 
- 메서드에서 생성한 객체의 메서드만 호출
- 파라미터로 받은 객체의 메서드만 호출
- 필드로 참조하는 객체의 메서드만 호출

디미터법칙 위반
    
    ex1)  account.getServiceDate().isAfter(now())
    
    ex2)  Date date = account.getExpDate();
          date.isAfter(now());
    
개선

    1.  account.isExpired()
    
    2.  account.isValid(now())

개선된 코드와 같이 객체의 메서드만 호출하는것 이다.


## 정리

캡슐화 - 기능의 구현을 외부에 감춤

캡슐화를 통해 기능을 사용하는 코드에 영향을 주지 않고(또는 최소화) 내부 구현을 변경할 수 있는 유연함을 가지게 된다.

# 캡슐화 연습

## 캡슐화 연습 1

    public AuthResult authenticate(String id, String pw) {
      Member member = findOne(id);
      if (member == null) return AuthResult.NO_MATCH;

      if (member.getVerificationEmailStatus() != 2) {
          return AuthResult.NO_EMAIL_VERIFIED;
      }
      
      if (passwordEncoder.isPasswordVaild(member.getPassword(), pw, member.getId())) {
          return AuthResult.SUCCESS;
      }
      return AuthResult.NO_MATCH;
    }
    
위 코드는 인증과 관련된 코드로 아이디와 암호를 매개변수로 받으며 다음과정을 거친다.

1. Member를 아이디로 찾고 해당하는 맴버가 없으면 AuthResult.NO_MATCH를 리턴
2. 맴버의 verificationEmailStatus() 값이 2가 아니라면 AuthResult.NO_EMAIL_VERIFIED를 리턴
3. 유효한 암호이면 AuthResult.SUCCESS를 리턴

위 코드를 캡슐화하기 위해 적용할 수 있는 규칙은 'Tell, Don't Ask' 다.(데이터를 달라하지 말고 해달라고 하기)
    
    //캡슐화 진행 할 부분 코드
    if (member.getVerificationEmailStatus() != 2) {
          return AuthResult.NO_EMAIL_VERIFIED;
    }
   
    //캡슐화 후 코드(member에서 결과를 가져오도록 수정)  
    public class Member {
    
      private int verificationEmailStatus;
        
      ...
        
      public boolean isEmailVerified(){
          return verificationEmailStatus == 2;
      }
        
      ...
  
    }
    
    public AuthResult authenticate(String id, String pw) {
      Member member = findOne(id);
      if (member == null) return AuthResult.NO_MATCH;
      
      //캡슐화 적용
      if (member.isEmailVerified) {
          return AuthResult.NO_EMAIL_VERIFIED;
      }
      
      if (passwordEncoder.isPasswordVaild(member.getPassword(), pw, member.getId())) {
          return AuthResult.SUCCESS;
      }
      return AuthResult.NO_MATCH;
    }
        
        
## 캡슐화 연습 2
마틴 파울러의 리팩토링 책에 나오는 예제이다.

Movie

   
    public class Movie {
      //최신 영화 NEW_RELEASE, 일반 REGULAR
      public static int REGULAR = 0;
      public static int NEW_RELEASE = 1;
      private int priceCode;

      public int getPriceCode() {
        return priceCode;
      }
      ...
    }

Rental

    public class Rental {
      private Movie movie;
      private int daysRented;
      
      //최신 영화를 하루 이상 대여시 2포인트 획득 아니면 1포인트 회득.
      public int getFrequentRenterPoints() {
        if (movie.getPriceCode() == Movie.NEW_RELEASE && daysRented > 1)
          return 2;
        else
          return 1;
      }
      ...
    }
    
위 코드에 캡슐화를 적용하면

    movie.getPriceCode() == Movie.NEW_RELEASE 

Rental에서 Movie 객체에게 priceCode를 달라하고 있다 이 부분을 Movie에게 해달라고하자!
    
Movie

    public class Movie {
      //최신 영화 NEW_RELEASE, 일반 REGULAR
      public static int REGULAR = 0;
      public static int NEW_RELEASE = 1;
      private int priceCode;

      public boolen isNewRelease() {
        return priceCode == NEW_RELEASE;
      }
      ...
    }

Rental

      public int getFrequentRenterPoints() {
        if (movie.isNewRelease() && daysRented > 1)
          return 2;
        else
          return 1;
      }
      ...
    }

위 코드를 보면 먼가 아쉽다... 조건 전체를 Movie에 맡겨보자!

Movie

    public class Movie {
      //최신 영화 NEW_RELEASE, 일반 REGULAR
      public static int REGULAR = 0;
      public static int NEW_RELEASE = 1;
      private int priceCode;

      public int getFrequentRenterPoints(daysRented ) {
        if (if priceCode == NEW_RELEASE && daysRented > 1)
          return 2;
        else
          return 1;
      }
      ...
    }
    
Rantal

    public class Rental {
      private Movie movie;
      private int daysRented;
      
      //최신 영화를 하루 이상 대여시 2포인트 획득 아니면 1포인트 회득.
      public int getFrequentRenterPoints(){
        movie.getFrequentRenterPoints(daysRented)
      }
      ...
    }
    
이런식으로 캡슐화를 하면 포인트를 구하는 공식이 바뀐 경우 Movie 객체의 getFrequentRenterPoints의 코드만 변경하면 된다. 


    데이터를 들고 있는 쪽에 기능을 추가하며, 기능에 필요한 다른 값을 파라미터로 받는 예시이다!

## 캡슐화 연습 3

Timer

    public class Timer {
      public long startTime;
      public long stopTime;
    }
    
로직 실행시간 측정 코드

    Timer t = new Timer();
    t.startTime = System.currentTimeMillis();

    ...

    t.stopTime = System.currentTimeMillis(); 
    long elaspedTime = t.stopTime - t.startTime; 
    
위 코드는 Timer 클래스에 데이터를 가져다 사용하는 절차 지향적으로 작성되어있다. 위 코드에 캡슐화를 적용해 보자!

로직을 보면 시작시간을 구하고, 종료시간을 구하고, 마지막으로 소요시간을 구한다. 해당 기능을 Timer 객체로 묶어보자!

Timer

    public class Timer {
      public long startTime;
      public long stopTime;
      
      public void start(){
        this.startTime = System.currentTimeMillis();
      }
      
      public void stop(){
        this.stopTime = System.currentTimeMillis();
      }
      
      public long elapsedTime(TimeUnit unit){
        switch(unit){
            case MILLISECOND;
                return stop - startTime;
            .....
        }
      }
    }
    
데이터 클래스로 사용되던 Timer가 기능을 제공하는 객체로 바뀌었다. Timer를 캡슐화함으로써 측정 시간 단위를 millisecond에서 nanosecond로 변경하더라도 외부의 코드는 변경하지 않고 내부의 구현을 변경하면된다.
 
 
## 캡슐화 연습 4

데이터를 가지고 와서 판단한 후, 판단의 결과로 데이터를 다시 바꾸는 코드

    public void verifyEmail(String token) {
      Member mem = findByToken(token);
      if (mem == null) throw new BadTokenException();

      if (mem.getVerificationEmailStatus() == 2) {
        throw new AlreadyVerifiedException();
      } else {
        mem.setVerificationEmailStatus(2);
      }
      // .. 수정사항 DB 반영
    }
    
위 코드는 token으로 Member를 조회하고 조회한 Member의 VerificationEmailStatus가 2면 예외처리하고 아닐 경우 verificationEmailStatus 값을 2로 설정 후 db에 저장한다.

해당 코드를 캡슐화 해보자!


Member

    public class Member {
    
      private int verificationEmailStatus;
        
      ...
        
      public boolean isEmailVerified(){
          return verificationEmailStatus == 2;
      }
        
      ...
    }
    
verifyEmail 로직

    public void verifyEmail(String token) {
      Member mem = findByToken(token);
      if (mem == null) throw new BadTokenException();

      if (mem.isEmailVerified()) {
        throw new AlreadyVerifiedException();
      } else {
        mem.setVerificationEmailStatus(2);
      }
      // .. 수정사항 DB 반영
    }
    
객체의 값을 달라고하는 부분은 캡슐화 했지만 코드의 구조는 개선되지 않았다... 이러한 코드는 조건문을 통으로 캡슐화했을 때 개선될 가능성이 높아진다. 

코드를 개선해보자!

Member

    public class Member {
    
      private int verificationEmailStatus;
        
      ...
      
      public void verifyEmail(){
        if (isEmailVerified()) {
            throw new AlreadyVerifiedException();
        } else {   
            this.verificationEmailStatus = 2;
        }
      }
        
      public boolean isEmailVerified(){
          return verificationEmailStatus == 2;
      }
      ...
    }
    
verifyEmail 로직


    public void verifyEmail(String token) {
      Member mem = findByToken(token);
      if (mem == null) throw new BadTokenException();

      mem.verifyEmail();
      // .. 수정사항 DB 반영
    }
    
