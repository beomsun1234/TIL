import heapq

def solution(operations):
    answer = []
    minHeap  = [] # D -1일때 최솟값 삭제
    maxHeap  = [] # D +1일때 최대값 삭제
    tmp = 0
    flag  = [False] *len(operations)
    for i in range(len(operations)):
        if operations[i][0:1] ==  'I':
            val = int(operations[i][2:len(operations[i])])
            heapq.heappush(minHeap,val)
            heapq.heappush(maxHeap,-val)
            
        if operations[i][0:1] == 'D':
            val = int(operations[i][2:len(operations[i])])
            if len(minHeap) == 0:
                continue
            if val == -1:# 최솟값 삭제
                delMinVal = heapq.heappop(minHeap)
                maxHeap.remove(-delMinVal)
            if val == 1:
                delMaxVal = heapq.heappop(maxHeap)
                minHeap.remove(-delMaxVal)
        
    if len(minHeap)==0 and len(maxHeap) ==0:
        return [0,0]
    else:
        return [-maxHeap[0], minHeap[0]]
    return answer