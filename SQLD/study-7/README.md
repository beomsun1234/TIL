## SQL 활용 오답노트
<br>

### 65번
순수 관계 연산자

- SELECT

     -  WHERE절로 구현
- JOIN
- DIVIDE
- PROJECTION

    - SELECT절로 구현



### 72번
실수를 줄이자!!

LEFT JOIN 
- 조인 수행시 먼저 표기된 좌측테이블에 해당하는 데이터를 읽은 후, 나중에 표기된 우츨 테이블에서 JOIN 대상 데이터를 읽어 온다.

- 즉 TABLE A와 B가 있을때 A와 B를 비교하여 B의 JOIN 컬럼에서 같은 값이 있을 때 그 해당 데이터를 가져오고 없을 경우 B테이블에 가져오는 칼럽들은 NULL값으로 채운다.


### 73번
실수를 줄이자!!!

FULL OUTER JOIN
- LEFT, RIGHT OUTER JOIN의 결과를 UNION 합칩한 처리한 결과와 동일하다.


        SELECT A.ID, B.ID
        FROM T1 A FULL OUTER JOIN T2 B ON A.ID = B.ID
        ---------------------------------------------

        SELECT A.ID, B.ID
        FROM T1 A LEFT JOIN T2 B ON A.ID = B.ID

        UNION
        
        SELECT A.ID, B.ID
        FROM T1 A RIGHT JOIN T2 B ON A.ID = B.ID

        ----------------------------------------

        SELECT A.ID, B.ID
        FROM T1, T2
        WHERE T1.ID = T2.ID --> INNER JOIN
        
        UNION ALL

        SELECT A.ID, NULL
        FROM T1 A
        WHERE NOT EXISTS (SELECT 1 FROM T2 WHERE A.ID = T2.ID)

        UNION ALL

        SELECT NULL, B.ID
        FROM T2 B
        WHERE NOT EXISTS (SELECT 1 FROM T1 WHERE B.ID = T1.ID)
        
