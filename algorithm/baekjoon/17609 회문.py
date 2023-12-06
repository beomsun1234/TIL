N = int(input())

case = []

for i in range(N):
    case.append(input())

# 시간복잡도 2n 예상

#왼쪽먼저 삭제할 경우
def checkLeft(s):
    l = len(s)
    start = 0
    end = l -1
    count = 0
    for i in range(l):
        if start >= end:
            break
        if count > 1:
            return count
        if s[start] == s[end]:
            start +=1
            end -=1
        else:
            start +=1
            count +=1
    return count

#오른쪽 먼저 삭제
def checkRight(s):
    l = len(s)
    start = 0
    end = l -1
    count = 0
    for i in range(l):
        if end <= start:
            break
        if count > 1:
            return count
        if s[start] == s[end]:
            start +=1
            end -=1
        else:
            end -=1
            count +=1  
    return count

cntL = 0
cntR  =0
for i in case:
    cntL = checkLeft(i)
    val = cntL
    if cntL >= 2:
        cntR = checkRight(i)
        val = min(cntL, cntR)
    print(val)
