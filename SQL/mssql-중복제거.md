## 중복데이터 제거하기

### DISTINCT를 사용하여 중복 제거

    SELECT DISTINCT dept_code, per_code
      FROM EMP_INFO
     WHERE dept_code in (C0, C1)

### GROUP BY를 사용하여 중복 제거

    SELECT dept_code, per_code
      FROM EMP_INFO
     WHERE dept_code in (C0, C1
     GROUP BY dept_code, per_code
