"""
월간 코드 챌린지 시즌 2

괄호 회전하기 level2

간단했다..

"""
def checkPairs(s,size):
    tt = []
    for i in s:
        if i == "{" or i =="[" or i == "(":
            tt.append(i)
        else:
            if tt[-1] == "{":
                if i != "}":
                    break
            
            if tt[-1] == "[":
                if i != "]":
                    break
                
            if tt[-1] == "(":
                if i != ")":
                    break
            tt.pop()
        
    if len(tt) == 0:
        return True

    
    return False

def solution(s):
    answer = 0
    for i in range(len(s)):
        t = s[i:]+ s[:i]
        if not t.startswith("(") and not t.startswith("[") and not t.startswith("{"):
            continue
        if not t.endswith(")") and not t.endswith("]") and not t.endswith("}"):
            continue
        open = 0
        close = 0
        idx = 0
        ## balance체크
        while open >= close and len(t)>idx:
            if t[idx] == "{" or t[idx] =="[" or t[idx] == "(":
                open+=1
            else:
                close+=1
            idx+=1
        if idx == len(t):
            if checkPairs(t,len(s)):
                answer+=1

    return answer