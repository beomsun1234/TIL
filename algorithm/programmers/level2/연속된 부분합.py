def solution(sequence, k):
    
    start = 0
    end = 0
    com = 1000000
    ss = 0
    ee = 0
    t = sequence[0]
    while start <= end and len(sequence)> end:
        if t == k:
            tmp = abs(start - end)
            if com > tmp:
                com = tmp
                ss = start
                ee = end
        if t <= k:
            end +=1
            if end <len(sequence) :
                t += sequence[end]
        else:
            t -= sequence[start]
            start +=1
            
    answer = []
    answer.append(ss)
    answer.append(ee)
    return answer
