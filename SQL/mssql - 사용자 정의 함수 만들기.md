## mssql - 사용자 정의 함수 만들기

    CREATE FUNCTION [함수명] ( [파라미터] )
    RETURNS [결과 데이터 타입]
    AS
    BEGIN
      [로직]
      RETURN [결과값]
    END
    
    //함수 호출
    
    SELECT dbo.[함수명]( [파라미터] )


## 요일 구하는 함수 

    //1(일),2(월),3(화),4(수),5(목),6(금),7(토)
    CREATE FUNCTION dbo.get_day(@now_date DATE)
    RETURN INT
    AS
    BEGIN 
        DECLARE @RET_VAL INT;
        
        SELECT @RET_VAL = DATEPART(WEEKDAY,@now_date)
    RETURN @RET_VAL

    //함수 실행
    SELECT dbo.get_day('2022-05-12')
    --> 5
    
