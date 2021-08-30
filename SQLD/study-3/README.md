## SQL 기본


- ```SQL``` : 관계형 DB에서 데이터 정의, 조작, 제어를 위
해 사용하는 언어

### ```SQL 문장들의 종류```
 - ```DML``` : SELECT, INSERT, UPDATE, DELETE 등 데
이터 조작어
 - ```DDL``` : CREATE, ALTER, DROP, RENAME 등 데이
터 정의어
 - ```DCL``` : GRANT, REVOKE 등 데이터 제어어
 - ```TCL``` : COMMIT, ROLLBACK 등 트랜잭션 제어어


### ```테이블 생성```
    CREATE TABLE 테이블이름 (
    );
- 테이블 명은 다른 테이블의 이름과 중복되면 안 된다. 테이블 내의 칼럼명은 중복될 수 없다. 
- 각 칼럼들은 , 로 구분되고 ; 로 끝난다. 칼럼 뒤에 데이터 유형은 꼭 지정되어야 한다. 
- 테이블명과 칼럼명은 반드시 문자로 시작해야한다. A-Z,a-z,0-9,_,$,#만 사용 가능
- DATETIME 데이터 유형에는 별도로 크기를 지정x


### ```제약조건```

    1. PRIMARY KEY(기본키) : 기본키 정의
    2. UNIQUE KEY(고유키) : 고유키 정의
    3. NOT NULL : NULL 값 입력금지
    4. CHECK : 입력 값 범위 제한
    5. FOREIGN KEY(외래키) : 외래키 정의

### ```테이블 구조확인```

    - DESC(RIBE) 테이블명; -> 테이블 구조 확인(Oracle)
    - exec sp_help ‘db0.테이블명’ -> (SQL Server)
    go


### ```테이블 구조 변경(칼럼 추가, 삭제 등) DDL```

- ALTER TABLE 테이블명
  - ADD 칼럼명 데이터 유형;
  ADD CONSTRAINT 조건명 조건 (칼럼명); 조건 추가
  - DROP COLUMN 칼럼명;
  - MODIFY (칼럼명 데이터유형 DEFAULT식 NOT NULL); -> 칼럼 데이터 유형, 조건 등 변경 Oracle
  - DROP CONSTRAINT 조건명; 제약조건 삭제

  - ALTER (칼럼명 데이터유형 DEFAULT식 NOT NULL); -> SQL Server

- ALTER TABLE RENAME COLUMN 변경전칼럼명 TO 뉴칼럼명; Ora
- ALTER TABLE 변경전테이블명 TO 변경후테이블명; Ora
- sp_rename 변경전칼럼명, 뉴칼럼명, ‘COLUMN’; SQl
  - sp_rename ‘db0.TEAM’,‘TEAM_BACKUP’; SQL


- DROP TABLE 테이블명 [CASCADE CONSTRAINT]
- CASCADE CONSTRAINT : 참조되는 제약조건 삭제
- TRUNCATE TABLE 테이블명: 행 제거, 저장공간 재
사용
-------------------------------


### ```DML```

    DDL 명령어의 경우 실행시 AUTO COMMIT 하지만 
    DML의 경우 COMMIT을 입력해야 한다. SQL Server의 경우 DML도 AUTO COMMIT


DISTINCT(중복제거)


### ```와일드카드```

        * : 모든
        % : 모든
        - : 한 글자


### ```합성 연산자```
 - 문자와 문자 연결 : ||(Oracle), +(SQL Server)


### ```TCL```

    - 트랜잭션 : 밀접히 관련되어 분리될 수 없는 1개 이상
    의 DB 조작
    - COMMIT : 올바르게 반영된 데이터를 DB에 반영
    - ROLLBACK : 트랜잭션 시작 이전의 상태로 되돌림
    - SAVEPOINT : 저장 지점

```트랜잭션의 특성```

    1. 원자성 : 트랜잭션에서 정의된 연산들은 모두 성공
    적으로 실행되던지 아니면 전혀 실행되지 않아야 함
    2. 일관성 : 트랜잭션 실행 전 DB 내용이 잘못 되지 
    않으면 실행 후도 잘못 되지 않아야 함
    3. 고립성 : 트랜잭션 실행 도중 다른 트랜잭션의 영
    향을 받아 잘못된 결과를 만들어서는 안된다. 
    4. 지속성 : 트랜잭션이 성공적으로 수행되면 DB의 내용은 영구적으로 저장된다. 
    
