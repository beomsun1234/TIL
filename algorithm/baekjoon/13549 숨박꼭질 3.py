from collections import deque

N, K= map(int,input().split())

dx = [2,-1,1]


time = 0
now = N

def bfs():
    q = deque()
    q.append([N,0])
    visited = [False] *100001
    visited[N] = True
    while q:
        now, time = q.popleft()
        if now == K:
            break
        for i in range(3):
            if i == 0:
                a_now = now *2
                if a_now  > 100000:
                    continue
                if visited[a_now]:
                    continue
                visited[a_now] = True
                q.appendleft([a_now,time]) 
            else:
                n_time = time + 1
                a_now = now + dx[i]
                if a_now > 100000:
                    continue
                if a_now< 0:
                    continue
                if visited[a_now]:
                    continue
                visited[a_now] = True
                q.append([a_now,n_time]) 
    print(time)

bfs()
