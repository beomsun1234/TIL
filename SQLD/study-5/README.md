## ```그룹함수, WINDOW 함수, 계층형쿼리``` 


<br>

### ```GROUP FUNCTION```

- ROLLUP 함수 - 소그룹 간의 소계를 계산, 사용이 쉽고, 병렬 수행 가능




        ROLLUP을 UNION을 사용하여 바꿔보자

        -> 오른쪽부터 GROUP BY 칼럼을 삭제 하여 집합을 계속 생성 하며 변환
        
        ex)
        SELECT A,B, SUM(C)
        FROM   T
        GROUP BY ROLLUP (A,B)

        ---변환---------

        SELECT A,B, SUM(C)
        FROM   T
        GROUP BY A,B

        UNION ALL

        SELECT A,NULL, SUM(C)
        FROM   T
        GROUP BY A

        UNION ALL
        
        SELECT NULL,NULL SUM(C)
        FROM   T
        GROUP BY NULL


        오른쪽부터 GROUP BY 칼럼을 삭제 하여 집합을 계속 생성 하며 변환



        예제

        
        SELECT DEPTNO, NULL JOB, ROUND(AVG(SAL),1) AVG_SAL, COUNT(*) CNT_EMP
        FROM EMP
        GROUP BY DEPTNO

        UNION ALL

        SELECT DEPTNO, JOB, ROUND(AVG(SAL),1) AVG_SAL, COUNT(*) CNT_EMP
        FROM EMP
        GROUP BY DEPTNO, JOB

        UNION ALL

        SELECT NULL DEPTNO, NULL JOB, ROUND(AVG(SAL),1) AVG_SAL, COUNT(*) CNT_EMP
        FROM EMP
        ORDER BY DEPTNO, JOB;


        --- ROLLUP 사용시

        SELECT DEPTNO, JOB, ROUND(AVG(SAL), 1) AVG_SAL, COUNT(*) CNT_EMP
        FROM EMP
        GROUP BY ROLLUP (DEPTNO, JOB);


        ex)
        
        ----GROUP BY 사용----------------------
        SELECT DNAME, JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
        FROM EMP, DEPT 
        WHERE DEPT.DEPTNO = EMP.DEPTNO 
        GROUP BY DNAME, JOB ORDER BY DNAME, JOB; 

        DNAME          JOB       Total Empl  Total Sal
        -------------- --------- ---------- ----------
        ACCOUNTING     CLERK              1       1300
        ACCOUNTING     MANAGER            1       2450
        ACCOUNTING     PRESIDENT          1       5000
        RESEARCH       ANALYST            2       6000
        RESEARCH       CLERK              2       1900
        RESEARCH       MANAGER            1       2975
        SALES          CLERK              1        950
        SALES          MANAGER            1       2850
        SALES          SALESMAN           4       5600
        9 rows selected.



        -----ROLLUP 사용 -----------------------------------------------

        SELECT DNAME, JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
        FROM EMP, DEPT 
        WHERE DEPT.DEPTNO = EMP.DEPTNO 
        GROUP BY ROLLUP (DNAME, JOB); 


        DNAME          JOB       Total Empl  Total Sal
        -------------- --------- ---------- ----------
        SALES          CLERK              1        950   Level 1
        SALES          MANAGER            1       2850
        SALES          SALESMAN           4       5600
        SALES                             6       9400   > Level 2
        RESEARCH       CLERK              2       1900
        RESEARCH       ANALYST            2       6000
        RESEARCH       MANAGER            1       2975   > Level 2
        RESEARCH                          5      10875
        ACCOUNTING     CLERK              1       1300
        ACCOUNTING     MANAGER            1       2450 
        ACCOUNTING     PRESIDENT          1       5000
        ACCOUNTING                        3       8750   > Level 2
                                        14      29025   > Level 3

        13 rows selected.

        * L1 - GROUP BY 수행시 생성되는 표준 집계 (9건)
        * L2 - DNAME 별 모든 JOB의 SUBTOTAL (3건)
        * L3 - GRAND TOTAL (마지막 행, 1건)




