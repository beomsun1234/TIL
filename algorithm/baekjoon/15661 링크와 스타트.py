N = int(input())

team = []

for i in range(N):
    a = list(map(int,input().split()))
    team.append(a)


visited2 = [False] * N

ret = 10000000000

def dfs(n,man_num):
    global ret
    # 두 팀의 인원수는 같지 않아도 되지만, 한 명 이상이어야 한다.
    if  n >=1:
        ret = min(cal(),ret) 
        
    for i in range(man_num,N):
        if visited2[i]:
            continue
        visited2[i]= True
        dfs(n+1, i+1)
        visited2[i]= False

def cal() -> int:
    tmp = 0
    tmp2 = 0
    for i in range(N):
        for j in range(i+1,N):
            if i==j: continue
            if visited2[i] and visited2[j]:
                tmp += team[i][j] 
                tmp += team[j][i]
            elif not visited2[i] and not visited2[j]:
                tmp2 += team[i][j]
                tmp2 += team[j][i]
    return abs(tmp-tmp2)

dfs(0,0)
print(ret)
