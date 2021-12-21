"""
재귀에서 막혔다.. 다른건 다 구현했지만 제일 중요한 재귀를 구현하지 못했다.. 아직 재귀가 너무 약하다... 

"""
def splitUAndV(p):
    ## U, V 변환
    openCnt = 0
    closeCnt = 0
    u = ""
    v = ""
    for idx,i in enumerate(p):
        if i == "(":
            u+=i
            openCnt+=1
        elif i == ")":
            u+=i
            closeCnt+=1
        if openCnt == closeCnt:
            v += p[idx+1:]
            break;
    
    return u,v

def isGoodP(u):
    ## 괄호가 올바른지 체크
    openCnt = 0
    closeCnt = 0
    if not u.startswith("("):
        return False
    for i in u:
        if i == "(":
            openCnt+=1
        elif i == ")":
            closeCnt+=1
        
        if closeCnt > openCnt:
            return False
    
    return True
    
def rec(p):
    result = ""
    if not len(p): return ""
    u,v = splitUAndV(p)
    if isGoodP(u):
        # u가 올바르지 않은 문자열이면 v에 대해 다시 수행
        # 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다
        result = u + rec(v)
    else: 
        #  문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
        tmp = "(" #4-1
        tmp += rec(v) # 4-2
        tmp += ")" # 4-3
        u = u[1:-1] # 4-4
        for c in u: # 4-4
            if c == '(':
                tmp+=')'
            else:
                tmp+='('
        result += tmp #4-5
    return result

def solution(p):
    if isGoodP(p):
        return p
    answer = rec(p)
    return answer