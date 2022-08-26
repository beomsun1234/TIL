# 문자열에 특정 패턴이 포함되는지 확인하는 함수

문자열에 특정 패턴이 포함되는지 확인하는 작업이 필요했었는데 여러곳에서 쓰일 것 같아서 사용자 함수로 만들어보았다.

EX) 문자열 A,B,C,D,E,F,G가 있을때 D,E,F 가 함께 붙어있는지 판별

    CREATE FUNCTION is_pattern_included(@as_text varchar(255),
                      @as_pattern varchar(255))
    RETURNS INTEGER
    AS
    BEGIN
         DECLARE @ret INTEGER 
         
         SELECT @ret = -1

         SELECT @ret = 1
         FROM (SELECT @as_text AS TEXT) A
         WHERE A.TEXT LIKE '%'+@as_pattern+'%'
        
         //-1이면 포함 X, 1이면 포함
         RETURN(@ret)
    END
    GO

-- 함수 실행

    SELECT dbo.is_pattern_included('A,B,C,D,E,F,G', 'D,E,F')


정말 간단하게 만들어서 사용중이다. 

다른 테이블에도 검사 할 문자열이 거의 비슷한 형식이라 적용 가능할 것 같다.

