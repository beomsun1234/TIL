## 피벗테이블을 이용해서 달력생성
        
        //피벗테이블
        CREATE TABLE PIVOT(
            i INT
        )
        PIVOT테이블에 1부터 31까지 넣는다.
        
        

        SELECT CONVERT(CHAR(2),DatePart(dd,Dateadd(DAY, A.i - 5,'2022-05-01'))) AS MON,  
               CONVERT(CHAR(2),DatePart(dd,Dateadd(DAY, A.i - 4,'2022-05-01'))) AS TUE,  
               CONVERT(CHAR(2),DatePart(dd,Dateadd(DAY, A.i - 3,'2022-05-01'))) AS WED,  
               CONVERT(CHAR(2),DatePart(dd,Dateadd(DAY, A.i - 2,'2022-05-01'))) AS THU,  
               CONVERT(CHAR(2),DatePart(dd,Dateadd(DAY, A.i - 1,'2022-05-01'))) AS FRI,  
               CONVERT(CHAR(2),DatePart(dd,Dateadd(DAY, A.i ,'2022-05-01')))    AS SAT,
               CONVERT(CHAR(2),DatePart(dd,Dateadd(DAY, A.i + 1,'2022-05-01'))) AS SUN,  
               Dateadd(DAY, A.i - 5,'2022-05-01') AS MON_A,  
               Dateadd(DAY, A.i - 4,'2022-05-01') AS TUE_A,  
               Dateadd(DAY, A.i - 3,'2022-05-01') AS WED_A,  
               Dateadd(DAY, A.i - 2,'2022-05-01') AS THU_A,  
               Dateadd(DAY, A.i - 1,'2022-05-01') AS FRI_A,  
               Dateadd(DAY, A.i ,'2022-05-01')    AS SAT_A,
               Dateadd(DAY, A.i +1,'2022-05-01') AS SUN_A    
          FROM BAS..Pivot A
         WHERE (DATEPART(dw,'2022-05-01') + A.i) % 7 = 0
           AND A.i BETWEEN 0 AND DateDiff(dd,'2022-05-01', '2022-05-31') + 6
         ORDER BY A.i;
