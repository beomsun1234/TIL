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
