"""
14501 퇴사

"""

N = int(input())
cost = []
end_time  = []

for i in range(N):
    d,c = map(int,input().split())
    cost.append(c)
    end_time.append(d)
combi = []
global answer 
answer = 0

def cal(day_combi):
    total_rev = 0
    if len(day_combi) > 0:
        now_time = 0
        for i in day_combi:
            if now_time ==0 or now_time <= (i+1):
                now_time = (i+1)+ end_time[i]
                total_rev += cost[i]
            else:
                return 0
        if now_time > N+1:
            return 0
    return total_rev
# 조합을 뽑자
def dfs(pick,idx):
    global answer 
    if pick ==N:
        answer = max(answer,cal(combi))
        return
    answer = max(answer,cal(combi))
    for i in range(idx,N):
        combi.append(i)
        dfs(pick+1,i+1)
        combi.pop()

dfs(0,0)

print(answer)