- CUBE 함수 : GROUP BY 항목들간 다차원적인 계산, 다양한 데이터를 얻는 장점, But 시스템 부하 많은 단점

        CUBE를 UNION을 사용하여 바꿔보자

        -> 나올 수 있는 모든 경우의 GROUP BY 절을 생성 하여 변환.

        ex)

        SELECT A,B, SUM(C)
        FROM   T
        GROUP BY CUBE(A,B)

        ----변환-----------------

        SELECT NULL, NULL, SUM(C)
        FROM   T
        GROUP BY NULL

        UNION ALL

        SELECT NULL, B, SUM(C)   <- ROLLUP(A,B) 에 없는 경우의 수
        FROM   T
        GROUP BY B

        UNION ALL

        SELECT A, NULL, SUM(C)
        FROM   T
        GROUP BY A

        UNION ALL

        SELECT A, B, SUM(C)
        FROM   T
        GROUP BY A, B


        ----------------------------------------------------

        --- 큐브사용---
        SELECT CASE GROUPING(DNAME) WHEN 1 THEN 'All Departments' ELSE DNAME END AS DNAME,
        CASE GROUPING(JOB) WHEN 1 THEN 'All Jobs' ELSE JOB END AS JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
        FROM EMP, DEPT WHERE DEPT.DEPTNO = EMP.DEPTNO 
        GROUP BY CUBE (DNAME, JOB) ; 


        ---- 큐브 -> UNION ALL사용

        SELECT DNAME, JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
        FROM EMP, DEPT 
        WHERE DEPT.DEPTNO = EMP.DEPTNO 
        GROUP BY DNAME, JOB 
        UNION ALL
        SELECT DNAME, 'All Jobs', COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
        FROM EMP, DEPT WHERE DEPT.DEPTNO = EMP.DEPTNO 
        GROUP BY DNAME 
        UNION ALL
        SELECT 'All Departments', JOB, COUNT(*) "Total Empl", SUM(SAL) "Total Sal" 
        FROM EMP, DEPT 
        WHERE DEPT.DEPTNO = EMP.DEPTNO
        GROUP BY JOB 
        UNION ALL
        SELECT 'All Departments', 'All Jobs', COUNT(*) "Total Empl", SUM(SAL) "Total Sal"        
        FROM EMP, DEPT 
        WHERE DEPT.DEPTNO = EMP.DEPTNO;

        ---- 결과-------------------------------------------
        DNAME           JOB       Total Empl  Total Sal
        --------------- --------- ---------- ----------
        SALES           MANAGER            1       2850
        SALES           CLERK              1        950
        ACCOUNTING      MANAGER            1       2450
        ACCOUNTING      PRESIDENT          1       5000
        ACCOUNTING      CLERK              1       1300
        SALES           SALESMAN           4       5600
        RESEARCH        MANAGER            1       2975
        RESEARCH        ANALYST            2       6000
        RESEARCH        CLERK              2       1900
        ACCOUNTING      All Jobs           3       8750
        RESEARCH        All Jobs           5      10875
        SALES           All Jobs           6       9400
        All Departments CLERK              4       4150
        All Departments SALESMAN           4       5600
        All Departments PRESIDENT          1       5000
        All Departments MANAGER            3       8275
        All Departments ANALYST            2       6000
        All Departments All Jobs          14      29025

        18 rows selected.

        -----------------------------------------------------


- GROUPING SETS : 특정 항목에 대한 소계를 계산


        GROUPING SETS를 UNION을 사용하여 바꿔보자

        -> comma(,)를 UNION 으로 바꿔서 GROUP BY 절을 계속 생성 하라.

        ex)
        SELECT A,B, SUM(C)
        FROM   T
        GROUP BY 
        GROUPING SETS (A,B) 

        -----변환---------------

        SELECT A, NULL, SUM(C)
        FROM   T
        GROUP BY A
        UNION ALL 
        SELECT NULL, B, SUM(C)
        FRO    T
        GROUP BY B 





### ```WINDOW FUNCTION```
- 분석함수(ANALYTIC FUNCTION) 
  - CORR, COVAR_POP, COVAR_SAMP, STDDEV, STDDEV_POP, STDDEV_SAMP, VARIANCE, VAR_POP, VAR_SAMP, REGR_(LINEAR REGRESSION), REGR_SLOPE, REGR_INTERCEPT, REGR_COUNT, REGR_R2, REGR_AVGX, REGR_AVGY, REGR_SXX, REGR_SYY, REGR_SXY
- 순위 함수(RANK FUNCTION)
  - RANK, DENSE_RANK, ROW_NUMBER
