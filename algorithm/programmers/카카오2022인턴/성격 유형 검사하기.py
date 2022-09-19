"""
프로그래머스 성격 유형 검사하기


1번 지표	라이언형(R), 튜브형(T)
2번 지표	콘형(C), 프로도형(F)
3번 지표	제이지형(J), 무지형(M)
4번 지표	어피치형(A), 네오형(N)

1 	매우 비동의
2	비동의
3	약간 비동의
4	모르겠음
5	약간 동의
6	동의
7	매우 동의
"""

def getCharacter(db,cha1,cha2):
    if db[cha1] >= db[cha2]:
        return cha1
    
    return cha2


def solution(survey, choices):
    comparison_target = []
    answer = ''
  
    db = {'R': 0, 'T':0,
          'C': 0, 'F':0,
          'J': 0, 'M':0,
          'A': 0, 'N':0}
    for idx in range(len(survey)):
        score = choices[idx]
        character_pair = survey[idx]
        if score <= 3:
            character = character_pair[0]
            score = (score-4)*-1
            db[character] +=score
        else:
            character = character_pair[1]
            score = score-4
            db[character] +=score
            
    
    answer += getCharacter(db,'R','T')
    answer += getCharacter(db,'C','F')
    answer += getCharacter(db,'J','M')
    answer += getCharacter(db,'A','N')
    
    
  
    
    return answer
