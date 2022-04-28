## 프로시저를 사용해서 구구단을 만들어보자
    
    
    //
    CREATE PROCEDURE GUGU()
    
    AS
    
    DECLARE  @i int ,@k int 
    DECLARE  @str VARCHAR(100) 
    
    SET @i = 2
    
    BEGIN
    WHILE @i < 10
      BEGIN
        SET @K = 1
        PRINT STR(@i)+'단'
        WHILE @ K<10
          BEGIN
            PRINT STR(@i) +'X' + STR(@k) + '=' +STR(@i * @k)
            SET @k = @k+1
          END
        PRINT ''
        SET @i = @i+1
      END
    END
    
   
   
