"""
11047 - 동전 0 , 힙큐를 사용하다가 시간초과가 발생했다.... 그냥 그리디로 푸니 정답이 됐다..
import sys
import heapq
input = sys.stdin.readline
N , K = map(int,input().split())

money = []
flag = 0
for i in range(N):
    A = int(input())
    if A <= K:
        heapq.heappush(money,-A)
    if A == K:
        flag = 1
       

if flag != 0:
    print(1)
else:
    cnt = 0
    now_money = K
    while now_money > 0 and money:
        if now_money > -money[0]:
            cnt+= now_money // -money[0]
            now_money = now_money % -money[0]
            heapq.heappop(money)
        else:
            heapq.heappop(money)
    print(cnt)


"""

import sys
input = sys.stdin.readline
N , K = map(int,input().split())

money = []
flag = 0
for i in range(N):
    A = int(input())
    if A <= K:
        money.append(A)
    if A == K:
        flag = 1
       

if flag != 0:
    print(1)
else:
    cnt = 0
    now_money = K
    for i in range(len(money)-1, -1,-1):
        if now_money >= money[i]:
            cnt+= now_money // money[i]
            now_money = now_money % money[i]
       
    print(cnt)