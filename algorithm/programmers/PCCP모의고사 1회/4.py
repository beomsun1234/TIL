import heapq
def solution(program):
    program.sort(key=lambda x: (x[1], x[0]))
    heap = []
    count = 0
    limt = len(program)
    
    heapq.heappush(heap, program.pop(0))
    
    answer = [0] * 11
    time = 0
    
    a,b,c = heapq.heappop(heap)
    wait = 0
    answer[a] =  wait
    time = b + c
    count = 1

    while limt > count :
        while len(program) >0 and program[0][1] <= time:
            p = program.pop(0)
            heapq.heappush(heap, p)
        if len(heap) < 1:
            time +=1
            continue

        a,b,c = heapq.heappop(heap)
        
        wait = time - b
        answer[a] += wait
        time += c

        count +=1

    answer[0] = time

    return answer