- 집계(AGGREGATE) 함수
  - SUM, MAX, MIN, AVG, COUNT
- 순서 관련 함수
    - IRST_VALUE, LAST_VALUE, LAG, LEAD

WINDOW FUNCTION SYNTAX

 - WINDOW 함수에는 OVER 문구가 키워드로 필수 포함된다.

        SELECT WINDOW_FUNCTION (ARGUMENTS) OVER ( [PARTITION BY 칼럼]] [ORDER BY 절] [WINDOWING 절] )
        FROM 테이블 명;


        - WINDOW_FUNCTION : 기존에 사용하던 함수도 있고, 새롭게 WINDOW 함수용으로 추가된 함수도 있다. - ARGUMENTS (인수) : 함수에 따라 0 ~ N개의 인수가 지정될 수 있다.

        - PARTITION BY 절 : 전체 집합을 기준에 의해 소그룹으로 나눌 수 있다.

        - ORDER BY 절 : 어떤 항목에 대해 순위를 지정할 지 ORDER BY 절을 기술한다.

        - WINDOWING 절 : WINDOWING 절은 함수의 대상이 되는 행 기준의 범위를 강력하게 지정할 수 있다. ROWS는 물리적인 결과 행의 수를, RANGE는 논리적인 값에 의한 범위를 나타내는데, 둘 중의 하나를 선택해서 사용할 수 있다. 다만, WINDOWING 절은 SQL Server에서는 지원하지 않는다.


- BETWEEN 사용 타입

        ROWS | RANGE BETWEEN UNBOUNDED PRECEDING | CURRENT ROW | VALUE_EXPR PRECEDING/FOLLOWING AND UNBOUNDED FOLLOWING | CURRENT ROW | VALUE_EXPR PRECEDING/FOLLOWING

- BETWEEN 미사용 타입

        ROWS | RANGE UNBOUNDED PRECEDING | CURRENT ROW | VALUE_EXPR PRECEDING




