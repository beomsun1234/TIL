"""
백준 촌수 계산 - 2644

쉽게 생각했지만 막상 제출하니 틀렸다고 나왔다... 테케 다 통과됐지만 왜 틀린지 몰랐다.. 

처음 로직은 아래와 같이 dfs탐색 중 y를 만나면 flag를 통해 중간에 빠져 나오도록 했다..
이 후 현재까지의 answer을 print해줬다... 왜 안되는지 아직도 모르겠다..
다른 방법으로 고쳤다. 찾으려는 사람을 시작점으로 방문하는 곳에 +1 해주고 탐색이 종료되고
찾는 촌수를 계산해야하는 분의(y)의 방문 값을 확인해서 만약 방문안하면 -1 방문했다면 몇번째에 방문 했는지를 print하면 답이된다.
def dfs(v):
    global flag
    global answer
    if v == y: # 만약 현재 정점이 구하려는 사람의 번호와 같다면 리턴
        flag = 1 # flag를 설정해서 dfs 탈출
        return
    for e in peoples[v]:
        if not visited[e] and flag ==0:
            answer+=1
            visited[e] = True
            dfs(e)
"""

# 사람 수 입력
n = int(input())

# 구하려는 촌수의 번호
x,y = map(int,input().split())

# 관계의 개수
m = int(input())

# 그래프 생성
peoples = []
for i in range(n+1):
    peoples.append([])
for i in range(m):
    xx,yy = map(int,input().split())
    peoples[xx].append(yy)
    peoples[yy].append(xx)


visited = [False] * (n+1)
global flag
flag = 0
global answer
answer = 0


## dfs를 통해 탐색
def dfs(v,count):
    for e in peoples[v]:
        if not visited[e]:
            visited[e] = count+1
            dfs(e,count+1)

visited[x] = True
dfs(x,0)
if not visited[y]:
    print(-1)
else:
    print(visited[y])