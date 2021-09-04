## SQL 활용 오답노트
<br>

### ```65번```
순수 관계 연산자

- SELECT

     -  WHERE절로 구현
- JOIN
- DIVIDE
- PROJECTION

    - SELECT절로 구현



### ```72번```
실수를 줄이자!!

LEFT JOIN 
- 조인 수행시 먼저 표기된 좌측테이블에 해당하는 데이터를 읽은 후, 나중에 표기된 우츨 테이블에서 JOIN 대상 데이터를 읽어 온다.

- 즉 TABLE A와 B가 있을때 A와 B를 비교하여 B의 JOIN 컬럼에서 같은 값이 있을 때 그 해당 데이터를 가져오고 없을 경우 B테이블에 가져오는 칼럽들은 NULL값으로 채운다.


### ```3번```
실수를 줄이자!!!

FULL OUTER JOIN
- LEFT, RIGHT OUTER JOIN의 결과를 UNION 합칩한 처리한 결과와 동일하다.


        SELECT A.ID, B.ID
        FROM T1 A FULL OUTER JOIN T2 B ON A.ID = B.ID
        ---------------------------------------------

        SELECT A.ID, B.ID
        FROM T1 A LEFT JOIN T2 B ON A.ID = B.ID

        UNION

        SELECT A.ID, B.ID
        FROM T1 A RIGHT JOIN T2 B ON A.ID = B.ID

        ----------------------------------------

        SELECT A.ID, B.ID
        FROM T1, T2
        WHERE T1.ID = T2.ID --> INNER JOIN
        
        UNION ALL

        SELECT A.ID, NULL
        FROM T1 A
        WHERE NOT EXISTS (SELECT 1 FROM T2 WHERE A.ID = T2.ID)

        UNION ALL

        SELECT NULL, B.ID
        FROM T2 B
        WHERE NOT EXISTS (SELECT 1 FROM T1 WHERE B.ID = T1.ID)


### ```80번```

INTERSECT - 교집합(중복제거)

주어진 테이블
- 서비스 - 서비스 ID(PK), 서비스명

- 서비스이용   - 서비스ID(FK), 회원ID(FK)

- 회원         - 회원 ID(PK)

<BR>

    SELECT A.서비스ID, B.서비스명, B.서비스URL
    FROM   (SELECT 서비스ID
            FROM  서비스

            INTERSECT

            SELECT 서비스ID
            FROM  서비스이용
            ) A,
            서비스 B
    WHERE A.서비스ID = B.서비스ID

    --------서비스를 이용한적이 있는 고객을 추출--

    SELECT X.서비스, X.서비스명, X.서비스 URL
    FROM   서비스 X  -
    WHERE  NOT EXISTS ( SELECT 1 
                        FROM  (SELECT 서비스ID
                               FROM   서비스

                               MINUS(차집합) 
                               ->즉 서비스를 이용하지않은 고객
                       
                               SELECT 서비스ID
                               FROM   서비스이용
                       ) Y
                         WHERE X.서비스ID = Y.서비스ID);

        서비스를 이용하지 않은 고객이 존재하지 않는 서비스 -> 즉 서비스를 이용한 적이 있는 고객 추출 위와같음


### ```87번```
ORDER SIBLINGS BY -> 형제 노드사이에서 정렬 수행

    TAB1
    C1   C2   C3
    ---  ---  ---
    1         A
    2     1   B
    3     1   C
    4     2   D

    SELECT C3
    FROM TAB1
    START WITH C2 IS NULL
    CONNECT BY PRIOR C1 = C2
    

    결과----
    C1   C2   C3
    ---  ---  ---
    1          A
    2     1    B
    4     2    D
    3     1    C


    SELECT C3
    FROM TAB1
    START WITH C2 IS NULL
    CONNECT BY PRIOR C1 = C2
    ORDER SIBLINGS BY C3 DESC

    결과----
    C1   C2   C3
    ---  ---  ---
    1          A
    4     2    C
    2     1    B
    3     1    D

    2번째로 오는 것은?
    답: C



### ```90번```

계층형 쿼리문

- SQL서버에서의 계층형 쿼리는 CTE를 재귀호출 함으로써 계층 구조를 전개한다

- SQL서버에서의 계층형 쿼리는 앵커멤버를 실행하여 기본 결과집합을 만들고 이후 재귀 맴버를 지속적으로 실행한다.

- 오라클의 계층형 쿼리의 WHERE절은 모든 전개를 진행한 이후 필터 조건으로서 조건을 만족하는 데이터만을 추출하는데 활용된다.

- 오라클 계층형 쿼리의 PRIOR 키워드는 SELECT, WHERE, CONNECT BY절에 사용가능하다

- PRIOR 자식 = 부모 -> 순반향 전개이다


### ```95번```
서브쿼리

- 서비쿼리는 단일 행, 복수행 비교연산자와 함께 사용할 수 있다.
  - 단일행 - =, <>, >, < 등등
  - 복수행 - IN, ANY, ALL, EXISTS

- 서브쿼리는 SELECT, FROM, WHERE, HAVING, ORDER BY 절에 등에서 사용가능하다.