- 예제
  - RANK , DENSE_RANK 함수


            SELECT JOB, ENAME, SAL
                , RANK( ) OVER (ORDER BY SAL DESC) RANK
                , DENSE_RANK( ) OVER (ORDER BY SAL DESC) DENSE_RANK
            FROM EMP; 

            JOB       ENAME             SAL       RANK      DENSE_RANK
            --------- ---------- ---------- -----------    -----------
            PRESIDENT KING             5000          1          1
            ANALYST   FORD             3000          2          2
            ANALYST   SCOTT            3000          2          2
            MANAGER   JONES            2975          4          3
            MANAGER   BLAKE            2850          5          4
            MANAGER   CLARK            2450          6          5
            SALESMAN  ALLEN            1600          7          6
            SALESMAN  TURNER           1500          8          7
            CLERK     MILLER           1300          9          8
            SALESMAN  WARD             1250         10          9
            SALESMAN  MARTIN           1250         10          9
            CLERK     ADAMS            1100         12         10
            CLERK     JAMES             950         13         11
            CLERK     SMITH             800         14         12



    - ROW_NUMBER()

      - ROW_NUMBER 함수
            ROW_NUMBER 함수는 RANK나 DENSE_RANK 함수가 동일한 값에 대해서는 동일한 순위를 부여하는데 반해, 동일한 값이라도 고유한 순위를 부여한다.


        
            SELECT JOB, ENAME, SAL 
                , RANK( ) OVER (ORDER BY SAL DESC) RANK
                , ROW_NUMBER() OVER (ORDER BY SAL DESC) ROW_NUMBER
            FROM EMP; 

            JOB       ENAME             SAL       RANK ROW_NUMBER
            --------- ---------- ---------- ---------- ----------
            PRESIDENT KING             5000          1          1
            ANALYST   FORD             3000          2          2
            ANALYST   SCOTT            3000          2          3
            MANAGER   JONES            2975          4          4
            MANAGER   BLAKE            2850          5          5
            MANAGER   CLARK            2450          6          6
            SALESMAN  ALLEN            1600          7          7
            SALESMAN  TURNER           1500          8          8
            CLERK     MILLER           1300          9          9
            SALESMAN  WARD             1250         10         10
            SALESMAN  MARTIN           1250         10         11
            CLERK     ADAMS            1100         12         12
            CLERK     JAMES             950         13         13
            CLERK     SMITH             800         14         14



    - WINDOWING 절 예제
        - ROWS 사용 예제 (아래 예제는 첫 번째 ROW부터 마지막 ROW까지의 합과(SAL1), 첫 번째 ROW부터 현재 ROW까지의 합(SAL2) 그리고 현재 ROW부터 마지막 ROW까지의 합(SAL3)을 출력하는 예제이다)

        - ```ROWS : 물리적인 ROW 단위로 행 집합을 지정한다.```
        - ```RANGE : 논리적인 상대번지로 행 집합을 지정한다.```
        - ```BETWEEN ~ AND 절 : 윈도우의 시작과 끝 위치를 지정한다.```
        - ```UNBOUNDED PRECEDING : PARTITION의 첫 번째 로우에서 윈도우가 시작한다.```
        - ```UNBOUNDED FOLLOWING : PARTITION의 마지막 로우에서 윈도우가 시작한다.```
        - ```CURRENT ROW : 윈도우의 시작이나 끝 위치가 현재 로우 이다.```

                SELECT empno, ename, deptno, sal,
                    SUM(sal) OVER(ORDER BY deptno, empno 
                                ROWS BETWEEN UNBOUNDED PRECEDING 
                                        AND UNBOUNDED FOLLOWING) sal1 -> 첫 번째 ROW부터 마지막 ROW까지의 급여 합계이다 ,

                    SUM(sal) OVER(ORDER BY deptno, empno 
                                ROWS BETWEEN UNBOUNDED PRECEDING 
                                        AND CURRENT ROW) sal2 ->  첫 번째 ROW 부터 현재 ROW까지의 급여 합계이다,

                    SUM(sal) OVER(ORDER BY deptno, empno 
                                ROWS BETWEEN CURRENT ROW 
                                        AND UNBOUNDED FOLLOWING) sal3 -> 현재 ROW부터 마지막 ROW까지 급여 합계이다.
                FROM emp;
                
                
                -- SAL1 : 첫 번째 ROW부터 마지막 ROW까지의 급여 합계이다. 
                -- SAL2 : 첫 번째 ROW 부터 현재 ROW까지의 급여 합계이다. 
                -- SAL3 : 현재 ROW부터 마지막 ROW까지 급여 합계이다.
                EMPNO ENAME       DEPTNO        SAL       SAL1       SAL2       SAL3
                ------ ------- ---------- ---------- ---------- ---------- ----------
                7782 CLARK           10       2450      29025       2450      29025
                7839 KING            10       5000      29025       7450      26575
                7934 MILLER          10       1300      29025       8750      21575
                7369 SMITH           20        800      29025       9550      20275
                7566 JONES           20       2975      29025      12525      19475
                7788 SCOTT           20       3000      29025      15525      16500
                7876 ADAMS           20       1100      29025      16625      13500
                7902 FORD            20       3000      29025      19625      12400
                7499 ALLEN           30       1600      29025      21225       9400
                7521 WARD            30       1250      29025      22475       7800
                7654 MARTIN          30       1250      29025      23725       6550
                7698 BLAKE           30       2850      29025      26575       5300
                7844 TURNER          30       1500      29025      28075       2450
                7900 JAMES           30        950      29025      29025        950



        - RANGE 사용 예제
            - 아래는 월별 금액 리스트를 출력하고, 직전 3개월 합계(AMT_PRE3)와 이후 3개월 합계(AMT_FOL3)를 함께 표시하는 예제이다.아래 예제에서는 7월 데이터가 없기 때문에 직전 3개월 합계(AMT_PRE3) 8월의 경우 6월,5월 두 달치만 누적된 것을 확인 할 수 있다.



                    SELECT yyyymm
                        , amt
                        , SUM(amt) OVER(ORDER BY TO_DATE(yyyymm,'yyyymm')
                                    RANGE BETWEEN INTERVAL '3' MONTH PRECEDING
                                            AND INTERVAL '1' MONTH PRECEDING) amt_pre3

                        , SUM(amt) OVER(ORDER BY TO_DATE(yyyymm,'yyyymm')
                                    RANGE BETWEEN INTERVAL '1' MONTH FOLLOWING
                                            AND INTERVAL '3' MONTH FOLLOWING) amt_fol3
                    FROM test
                    ;
                    
                    -- AMT_PRE3 : 직전 3개월 합계
                    -- AMT_FOL3 : 이후 3개월 합계 

                    YYYYMM           AMT   AMT_PRE3   AMT_FOL3
                    --------- ---------- ---------- ----------
                    200801           100                   900
                    200802           200        100       1200
                    200803           300        300       1500
                    200804           400        600       1100
                    200805           500        900       1400
                    200806           600       1200       1700
                    200808           800       1100       1200
                    200809           900       1400        600
                    200810           100       1700        500
                    200811           200       1800        300
                    200812           300       1200 


