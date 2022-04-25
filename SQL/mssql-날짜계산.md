## mssql을 사용해서 날짜를 계산해보자

    
### DATEDIFF
    
SELECT DATEDIFF(날짜형식, 시작날짜, 종료날짜)

    // 두 날짜간 일수 차이 
    SELECT DATEDIFF(DAY, '2022-04-20', '2020-04-19') 
    -> 1
    
    
### DATEADD

SELECT DATEADD(날짜형식, 값, 날짜)

    // 기준날짜의 + n일(2번째 인자)
    SELECT DATEADD(D, 2, '2022-04-20')
    -> '2022-04-22 00:00:00' 
    
    // 기준날짜의 + n달(2번째 인자)
    SELECT DATEADD(MONTH, 2, '2022-04-20')
    -> '2022-06-20 00:00:00' 
    
    // 기준날짜의 + n년(2번째 인자)
    SELECT DATEADD(YEAR, 2, '2022-04-20')
    -> '2024-06-20 00:00:00' 
     
    // 해당 달의 마지막 일자 구하기
    SELECT DATEADD(DAY, -1, DATEADD(MONTH, 1, '2022-04-01'))
    -> '2022-04-30 00:00:00'
    
    // 년 계산 (YEAR)
    SELECT DATEADD(YEAR, -1, '2022-04-25') AS [1년전] 
    SELECT DATEADD(YEAR, 1, '2022-04-25')  AS [1년후]
    
    // 최근 30일 전
    SELECT DATEADD(DAY, -30, GETDATE())
    
    
    
    
