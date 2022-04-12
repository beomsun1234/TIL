## mssql 중복데이터삭제하기

    SELECT MAX(UID) AS SEQ
           PER_CODE, 
           PER_NAME
      FROM 테이블
     GROUP BY PER_CODE 
     HAVING count(*) > 1;
    
    --------------------------
    테이블은 동일한 테이블이다.
    
    DELETE FROM 테이블
    WHERE UID IN (
    SELECT A.UID
      FROM 테이블 A,
           (SELECT MAX(UID) 
                   PER_CODE, 
                   PER_NAME
              FROM 테이블
             GROUP BY PER_CODE 
            HAVING count(*) > 1) B
     WHERE A.PER_CODE = B.PER_CODE
       AND A.UID <> B.UID 
    )
