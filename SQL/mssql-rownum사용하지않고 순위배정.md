## rownum 사용하지않고 입사일자 순서로 순위배정 하기

    SELECT E.ENTERDATE,
         (SELECT COUNT(1)+1
            FROM EMP EE
           WHERE E.ENTERDATE > EE.ENTERDATE
             AND E.DEPTCODE =  EE.DEPTCODE) AS 'RANK'
      FROM EMP E
     WHERE E.DEPTCODE = '부서코드'
    ORDER BY E.ENTERDATE;
