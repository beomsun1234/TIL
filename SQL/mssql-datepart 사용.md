## datepart를 이용해서 요일 출력

    // 1.일, 2.월, 3.화, 4.수 , 5.목, 6금, 7토
    SELECT  GETDATE() AS now_day, 
            DATEPART(dw, GETDATE()) AS DAY
    
    //Pivot테이블은 int형 컬럼 i만 존재하면 1 ~ 50까지 들어있다. 
    //datepart를 사용해서 4주 나타내기
    SELECT A.i, 
           CONVERT(DATETIME, Dateadd(DAY, A.i + 1,'2022-05-01')), -- 일요일
           CONVERT(DATETIME, Dateadd(DAY, A.i - 5,'2022-05-01'))  -- 월요일
      FROM BAS..Pivot A
     WHERE (DATEPART(dw,'2022-05-01') + A.i) % 7 = 0 --토요일이면
      AND A.i BETWEEN 0 AND DateDiff(dd,'2022-05-01', '2022-05-31');
    토요일의 i값을 가져와 5월의 사작날과 더해서 4주를 나태낼 수 있다..
    