- SAVEPOINT SVPT1; (Oracle)
- ROLLBACK TO SVPT1; (Oracle)
- SAVE TRAN SVPT1; (SQL Server)
- ROLLBACK TRAN SVPT1; (SQL Server)
- COMMIT; 


### ```연산자의 종류```
 - BETWEEN a AND b : a와 b 값 사이에 있으면 됨
 - IN (list) : 리스트에 있는 값중 어느 하나라도 일치
 - LIKE ‘비교문자열’ : 비교문자열과 형태가 일치
 - IS NULL : NULL 값인 경우
 - NOT IN (list) : list의 값과 일치하지 않는다
 - IS NOT NULL : NULL 값을 갖지 않는다. 

### ```연산자 우선순위``` 
-  ()->NOT->비교연산자->AND->OR

## ```NULL```
    - NULL 값과의 수치연산은 NULL 값을 리턴한다. 
    - NULL 값과의 비교연산은 거짓(FALSE)를 리턴한다

### ROW값

- ROWNUM : 원하는 만큼의 행을 가져올 때 사용(Or)
    - WHERE ROWNUM =1;(첫번째 사람만 가져와라)

- TOP : (SQL Server)
    - SELECT TOP(1) PLAYER_NAME FROM PLAYER;


### ```문자형 함수```
    LOWER : 문자열을 소문자로
    UPPER : 문자열을 대문자로
    ASCII : 문자의 ASCII 값 반환
    CHR/CHAR : ASCII 값에 해당하는 문자 반환
    CONCAT : 문자열1, 2를 연결
    SUBSTR/SUBSTRING : 문자열 중 m 위치에서 n개
    의 문자 반환

    LENGTH/LEN : 문자열 길이를 숫자 값으로 반환
    CONCAT(‘RDBMS’,‘ SQL’) -> ‘RDBMS SQL’
    SUBSTR(‘SQL Expert’,5,3) -> ‘Exp’
    LTRIM(‘xxxYYZZxYZ’,‘x’) -> ‘YYZZxYZ’
    RTRIM(‘XXYYzzXYzz’,‘z’) -> ‘XXYYzzXY’
    TRIM(‘x’ FROM ‘xxYYZZxYZxx’) -> ‘YYZZxYZ


### ```숫자형 함수```
    -SIGN(n) : 숫자가 양수면1 음수면-1 0이면 0 반환
    -MOD : 숫자1을 숫자2로 나누어 나머지 반환
    -CEIL/CEILING(n) : n보다 큰 정수값들중에서 최소값 23.3 - > 24
    -FLOOR(n) : n보다 작은 정수값들중에서 최대값 EX) 23.3 -> 23
    -ROUND : 반올림
    -TRUNC : 숫자 제거 함수


    ROUND(38.5235,3) -> 38.524
    ROUND(38.5235,1) -> 38.5
    ROUND(38.5235) -> 39
    TRUNC(38.5235,3) -> 38.523 3는 소수점 세번째까지 출력
    TRUNC(38.5235,1) -> 38.5
    TRUNC(38.5235) -> 38

### ```날짜형 함수```
- SYSDATE/GETDATE() 현재날짜와 시각 출력
- EXTRACT/DATEPART 날짜에서 데이터 출력
- TO_NUMBER(TO_CHAR(d,‘YYYY’))/YEAR(d)


## ```NULL 관련 함수```

    - NVL(식1,식2) : 식1의 값이 NULL 이면 식2 출력

    -  ISNULL(식1,식2) : 식1의 값이 NULL 이면 식2 출력

    - NULLIF(식1,식2) : 식1이 식2와 같으면 NULL을 아
    니면 식1을 출력

    - COALESCE(식1,식2) : 임의의 개수표현식에서 NULL
    이 아닌 최초의 표현식, 모두 NULL이면 NULL 반환

    ex)COALESCE(NULL,NULL,‘abc’) -> ‘abc’ 


## ```집계 함수```
- ALL : Default 옵션
- DISTINCT : 같은 값을 하나의 데이터로 간주 옵션

1. 여러 행들의 그룹이 모여서 그룹당 단 하나의 결과
를 돌려주는 함수이다.

2. GROUP BY 절은 행들을 소그룹화 한다. 

