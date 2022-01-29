"""
최소힙 - 1927

"""

import sys
## 최소 힙
import heapq

N = int(sys.stdin.readline())
nums = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x != 0: #0이아니면 값 추가
        heapq.heappush(nums,x)

    else: #0을 입력하면 주어진 횟수 만큼 출력
        if not nums: # nums가 비어있다면 0
            print(0)
        else: 
            print(heapq.heappop(nums))

