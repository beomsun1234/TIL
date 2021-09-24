## ```간편송금을 위한 테이블 설계```

<br>

### ```1. Member```

|구분|데이터타입|길이|내용|비고|
|------|---|---|------|---|
|```MEMBER_ID(PK)```|NUMERIC|(10,0)|0000000001|자동증가( identity)  PK|
|MEMBER _NAME|VARCHAR|10|박oo|외국인도 등록할수 있기에 varchar로 설정 not null|
|MEMBER _PHONE|CHAR|11|01012345678|not null|
|ENT_DATE|DATETIME|||not null|
|MOD_DATE|DATETIME||||



<br>


### ```2. ACCOUNT```



|구분|데이터타입|길이|내용|비고|
|------|---|---|------|---|
|```ACCOUNT_NUM(PK)```|CHAR|11|12345678901|11자리 계좌번호 PK|
|ACCOUNT_TYPE|CHAR|1|S|S-적금,  W-월급,  D–입출금, U-공과금 not null|
|ACCOUNT_ENT_DATE|DATETIME|||not null|
|ACCOUNT_EXP_DATE|DATETIME|||not null|
|AVAILABLE_BALANCE|NUMERIC|(13,0)||한도 not null|
|ACTIAL_BALANCE|NUMERIC|(13,0)||전체 금액 not null|
|STATE|CHAR|1|Y|주계좌 – Y, 정지 – N, 나머지 - A not null|
|SECRET_NUM|CHAR|4||계좌비밀번호 숫자 4자리 not null|
|```MEMBER_ID(FK)```|NUMERIC|(10,0)||FK


<br>

### ```3. BANk_TRANSACTION```

|구분|데이터타입|길이|내용|비고|
|------|---|---|------|---|
|```TRANS_ID(PK)```|CHAR|11||UUID 사용하여 겹치지 않게|
|TRANS_DATE|DATETIME|11||거래 일자 (index) 거래일자 조회|
|TRANS_BALANCE|NUMERIC|(13,0)||거래 금액|
|TRANS_TYPE|CHAR|1||W-출금, D-입금 (송금-> 출금 + 입금)|
|TRANS_ACCOUNT_NUM|CHAR|11||거래할 계좌|
|ACCOUNT_CUR_BALANCE|NUMERIC|(13,0)||거래 후 잔액|
|```ACCOUNT_NUM(FK)```|CHAR|11||내 계좌|
