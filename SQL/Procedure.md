## 프로시저 사용


사내 DB교욱시간에 프로시저이론을 들었다... 이걸 내것으로 만들기 위해 나만의 테이블을 설계하고 이를 이용해 프로시저를 만들어보았다.


- 프로시저를 왜 사용하나?

  - DB 보안 향상


        - 자체 보안 설정 기능을 통해 단위 실행 권한을 부여할 수 있음. 읽기, 수정, 특정 컬럼에 대한 권한 설정 등 세밀한 권한 제어 가능하다. 
        - ex) 외주 업체가 와서 개발할시 OO정보, OO기록 등 중요한 정보가 들어있는 테이블의 특정 컬럼을 삭제하거나, 수정할 수 없도록 SELECT 기능만 부여  

     <br>



  - 기능 추상화.
    
        -어떤 어플리케이션을 사용하더라도 SP를 이용한다면, 값 추출하는데 용의


      <br>   
  - 네트워크 소요 시간 절감.

    
        만약 동일한 쿼리를 100, 200번씩 호출한다면, 서버에서 100, 200번 호출하는 것 보다, DB단에서 100, 200번 호출해서 결과물을 출력하면 소요 시간을 줄일 수 있다.

     <br>

  - 성능개선
    
        실행계획을 미리 저장해 두기에 빠르다.

        하나의 요청으로 여러 SQL문을 실행 할 수 있습니다.

     <br>
  - 절차적 기능 구현
    

        SQL 쿼리는 절차적 기능 제공하지 않지만, SP는 IF, While과 같은 제어문 허용

     <br>


- 단점

- 낮은 처리 성능

    
        문자, 숫자열 연산에 SP를 사용하면 오히려 c, java보다 느린 성능을 보일 수 있음

 

- 유지 보수 어려움

        설치, 배포, 버전 관리등이 어려움

        -> 반대로 서버 재기동이 필요 없고 SP만 수정하면 관리되는 측면은 장점이 됨



- 디버깅이 어렵습니다


- DB 확장이 매우 힘듭니다.

        서비스 사용자가 많아져 서버수를 늘려야할 때, DB 수를 늘리는 것이 더 어렵습니다.
        
        서비스 확장을 위해 서버수를 늘릴경우 DB 수를 늘리는 것보다 WAS의 수를 늘리는 것이 더 효율적이기 때문에 대부분의 개발에서 DB에는 최소의 부담만 주고 대부분의 로직은 WAS에서 처리할 수 있게 합니다.





----------------
```실습```



### ```1.프로시저 생성(user의 계좌별 월별 거래금액(입금, 출금)합계)```

      
         create procedure proc_member_month_trans_sum
         ( @as_member_id numeric(10) , @as_account_num char(11) , @ad_fdate datetime, @ad_edate datetime )

         AS

         BEGIN
            SELECT A.ACCOUNT_NUM, B.MEMBER_NAME AS 'ACCOUNT_OWNER', SUM(C.TRANS_BALANCE) AS '거래금액'
            FROM PBS_ACCOUNT A,
                  PBS_MEMBER  B,
                  PBS_BANK_TRANSACTION C
            WHERE A.MEMBER_ID = B.MEMBER_ID
               AND A.ACCOUNT_NUM = C.ACCOUNT_NUM
               AND A.ACCOUNT_NUM = @as_account_num
               AND B.MEMBER_ID = @as_member_id
               AND C.TRANS_DATE BETWEEN @ad_fdate AND @ad_edate
            GROUP BY A.ACCOUNT_NUM, B.MEMBER_NAME
         END;

- ### ```실행``` ###   

   ```12345678903계좌번호를 가지고있는 유저의 8월 거래금액``` 
      
         exec proc_member_month_trans_sum @as_member_id = 3, @as_account_num = '12345678903', @ad_fdate = '2021-08-01 00:00:00', @ad_edate = '2021-08-31 23:59:59';

   ```12345678903계좌번호를 가지고있는 유저의 9월 거래금액```

         exec proc_member_month_trans_sum @as_member_id = 1, @as_account_num = '12345678901', @ad_fdate = '2021-09-01 00:00:00', @ad_edate = '2021-09-30 23:59:59';


-----
<br>

### ```2.프로시저 생성(admin-> 모든계좌 월별 거래금액(입금 or 출금)합계) ///type-> D = 입금, W=출금```

      create procedure proc_trans_month_sum_all (@ad_fdate datetime , @ad_edate datetime, @as_type char(1))

      AS

      BEGIN
         SELECT SUM(TRANS_BALANCE)
            FROM PBS_BANK_TRANSACTION
         WHERE TRANS_DATE BETWEEN @ad_fdate AND @ad_edate
            AND TRANS_TYPE = @as_type
      END;


- ### ```실행``` ###  

```은행의 8월 입금 금액 합계 ```

      exec proc_trans_month_sum_all @ad_fdate = '2021-08-01 00:00:00', @ad_edate ='2021-08-31 23:59:59', @as_type = 'D';

``` 8월 출금 금액 합계 ```

      exec proc_trans_month_sum_all @ad_fdate = '2021-08-01 00:00:00', @ad_edate ='2021-08-31 23:59:59', @as_type = 'W';

``` 9월 입금 금액 합계 ```

      exec proc_trans_month_sum_all  @ad_fdate = '2021-09-01 00:00:00', @ad_edate='2021-09-30 23:59:59', @as_type = 'D';

``` 9월 입금 금액 합계 ```

      exec proc_trans_month_sum_all  @ad_fdate = '2021-09-01 00:00:00', @ad_edate='2021-09-30 23:59:59', @as_type = 'W';