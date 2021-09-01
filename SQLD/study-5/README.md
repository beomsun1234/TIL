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
- 순위 함수(RANK FUNCTION)


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