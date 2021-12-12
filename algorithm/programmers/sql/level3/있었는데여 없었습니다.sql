-- 코드를 입력하세요
-- ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보
-- ANIMAL_OUTS 테이블은 동물 보호소에서 입양 보낸 동물의 정보
SELECT O.ANIMAL_ID, O.NAME
  FROM ANIMAL_OUTS O,
       ANIMAL_INS  I
 WHERE O.ANIMAL_ID = I.ANIMAL_ID   
   AND O.DATETIME < I.DATETIME
 ORDER BY I.DATETIME ASC;