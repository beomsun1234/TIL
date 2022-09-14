# 지우, 경희, 민호 순으로 경기를 진행

#지우의 가위바위보를 뽑는다. 중복 x 순서 중요!
from collections import deque

N, K = map(int, input().split())
jiwo = []
minho = []
kyoung = []
rules = []
global ans 
visited = [False] * (N+1)

ans = 0
for i in range(N):
    rule = list(map(int, input().split()))
    rules.append(rule)
for i in range(2):
    tmp_player_act = list(map(int, input().split()))
    if i ==0:
        kyoung = tmp_player_act
    else:
        minho = tmp_player_act
        
def getBattleOrder(p, next_player):
    if p < next_player:
        return (p,next_player)
           
    return (next_player,p)


def getNextPlayer(p1,p2):
    for i in range(1,4):
        if i !=p1 and i!=p2:
            return i
    return 0
# 가위바위보
def check(jiwo):
    global ans 
    win = [0] * 3
    players_turn = [0] * 3
    orders = deque()
    players_act = []
    players_act.append(jiwo)
    players_act.append(kyoung)
    players_act.append(minho)
    #처음은 무조건 지우랑 경희랑한다
    if rules[jiwo[players_turn[0]]-1][kyoung[players_turn[1]]-1] == 2:
        #지우가 이기면 민수랑
        orders.append((1,3))
        win[0]+=1
    else:
        #지우가 지거나 비기면 경희랑 민수랑
        orders.append((2,3)) 
        win[1]+=1
    # 턴 증가
    players_turn[0]+=1
    players_turn[1]+=1
    while(orders):
        p1,p2 = orders.popleft()
        if win[1] == K or win[2] == K:
            break
        elif win[0] == K:
            ans = 1
            break
        if players_turn[0] >= N:
            break
        if rules[players_act[p1-1][players_turn[p1-1]]-1][players_act[p2-1][players_turn[p2-1]]-1] == 2:
            win[p1-1]+=1

            next_player = getNextPlayer(p1,p2)

            orders.append(getBattleOrder(p1,next_player))
            
        else:
            win[p2-1]+=1

            next_player = getNextPlayer(p1,p2)

            orders.append(getBattleOrder(p2,next_player))
            

        players_turn[p1-1]+=1
        players_turn[p2-1]+=1
    return
def dfs(pick):
    if ans == 1:
        return
    if pick == N:
        check(jiwo)
        return
    for i in range(1,N+1):
        if not visited[i]: 
            visited[i] = True
            jiwo.append(i)
            dfs(pick+1)
            jiwo.pop()
            visited[i] = False

if N<K:
    print(0)
else:
    dfs(0)
    print(ans)