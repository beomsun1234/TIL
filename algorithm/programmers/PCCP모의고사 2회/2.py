# 2번
import heapq

def solution(ability, number):
    answer = 0
    ability.sort()
    heap = []

    for i in ability:
        heapq.heappush(heap,i)
        
    while number > 0:
    # 교육 시작
        number -=1
        a1 = heapq.heappop(heap)
        a2 = heapq.heappop(heap)
        tmp = a1+ a2
        heapq.heappush(heap,tmp)
        heapq.heappush(heap,tmp)
    answer = sum(heap)
    return answer
