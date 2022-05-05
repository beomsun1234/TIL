## MSSQL-IF ELSE구문 사용

    IF [조건]
    BEGIN
      로직1
    END
    ELSE 
    BEGIN
      로직2
    END
    
    
    DECLARE @SALARY
    SET @SALARY = 100000
    
    IF @SALARY >= 100000
    BEGIN
      PRINT '@SALARY 정규직입니다.'
    END
    ELSE 
    BEGIN
      PRINT '@SALARY 비정규직입니다.'
    END
    
    