3. SELECT, HAVING, ORDER BY 절에 사용 가능

        -COUNT(*) : NULL 포함 행의 수
        -COUNT(표현식) : NULL 제외 행의 수
        -SUM, AVG : NULL 제외 합계, 평균 연산
        -STDDEV : 표준 편차
        -VARIAN : 분산
        -MAX, MIN : 최대값, 최소값


## ```GROUP BY, HAVING 절의 특징```

    1. GROUP BY 절을 통해 소그룹별 기준을 정한 후, SELECT 절에 집계 함수를 사용한다. 

    2. 집계 함수의 통계 정보는 NULL 값을 가진 행을 
    제외하고 수행한다. 

    3. GROUP BY 절에서는 ALIAS 사용 불가

    4. 집계 함수는 WHERE 절에 올 수 없다.

    5. HAVING 절에는 집계함수를 이용하여 조건 표시o

    6. HAVING 절은 일반적으로 GROUP BY 뒤에 위치

### SEARCHED_CASE_EXPRESSION

    -CASE WHEN LOC = ‘a’ THEN ‘b’

    - CASE LOC WHEN ‘a’ THEN ‘b’

    이 2문장은 같은 의미이다. 


### ```ORDER BY 특징```
    -SQL 문장으로 조회된 데이터들을 다양한 목적에 
    맞게 특정한 칼럼을 기준으로 정렬하여 출력하는데 
    사용한다. 

    -ORDER BY 절에 칼럼명 대신 ALIAS 명이나 칼럼 
    순서를 나타내는 정수도 사용 가능하다. 

    -DEFAULT 값으로 오름차순(ASC)이 적용되며 
    DESC 옵션을 통해 내림차순으로 정렬이 가능하다.

    -SQL 문장의 제일 마지막에 위치한다. 5. SELECT 절에서 정의하지 않은 칼럼 사용 가능


    - Oracle에서는 NULL을 가장 큰 값으로 취급하며 SQL 
    - Server에서는 NULL을 가장 작은 값으로 취급한다.


### ```SELECT 문장 실행 순서```
    FROM -> WHERE -> GROUP BY -> HAVING -> 
    SELECT -> ORDER BY

### ```WITH ITES```
    SELECT TOP(2) WITH TIES ENAME, SAL
    FROM EMP
    ORDER BY SAL DESC;
위는 급여가 높은 2명을 내림차순으로 출력하는데 같
은 급여를 받는 사원은 같이 출력한다(WITH TIES)

## ```JOIN```

    - JOIN : 두 개 이상의 테이블들을 연결 또는 결합하여 
    데이터를 출력하는 것
    일반적으로 행들은 PK나 FK 값의 연관에 의해 JOIN
    이 성립된다. 어떤 경우에는 PK, FK 관계가 없어도 
    논리적인 값들의 연관만으로 JOIN이 성립가능하다.


    - 5가지 테이블을 JOIN 하기 위해서는 최소 4번의 JOIN 
    과정이 필요하다. (N-1)


- NON EQUI JOIN : 2개의 테이블 간에 칼럼 값들이 
서로 정확하게 일치하지 않는 경우에 사용
‘=’ 연산자가 아닌 ```BETWEEN, >, <=``` 등 연산자 사용


        SELECT E.ENAME, E.JOB, E.SAL, S.GRADE
        FROM EMP E, SALGRADE S
        WHERE E.SAL BETWEEN S.LOSAL AND S.HSAL;


위는 E의 SAL의 값을 S의 LOSAL과 HSAL 범위에서 
찾는 것이다. 


###  ```집합 연산자```

- 두 개 이상의 테이블에서 조인을 사용
하지 않고 연관된 데이터를 조회할 때 사용
SELECT 절의 칼럼 수가 동일하고 SELECT 절의 동
일 위치에 존재하는 칼럼의 데이터 타입이 상호 호환
할 때 사용 가능


 - 일반 집합 연산자

        -UNION : 합집합(중복처리O)

        -UNION ALL : 합집합(중복처리 X)

        -INTERSECT : 교집합(INTERSECTION)

        -EXCEPT,MINUS : 차집합(DIFFERENCE)
        
        -CROSS JOIN : 곱집합(PRODUCT)


### 2과목 틀린문제
```63```
<br>
JOIN

- 일반적으로 JOIN은 PK와 FK값의 연관성에 의해 성립된다.

- DBMS 옵티마이져는 From절에 나열된 테이블들을 임의로 2개정도씩 묶어서 Join을 처리한다.

