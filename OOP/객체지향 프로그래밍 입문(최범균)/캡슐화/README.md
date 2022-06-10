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

## 캡슐화 연습1

    public AuthResult authenticate(String id, String pw) {
      Member mem = findOne(id);
      if (mem == null) return AuthResult.NO_MATCH;

      if (mem.getVerificationEmailStatus() != 2) {
          return AuthResult.NO_EMAIL_VERIFIED;
      }
      
      if (passwordEncoder.isPasswordVaild(mem.getPassword(), pw, mem.getId())) {
          return AuthResult.SUCCESS;
      }
      return AuthResult.NO_MATCH;
    }
    
위 코드는 인증과 관련된 코드로 아이디와 암호를 매개변수로 받으며 다음과정을 거친다.

1. 아이디에 해당하는 맴버가 없으면 AuthResult.NO_MATCH를 리턴
2. 맴버의 verificationEmailStatus() 값이 2가 아니라면 AuthResult.NO_EMAIL_VERIFIED를 리턴
3. 유효한 암호이면 AuthResult.SUCCESS를 리턴

위 코드에 캡슐화를 적용해보자!

위 코드를 캡슐화하기 위해 적용할 수 있는 규칙은 'Tell, Don't Ask' 다.(데이터를 달라하지 말고 해달라고 하기)

    if (member.getVerificationEmailStatus() != 2) {
          return AuthResult.NO_EMAIL_VERIFIED;
    }
