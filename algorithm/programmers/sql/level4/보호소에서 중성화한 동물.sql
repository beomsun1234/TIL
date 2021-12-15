-----

-- 코드를 입력하세요
-- ANIMAL_INS 테이블은 동물 보호소에 들어온 동물
-- ANIMAL_OUTS 테이블은 동물 보호소에서 입양 보낸 동물
-- 보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다
--  보호소에 들어올 당시에는 중성화1되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회
-- Intact 중성화 X, Spayed 중성화 o, Neutered(중성화)
SELECT O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME
 FROM ANIMAL_OUTS O
WHERE EXISTS (SELECT '1' 
              FROM ANIMAL_INS I 
              WHERE I.ANIMAL_ID = O.ANIMAL_ID
                AND I.SEX_UPON_INTAKE LIKE 'Intact%'
             )
  AND (SEX_UPON_OUTCOME LIKE 'Spayed%'
   OR SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY O.ANIMAL_ID