- EQUI Join은 Join에 관여하는 테이블 간의 컬럼 값들이 정확하게 일치하는 경우에 사용되는 방법

- EQUI Join은 '=' 연산자에 의해서만 수행되며, 그 이외의 비교연사자를 사용하는 경우에는 모두 Non EQUI Join이다

- 대부분 Non EQUI Join을 수행할 수 있지만, 때로는 설계상의 이류로 수행이 불가능한 경우도 있다. 


```57```
<br>
ORDER BY

- DBMS에 따라 NULL 값에 대한 정렬 순서가 다를 수 있으므로 주의하여야한다. 
    
    - 오라클은 NULL값을 가장 큰값으로 간주
    - SQL Server는 NULL값을 가장 작은 값으로 간주

- 기본적인 정렬순서는 오름차수이다.

- 날짜형 데이터타입은 오른 차순일 경우 날짜 값이 가장 빠른 값이 먼저 출력된다
ex) 2012-01-01 이 2021-12-01 보다 먼저 출력된다

- ORDER BY절에서 컬럼명 대신 Alias 명이나 컬럼 순서를 나타내는 정수도 사용이 가능하나, 이들을 혼용하여 사용할 수 있다.




```56번```
<br>
오류가 발생하는 SQL구문

    SELECT 지역, SUM(매출금액) AS 매출금액
    FROM   지역매출
    GROUP BY 지역
    ORDER BY 년 DESC;



```53번```
<br>
오류가 발생하는 SQL구문

        SELECT 메뉴ID, 사용유형코드, AVG(COUNT
        (*)) as AVGCNT

        FROM 시스템사용이력

        WHERE 사용일시 BETWEEN SYSDATE -1 AND SYSDATE

        GROUP BY 메뉴ID, 사용유형코드


        답 : 중첩된 그룹함수의 경우 최종결과값은 1건이 될수 밖에 없기에 GROUP BY절에 기술된 메뉴ID와 사용유형코드는 SELECT절에 기술될 수 없다

        

```48번```
<br>
NULL 다루기

A테이블 C1 컬럼 -> 1 , null, null
        
C2      -> 2,   2  , null
        
C3      -> 3,   3  ,  3

    SELECT SUM(COALESCE(C1,C2,C3)) FROM A

    - 답 : 6

```46번```
<br>
NULL 값 다루기

테이블에서 해당컬럼값(MGR)이 7698과 같으면 NULL을 표시 같지 않으면 해당컬럼을 표시

NULLIF(MGR,7698)

```42번```
<br>
오라클 환경에서 날짜 데이터


    1/24/60 -> 1분 
    1/24/60/10 -> 10분 

```40번```
<br>
내장 함수에 대한 설명

- 함수의 입력 행수에 따라 단일행 함수와 다중행 함수로 구분할 수 있다.

- 단일행 함수는 SELECT, ORDERBY, UPDATE의 SET 절에 사용이 가능

- 1:M 조인이라 하더라도 M쪽에서 출력된 행이 하나씩 단일행 함수의 입력값으로 사용할 수 있다.

- 다중행 함수도 단일행 함수와 동일하게 단일값만 반환

- 다중행 함수
  
        - 집계함수
        - 그룹함수
        - 윈도우 함수


```37번```
<br>
오라클과 SQL Server에서의 INSERT, SELECT시 NULL 값 처리

- 1 - INSERT INTO 서비스 VALUES('999','','2015-12-31');

        오라클 
        - 1번과 같이 공백이 입력됐을 경우 NULL로 입력됨 '' = null

        SQL Server
        - 1번과 같이 공백이 입력됐을 경우 공백으로 입력됨 '' = ''


```35번```
<br>
NULL의 연산

- NULL 값과의 연산은 NULL을 리턴한다.
- NULL 값과의 비교연산은 FALSE을 리턴한다.
- NULL은 특정값보다 크다, 작다 라고 표현할 수 없다.

```29번```
<br>
UPDATE, CREATE 수행시 커밋 롤백에 대한 문제

- 오라클
  - DDL 문장 수행 후 자동으로 COMMIT을 수행한다(내부적으로 트랜젝션 종료).

- SQL Sever
  - DDL 문장 수행 후 자동으로 COMMIT을 수행하지 않는다.
  
        CREATE TABLE B (생략);
        ROLLBACK;

        - 오라클에서는 DDL 문장 수행 후 자동 커밋으로 트랜잭션을 종료시키므로 B테이블은 생성된다.

        - SQL Server에서는 CREATE 문장도 트랜젝션의 범주에 포함된다. 그러므로 ROLLBACK 문장에 의해 B테이블이 생성되지 않는다.

