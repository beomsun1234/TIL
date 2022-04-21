## 불필요하게 긴 in절을 빼고 like로 보기 좋기 변경하기
     
     SELECT A.ALPHA
       FROM 테이블 A
      WHERE A.ALPHA IN ('RD','RB','RL', 'RH', 'RI', 'RM', 'RE', 'RJ', 'RK', 'RH','TC','TA', 'TB','TD','TE')
      
      -------------------------------------------
      
     SELECT A.ALPHA
       FROM 테이블 A
      WHERE A.ALPHA LIKE 'R[DBLHIMEJKH]%' OR A.ALPHA LIKE 'T[CABDE]%')
