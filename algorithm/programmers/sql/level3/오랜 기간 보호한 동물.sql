/// 오랜 기간 보호한 동물

-- 코드를 입력하세요
-- ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블
-- ANIMAL_OUTS 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블

-- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회
SELECT I.NAME, 
       I.DATETIME
 FROM ANIMAL_INS I 
WHERE NOT EXISTS (SELECT '1'
                    FROM ANIMAL_OUTS O
                   WHERE O.ANIMAL_ID = I.ANIMAL_ID)
ORDER BY I.DATETIME
LIMIT 3

알게된점 MSSQL의 TOP, MYSQL은 LIMIT을 써야한다
MSSQL을 사용해서 그런지 TOP이 더 익숙해서 LIMIT을 까먹어버렸다.... 