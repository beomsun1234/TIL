## 퇴사자 발생시 재직여부 컬럼 일괄 변경 쿼리

     create procedure proc_emp_retire

     AS
     
     BEGIN
        ------
        -- 퇴사자 컬럼 변경 = '2'
        ------
        UPDATE EMP
           SET STATUS = '2'
         WHERE RETIRE_DATE <= GETDATE()
     END;
     
     
     exec proc_emp_retire;
