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

"""Tell, Don’t Ask"""

    데이터를 달라하지 말고 해달라고 하기



