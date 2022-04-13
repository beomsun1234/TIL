## 열을 행으로 변경하기

       job        dept_code   sal                   job        01    02 
      CLERK           01      1200                 ANALYST     NULL  1300 
      MANAGER         01      1400                 CLERK       1200  1300
      PRESIDENT       01      1500        ->       MANAGER     1400  1500
      ANALYST         01      1300                 PRESIDENT   1500  NULL
      MANAGER         02      1500
      CLERK           02      1100
  
  
  
  MSSQL PIVOT 함수를 사용해서 변경해보자.
  
      SELECT *
        FROM ( 피벗할 쿼리문 ) AS result
       PIVOT ( 그룹합수(집계컬럼) FOR 피벗대상컬럼 IN ([피벗컬럼값] ... ) AS pivot_result
       
피벗컬럼값의 대괄호([ ])는 존재해야하며, FROM절과 PIVOT절의 별칭(result, pivot_result)은 꼭 붙여줘야 오류가 발생하지 않는다.


    SELECT *
      FROM (
             SELECT job,
                    dept_code,
                    sal
               FROM emp
           ) AS result
     PIVOT ( 
             SUM(sal) FOR deptno IN ([01], [02]) 
           ) AS pivot_result
     ORDER BY job
