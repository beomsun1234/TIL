## 프로시저를 사용해서 달력 생성

    CREATE PROC makeCalendar
        @yyyy char(4)
    AS
    
    DECLARE @date as datetime
    DECLARE @diff as int
    DECLARE @i as int
    DECLARE @i_w as int
    DECLARE @h_val as int
    
    SET NOCOUNT ON -- 1개의 메시지만 출력
    
    SET @i = 0
    SET @diff = datediff(d,@yyyy + '-01-01',@yyyy + '-12-31')

    WHILE @i <= @diff 
      BEGIN
        set @date = dateadd(d, @i, @yyyy + '-01-01')
        set @i_w = datepart(w,@date)

        IF @i_w = 1 or @i_w = 7 
          BEGIN
            set @h_val = 1
          END 
         ELSE 
          BEGIN
            set @h_val = 0
          END
          
        INSERT INTO calendar (cdate,holiday) values (@date,@h_val)
        Set @i = @i + 1
      END
    SET NOCOUNT OFF
