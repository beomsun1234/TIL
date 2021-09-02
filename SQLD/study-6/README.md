## 38회 기출문제 오답


### 문제 5
 - 테이블 '구매내역'에서 유일한 회원수 구하기


        회원번호  구매제품     
        -------  ------------
        1111       A103
        1111       A104
        1111       B12
        1112       A103
        1112       A104
        1113       B12
        1114       B13
        1114       B13
        1114       B13
        NULL       NULL

        ->
        SELECT COUNT(DISTINCT 회원번호)
        FROM 구매내역 ; 

        ->
        SELECT COUNT(회원번호)
        FROM 구매내역
        GROUP BY 회원번호;




잘몰랐던점-  ```집계함수를 사용할시 즉 함수를 사용할시 NULL값은 무시한다```



### 문제10

    SELECT 상품분류코드,
        AVG(상품가격) AS 상품가격,
        COUNT(*) OVER (ORDER BY AVG(상품가격) RANGE BETWEEN 10000 PRECEDING AND FOLLOWING ) AS 유사개수
    FROM 상품
    GROUP BY 상품분류코드

    유사개수 컬럼은 상품 분류 코드별 평균 상품격을 서로 비교하여 -10000 ~ + 10000 사이에 존재하는 상품분류 코드의 개수를 구한것이다.
    ->(GROUP BY에 있는 것(상품분류코드))


### 문제 21
계층형 쿼리에 대한 설명

- START WITH은 계층 구조의 시작점을 지정하는 구문.

- ORDER SIBLINGS BY 절은 계층내에서 정렬을 지정하는 구문이다

- 순방향전개랑 부모노드로부터 자식노드 방향으로 전개하는것을 말하다 

        connect by prior child - parent

- 루트노드의 LEVEL값은 1이다.           




### 문제 23

        COL 1     COL2
        ------   -------
         11        NULL
         NULL      12
         1          1


         -ㄱ
         SELECT SUM(COL1) + SUM(COL2) 
         FROM T2;

         -ㄴ
         SELECT SUM(COL1 + COL2)
         FROM T2;

         -ㄷ
         SELECT SUM(COL1, COL2)
         FROM T2;


         ㄱ->25     
         집계함수는 NULL값을 무시하고 계산한다.(없는걸로 본) 그러므로 
         col1 = 11, col2 = 13, 
         11+13 = 25

         ㄴ->2    
         SUM(COL1 + COL2) 
         row1 -> 11 + NULL = NULL
         row2 -> NULL + 12 = NULL
         ro3  -> 1+1       =   2

         COL3 
        -----
         NULL
         NULL
         2

         SUM(COL3) 이라는 뜻이므로 답은 2

         ㄷ->오류

         SUM은 파라미터로 1나만 받을수 있으므로 오류가 난다.


### 문제27

    A                B

    NAME            rule_no  RULE
    -----           ------- -------
    SMITH              1       S%
    ALLEN              2       %T
    SCOOT


    SELECT COUNT(*) CNT
    FROM A A, B B,
    WHERE A.NAME LIKE B.RULE


    우선 크로스조인이 발생하여 아래와 같이 나오고

     NAME  rule_no  RULE
    -----  ------- -------
    SMITH       1   S%
    ALLEN       1   S%
    SCOOT       1   S%
    SMITH       2   %T
    ALLEN       2   %T
    SCOOT       2   %T

    WHERE절의 조건을 필터링하면 아래와 같이 나온다

     NAME  rule_no  RULE
    -----  ------- -------
    SMITH       1   S%
    SCOOT       1   S%
    SCOOT       2   %T


    COUNT(*) = 3이다

    틀린이유 %T를 잘못생각했다... 그래서 룰넘버 2에 SMITH도 포함시켰다.... 문제를 너무 대충읽고 풀었다.... 왜 틀렸는지 아직도 의문이긴하다... 


### 문제 34

조인에 관한 문제

        T1              T2
        col1  col2      col1  col3
        ----  ----      ----  ----
         1      1        2      2  
         2      2        2      3
         4      3        3      4
         5      4        6      5

         inner, left, right, full , cross 조인의(T1.col1 = T2 col1) row수

         -inner

            col1  col2  col1  col3
            ----  ----  ----  ----
              2     2     2    2
              2     2     2    3

            ROW = 2개

         -left

            col1  col2  col1  col3
            ----  ----  ----  ----
              1     1   NULL  NULL
              2     2     2    2
              2     2     2    3
              4     3   NULL  NULL
              5     4   NULL  NULL

            ROW = 5개

         -right

            col1  col2  col1  col3
            ----  ----  ----  ----
              2     2     2     2
              2     2     2     3
            NULL  NULL    3     4
            NULL  NULL    6     5

            ROW = 4개

         -full

            col1  col2  col1  col3
            ----  ----  ----  ----
              1     1   NULL  NULL
              2     2     2    2
              2     2     2    3
              4     3   NULL  NULL
              5     4   NULL  NULL
            NULL  NULL    3     4
            NULL  NULL    6     5

            FULL OUTER JOIN을 틀렸다...
            중복을 처리를 잘몰랐던것같다...
            중복값을 처리해줘야한다.
            쉽게 생각하면 LEFT JOIN과 RIGHT JOIN을 합한거에 중복을 제거한거다.

            ROW = 7개

         -cross

           행별기반 이므로 4행 x 4행 = 16개
            

FULL OUTER JOIN을 틀렸다...

중복을 처리를 잘몰랐던것같다...
중복값을 처리해줘야한다.
쉽게 생각하면 ```LEFT JOIN과 RIGHT JOIN을 합한거에 중복을 제거한거다.```