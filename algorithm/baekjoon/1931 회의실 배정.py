## 1931 회의실 배정


## 우선 회의가 끝나는 시간이 작은 순서로 정렬한다. 이 때 힙 큐사용
## 다음 회의시간이 현재 회의 끝난 시간보다 크거나 같다면 회의 가능  

import sys
import heapq
input = sys.stdin.readline
N = int(input())

time = []

for i in range(N):
    start, end = map(int, input().split())
    heapq.heappush(time,(end, start))

end, start = heapq.heappop(time)

cnt = 0
for i in range(len(time)):
    # 다음 시작점이 현재 끝시간 -1 이면
    if time[0][1] >= end:
        end, start = heapq.heappop(time)
        cnt+=1
    else:
        heapq.heappop(time)
    
print(cnt+1)

db = ['IOI']
