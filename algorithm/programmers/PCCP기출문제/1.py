# 1번
def solution(bandage, health, attacks):
    answer = 0
    nH = health
    time = 0
    end = attacks[-1][0]
    band_cnt = 0
    while time < end:
        time +=1
        # 공격
        if attacks[0][0] == time:
            nH -= attacks[0][1]
            attacks.pop(0)
            band_cnt = 0
            if nH <=0 :
                break
        else:
            if band_cnt > bandage[0]:
                band_cnt = 0
                continue
            band_cnt+=1
            heel = bandage[1]
            if band_cnt == bandage[0]:
                heel += bandage[2]
                band_cnt =0
            nH += heel
            
            if nH > health:
                nH = health

    if nH <=0:
        nH = -1
      
    return nH