<br>


## ```HASH JOIN, SORT MERGE JOIN, NL JOIN (NESTED LOOP JOIN) ```

- ### ```참고비동등 조인 가능여부```

        - HASH JOIN                   X 

        - SORT MERGE JOIN             O

        - NL JOIN (NESTED LOOP JOIN)  O

- ### ```선행테이블 부하여부```

        - HASH JOIN - 선행테이블 적을 수록 좋다. 

        - SORT MERGE JOIN - 결과 행의 수가 적은 테이블을 조인 순서 상 선행 테이블로 선택

        - NL JOIN (NESTED LOOP JOIN) - 좁은 범위에 유리한 성능


- ### ```인덱스 유무```

        ---- HASH JOIN------
        - Hash Join은 양쪽 테이블 모두 Join 컬럼에 인덱스가 없을 경우에 사용

        ---- SORT MERGE JOIN--------
        -인덱스 없어도 빨리 데이터 찾는다.

        ---- NL JOIN (NESTED LOOP JOIN)-------
        -인덱스 생성 필요


- ### ```정렬 여부```

        ---- HASH JOIN ---------
        - 정렬 대신 해쉬값 생성 

        ---- SORT MERGE JOIN  ---------
        - 정렬을 위한 영역(Sort Area Size)에 따라 효율에 큰 차이 발생

        ---- NL JOIN (NESTED LOOP JOIN)  ---------
        - 데이터 랜덤 액세스

- ### ``` 순서```

   - HASH JOIN 

            1) 선행 테이블에서 주어진 조건을 만족하는 행을찾음

            2) 선행 테이블의 조인 키를 기준으로 해쉬 함수를 
            적용하여 해쉬 테이블을 생성(조인 칼럼과 SELECt 절에서 필요로 하는 칼럼도 함께 저장)
            (1 ~ 2번 작업을 선행 테이블의 조건을 만족하는 모든 행에 대해 반복수행)

            3) 후행 테이블에서 주어진 조건을 만족하는 행을 찾음

            4) 후행 테이블의 조인 키를 기준으로 해쉬 함수를 적용하여 해당 버킷을 찾음(조인 키를 이용해서 실제 조인될 데이터를 찾음)

            5) 조인에 성공하면 추출버퍼에 넣음(3 ~ 5번 작업을 후행 테이블의 조건을 만족하는 모든 행에 대해서 반복수행)


  - SORT MERGE JOIN

            1) 선행 테이블에서 주어진 조건을 만족하는 행을 찾음

            2) 선행 테이블의 조인 키를 기준으로 정렬 작업을 수행(1 ~ 2번작업을 선행 테이블의 조건을 만족하는 모든 행에 대해 반복 수행)

            3) 후행 테이블에서 주어진 조건을 만족하는 행을 찾음

            4) 후행 테이블의 조인 키를 기준으로 정렬 작업을 수행(3 ~ 4번 작업을 후행 테이블의 조건을 만족하는 모든 행에 대해 반복 수행)

            5) 정렬된 결과를 이용하여 조인을 수행하며 조인에 성공하면 추출버퍼에 넣음

  - NL JOIN (NESTED LOOP JOIN)

            1) 선행 테이블에서 조건을 만족하는 첫 번째 행을 찾음
            -> 이때 선행 테이블에 주어진 조건을 만족하지 않는 경우 해당 데이터는 필터링됨

            2) 선행 테이블의 조인 키를 가지고 후행 테이블에 조인 키가 존재하는지 찾으로 감
            -> 조인시도

            3) 후행 테이블의 인덱스에 선행 테이블의 조인 키가 존재하는지 확인
            -> 선행 테이블의 조인 값이 후행 테이블에 존재하지 않으면 선행 테이블 데이터는 필터링됨(조인작업x)

            4) 인덱스에서 추출한 레코드 식별자를 이용하여 테이블을 액세스
            -> 인덱스 스캔을 통한 테이블 액세스
            
            5) ~ 11) 반복수행