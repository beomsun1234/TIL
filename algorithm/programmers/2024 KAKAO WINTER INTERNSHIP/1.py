def solution(friends, gifts):
    answer = 0
    # 1.선물 주고받은 기록 o
    # a > b - next b-> a +1
    # 2.기록 x or a = b
    # 선물지수가 작은사람에게 하나 더 받는다.
    # -선물지수는 내가준선물 - 내가받은선물
    # 선물지수도 같다면 선물 주고받지 않는다.
    # hash 사용
    
    #gifts - "A B" -> A는 선물 준 친구,  b는 받은 친구
    rec_db = {}
    give_db = {}
    record = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    
    code_db = {}
    for i in range(len(friends)):
        rec_db[friends[i]] = 0
        give_db[friends[i]] = 0
        code_db[friends[i]] = i
        
     
    for i in gifts:
        info = i.split(" ")
        giver = info[0]
        reciver = info[1]
        give_db[giver] +=1
        rec_db[reciver] +=1
        
        g = code_db[giver]
        r = code_db[reciver]
        record[g][r] +=1
    
    for f in range(len(friends)):
        record[f][f] = give_db[friends[f]] - rec_db[friends[f]]
    
    
    
    maxRes = 0
    
    
    for i in range(len(friends)):
        cnt = 0
        for j in range(len(friends)):
            if i == j: continue
            giveCnt = record[i][j]
            recCnt  = record[j][i]
            
            ## 내가 더많이 줬다면
            if giveCnt >0 and giveCnt >recCnt:
                cnt+=1
            elif (giveCnt == 0 and  recCnt == 0) or giveCnt == recCnt:
                giftCntTo = record[i][i]
                giftCntFrom = record[j][j]
                if giftCntTo > giftCntFrom:
                    cnt+=1
        maxRes = max(maxRes, cnt)
                    
    return maxRes
