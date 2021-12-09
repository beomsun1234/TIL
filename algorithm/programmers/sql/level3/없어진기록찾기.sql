-- 없어진 기록 찾기 LEVEL3

-- 코드를 입력하세요 
-- ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블 
-- ANIMAL_OUTS 테이블은 동물 보호소에서 입양 보낸 동물의 정보 
SELECT O.ANIMAL_ID, O.NAME FROM ANIMAL_OUTS O WHERE NOT EXISTS (SELECT '1' FROM ANIMAL_INS I WHERE I.ANIMAL_ID = O.ANIMAL_ID );