- 연관 서비쿼리는 서브쿼리가 메인쿼리 컬럼을 포함하고 있는 형태의 서브쿼리이다.

- 다중컬럼 서브쿼리는ㄴ SQL SERVER에서는 사용 X
                        


### ```98번```
테이블
- 회원     - 회원ID(PK), 가입일시, 이메일
- 메일발송 - 이벤트ID(PK,FK), 회원ID(PK,FK), 발송일시
- 이벤트   - 이벤트ID(PK), 이벤트명, 시작일자, 종료일자, 내용

<BR>

    SELCET A.회원ID , A.회원명, A.이메일
    FROM   회원 A
    WHERE EXISTS (SELECT 'X'
                  FROM   이벤트 B, 메일발송 C
                  WHERE  B.이벤트ID = C.이벤트ID
                  AND B.시작일자 >= '2014.10.01'   - ㄱ
                  --------------------------------
                  AND A.회원ID = C.회원ID          - ㄴ
                  --------------------------------
                  HAVING COUNT(*) (SELECT COUNT(*)
                                   FROM   이벤트
                                   WHERE  시작일자 >= '2014.10.01')- ㄷ
                  --------------------------------          
                  ) 

    -ㄱ에서 ㄴ을 보면 2014.10.01에 시작하는 이메일을 받은 회원을 나타낸다.
    -ㄷ은 해당회원의 이벤트 이메일을 받은 숫자와 전체 이벤트를 비교해서 진행된 이벤트보다 받은 메일의 숫자가 적으면 이메일을 못받은거다.

즉- 이벤트메시지를 하나라도 못받은 회원을 나타내는 쿼리이다. 



### ```99번```
서브쿼리(자주 틀리는것같다.. 개념을...)

- 다중행 서브쿼리 비교 연산자는 단일행 서브쿼리의 비교연산자로도 사용가능하다
   - 주의: 단일행은 다중행 비교연산자로 하지못함

- 비연관 서브쿼리는 메인쿼리에 값을 제공
  - 주의: 연관 서브쿼리는 X

- 서브쿼리는 항상 메인쿼리에서 읽혀진 데이터에 대해 서브쿼리에서 해당 조건이 만족하는지를 확인하는 방법으로 수행된다-> ```XXXX완전틀리다``` 상황에 따라 다르다!!



### ```120번```

B_USER 가 아래의 작업을 수행할 수 있도록 권한을 부여하는 DCL

    UPDATE A_USER.TB_A
    SET COL1 = 'AAA'
    WHWERE COL2= 3

GRANT SELECT, UPDATE ON A_USER TO B_USERP;


### ```123번```

PL/SQL

-BLOCK구조로 되어있어 각 기능별로 모듈화 가능

- 변수, 상수 등을 선언하여 SQL문장 간 값을 교환(WHERE절의 조건으로 대입 가능)

- IF, LOOP 등의 절차형 언어를 사용하여 절차적인 프로그램이 가능

- DBMS정의 에러나 사용자 정의에러를 정희하여 사용가능(EXECPTION)

- PL/SQL은 오라클에 내장되어있다.

- PL/SQL은 프로그램의 성능을 향상시킨다.

- PL/SQL은 여러 SQL문장을 BLOCK으로 묶고 한번에 BLOCK를 전부 서버로 보내기 때문에 통신량을 줄일수 있다.

- PL/SQL로 작성된 PROCEDURE, TRIGGER, USER DEFINED FUNCTION은 작성자 기준으로 트랜젝션 분리, 자율 트랜젝션처리가 가능하다.


### ```124번```

PL/SQL

부서 테이블에 데이터를 입력하기 전에 부서테이블의 모든 테이버를 ROLLBACK이 불가능 하도록 삭제하려고 할때 사용하는 문법


    CREATE OR REPLACE PROCEDURE INSERT_DEPT AUTHID CURRENT_USER
    AS
    BEGIN

    EXECUTE immediate 'TRUNCATE TABLE DEPT';

```EXECUTE immediate 'TRUNCATE TABLE DEPT';``` 이다

<BR>

### ```125번```

절차형 SQL 모둘

- 저장형 프로시져는 SQL을 로직과 함께 데이터베이스 내에 저장해 놓은 명령문의 집합을 의미한다.

- 저장형 함수(사용자 정의 함수)는 단독적으로 실행되기 보다는 다른 SQL문을 통하여 호출되고 그결과를 리턴하는 SQL의 보조적인 역활을 한다.

- 트리거는 특정한 테이블에 DML문이 수행되었을 때 데이터베이스에서 자동으로 동작하도록 작성된 프로그램이다

- 트리거 - 데이터의 무결성과 일관성을 위해 사용



### ```126번```
트리거

- 데이터베이스에 의해 자동으로 호출되고 수행

- DML문이 수행되었을때 호출되도록 정의할 수 있다.

- TCL로 트랜젝션을 제어할 수 없다.
  - 프로시저만 가능하다

- 데이터베이스에 로그인하는 작업에도 정의할 수 있다.

프로시저

- EXECUTE 명령어로 실행가능

- TCL사용가능






