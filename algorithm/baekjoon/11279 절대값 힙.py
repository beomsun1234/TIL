"""
절댓값 힙 - 11279

힙에 튜플형식으로 (절대값, 현재 값을) 넣어줘서 절대값으로 비교하고 결과 도출을 현재 값으로 한다.

"""

import sys
import heapq

N = int(sys.stdin.readline())
nums = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x != 0: #0이아니면 값 추가
        heapq.heappush(nums,( abs(x), x))

    else: #0을 입력하면 주어진 횟수 만큼 출력
        if not nums: # nums가 비어있다면 0
            print(0)
        else: 
            print(heapq.heappop(nums)[1])
            
