## 일한 시간 통계내기
    //업무 시작시간과 종료시간의 차를 분으로 계산하고 FLOAT형식으로 변경해서 60으로 나누어서 00.0 형식으로 구현(소수점 뒤의 숫자는 분을 의미한다.)
    SELECT A.사원번호, SUM(A.WORKTME)
      FROM (SELECT COMPANY_ID, 
                   업무시작시간, 
                   업무종료시간,
                   CONVERT(DECIMAL(4,1),CONVERT(FLOAT, DATEDIFF(MINUTE, 업무시작시간,업무종료시간))/60) AS 'WORKTME'
              FROM 근무시간테이블 
            WHERE 부서코드 = '해당부서'
      AND 업무시작시간 >= '2022-05-02 00:00:00'
      AND 업무종료시간 <= '2022-05-08 00:00:00'
      AND LEFT(특정사람 구분자,1) = '첫번째글자로구분한다') A
     GROUP BY A.사원번호;
     
    
더 좋은 방법 생각해보자!!