```26번```
<br>
DELETE, TRUNCATE, DROP 명령어에 대해 비교한 설명

- DROP 
   - DDL
   - 롤백 불가능
   - Auto Commit
   - 테이블 정의 자체를 완전히 삭제함
   
- TRUNCATE
   - DDL(일부 DML성격을 가짐) 
   - 롤백 불가능
   - Auto Commit
   - 테이블을 최초 생성된 초기상태로만듬(껍데기만 존재)
- DELETE
  - DML
  - Commit 이전 Rollback 가능
  - 사용자 COMMIT
  - 데이터만 삭제

```23번```
- 개발 프로젝트의 표준은 모든 삭제 데이터에 대한 로그를 남기는 것을 원칙, 개발팀에서 사용 용도가 없다고 판단한 테이블의 데이터를 삭제하는 가장 좋은 방법은?


        정답 : DELETE FROM 테이블

        TRUNCATE, DROP -> 로그를 남기지 않는다


```2과목 19번```
- ```Delete Action : Cascade, Set Null, Set Default, Restrict```

    - Cascade : 마스터 삭제시 자식 같이 삭제
    - Set Null : 마스터 삭제시 해당 자식 필드 Null
    - Set Default : 마스터 삭제시 해당 자식 필드 Default 값으로 설정
    - Restrict :  자식 테이블에 pk값이 없는 경우만 마스터 삭제허용
    - No Action : 참조무결성을 위반하는 삭제/수정 액션을 취하지 않음

- ```Inset Action : AutoMatic, Set Null, Set Default, Dependent```

    - AutoMatic : 마스터 테이블에 pk가 없는 경우 마스터 pk를 생성후 자식 입력

    - Set Null : 마스터 테이블에 pk가 없는 경우 자식을 외부키를 NULL 값으러 처리
    - Set Default : 마스터 테이블에 pk가 없는 경우 자식을 외부키를 지정된 기본값으로 처리

    - Dependent : 마스터 테이블에 PK가 존재할 때만 자식 입력허용

```2과목 18번```
- RENAME 테이블명 TO 변경할 테이블명

```17번```
 - 직원 테이블 외래키 제약조건이 ON DELETE CASCADE
 - 부서 2개, 직원 1 -> 1번부서 , 직원 2,3 ->2번부서
 - A번 조건 -> 직원 카운트 = 3
 - B번 조건 -> 2번 부서 테이블 삭제
 - C번 조건 -> 직원 카운트 = 1 이 된다.

틀린 이유 : ON DELETE CASCADE 를 파악하지 못했다..


 ```15번 제약조건에 대한 설명(맞았지만 조그 헷갈렸음)```
 
 - 고유키로 지정된 모든 컬럼은 NULL값을 가질수없다. -> NULL값을 가질수 있다.

```14번 - 외래키에 대한 설명```(맞았지만 헷갈렸다...)
- 외래키는 널값을 가질수 없다-> 외래키는 널값을 가질수 있다.
- 한 테이블에 하나만 존재해야 한다. -> 여러 개 존재할 수 있다.

```13번```
- 학생 테이블을 생성후 유효한 튜플을 넣었을때 결과 (학생테이블 - 학번(char(8) pk, 장학금 - integer))

- 1.select count(*) from 학생
- 2.select count(학번) from 학생

- 정답: 1,2 번의 sql문장의 실행결과는 같다.(학번 컬럼이 pk이기에 널값이 없으므로)

```7번 ALTER TABLE Oracle과 SQL 서버 비교 문제```

- [오라클]

        ALTER Table 테이블명 ALTER COLUMN (컬럼명1 VARCHAR(30) NOT NULL, 컬렴명2 DATE NOT NULL);

- [SQL Server]

        ALTER Table 테이블명 ALTER COLUMN 컬럼명1 VARCHAR(30) NOT NULL;

        ALTER Table 테이블명 ALTER COLUMN 컬렴명2 DATE NOT NULL;

```3번```
- 다음 설명하는 SQL 명령어 종류는 무엇이냐
- (커밋, 롤백, 세이브포인트)트랜잭션 제어어, 일부에서는 DCL로 분류

정답 - TCL