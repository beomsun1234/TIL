"""
5014 - 스타트링크
처음 접근 로직은 간단했다.. bfs를 이용했고 현재 층이 목적 층보다 클 경우 아래로, 작을 경우는 위로 가게 했다.. 여기 문제가
위로 갈때 더이상 층이 없거나 아래로 갈때 갈 층이 없다면 갈 수 없다. 이 조건을 추가해 주지 않고 그냥 q에 냅다 위, 아래 값을 넣어 주어서 
루프를 빠져나오지 못했다.. 왜 간단한걸 생각못한걸까.. 갔단 곳도 다시 방문하게 될 것이다..

다시 방문했던 곳 방문하지 못하도록 visited를 설정해 주고 위 아래 이동해주면 된다.


q = deque()

if G < S and D == 0:
    print("use the stairs")

# 강호가 S층에서 G층으로 가
else:
    q.append(S)
    cnt = 0

    while q:
        now_s = q.popleft()

        if now_s == G:
            print("cnt=",cnt)
            break
        if now_s < G:
            next_s = now_s+U
        if now_s > G:
            next_s = now_s-D
        cnt+=1 
        q.append(next_s)

"""

from collections import deque
F,S,G,U,D = map(int,input().split())
visited = set()
q = deque()


# 강호가 S층에서 G층으로 가
flag = 0
q.append((S,0))
visited.add(S)
while q:
    now_s , cnt = q.popleft()
    if now_s == G:
        flag = 1
        print(cnt)
        break 
    if now_s+U <= F and now_s+U not in visited:
        next_s = now_s+U
        visited.add(next_s)
        q.append((next_s,cnt+1))
    if now_s - D >=1 and now_s - D not in visited:
        next_s = now_s-D
        visited.add(next_s)
        q.append((next_s,cnt+1))

if flag ==0:
    print('use the stairs')
    