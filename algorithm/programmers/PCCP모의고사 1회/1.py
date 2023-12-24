# 1번
def solution(input_string):
    S = input_string
    b = ""
    db = {}
    start = 0
    end = len(S)
    while start < end:
        a = S[start]
        b += a
        for j in range(start+1,len(S)):
            a2 = S[j]
            if a2 == a:
                start +=1
            else:
                break
        start+=1
        
    ans = []
    s = set()
    for i in b:
        if i not in db:
            db[i] = 1
        else:
            s.add(i)
            
    for i in s:
        ans.append(i)

    ans.sort()

    res = "".join(ans)
    if res == "":
        answer = "N" 
    else:
        answer = res
    return answer
