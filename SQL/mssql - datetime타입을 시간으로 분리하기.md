## mssql - datetime타입을 시간으로 분리하기

     SELECT DATEPART(YEAR, GETDATE()) AS 년, 
	          DATEPART(MONTH, GETDATE()) AS 월, 
            DATEPART(DAY, GETDATE()) AS 일,
            DATEPART(HOUR, GETDATE()) AS 시,
            DATEPART(MINUTE, GETDATE()) AS 분,
            DATEPART(SECOND, GETDATE()) AS 초,
            
