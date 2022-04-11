## MSSQL을 이용해서 랜덤 뽑기

    SELECT TOP 1 *
      FROM 테이블명
     ORDER BY NEWID()
