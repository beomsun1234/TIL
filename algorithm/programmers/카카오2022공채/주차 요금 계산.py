"""
프로그래머스 2022 KAKAO BLIND RECRUITMENT 주차 요금 계산

간단했다. db를 사용한다고 가정하고 풀이했다. 우선 모든 입차, 출차 시간을 분으로 변경해 준다 key값을 set으로 중복을 제거해서 저장한다. 이 후 차량 번호를 key값으로 입차, 출차에 대한 시간을 저장한다.
또한 key를 차량번호로 하는 IN, OUT에 대한 기록을 저장하는 map을 하나 더 생성해서 마지막 입차, 출차를 기록한다.  key에 해당하는 IN, OUT에 대한 히스토리를
찾아서 만약 출차(OUT)에 대한 기록이 없다면 23:59분에 출차된 것으로 간주 한다. 시간이 기록된 db에 23:59의 값을 분으로 변경하고 db에 추가한다. 이제 시간은 모두 저장됐으니 요금을 구하면 된다.

위에 과정이 완료되면 key를 오름차순으로 정렬해주고 시간이 저장된 db에는 입차가 있으면 반드시 출차가 있다. 즉 0번 인덱스는 입차 1번인덱스는 출차이다. 짝수는 입차이고 홀수는 출차이다.
이를 통해 누적 주차 시간을 계산해준다.  이 후 누적 주차 시간이 기본 시간이하라면, 기본 요금을 청구하고 아니면 요금을 계산한다. 계산 할 때 주의 할 점이 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림해야한다.

초과한 시간 = (누적 주차시간 - 기본시간) // 단위 시간(분)

주어진 계산 로직으로 계산을 수행하고 answer에 담으면 정답이 된다.
"""

from collections import defaultdict
def solution(fees, records):
    answer = []
    # 공백기준으로 문자열 나눈 후 key는 2번째 인덱스
    db = defaultdict(list)
    history_db = defaultdict(list)
    tmp_key = set()
    for record in records:
        data = record.split(" ")
        # 시각을 분으로 변경하자
        time = data[0]
        time = time.split(":")
        time = (int(time[0]) * 60)+ int(time[1])  
        key = data[1]
        tmp_key.add(key)
        # IN - 입차, OUT - 출차
        history = data[2]
        history_db[key] = data[2]
        db[key].append(time)
    
    #내역에서 마지막 출차 기록이 없다면
    # 23:59에 출차된 것으로 간주 1439분
    for k in tmp_key:
        if history_db.get(k) == 'IN':
            db[k].append(1439)
    tmp_key = sorted(tmp_key)
    ## 요금계산
    # fees[0] 기본 시간(분), [1] 기본 요금(원), [2] 단위 시간(분), [3] 단위 요금(원)
    for k in tmp_key:
        tmp = 0
        for idx,data in enumerate(db.get(k)):
            if idx % 2 == 0:
                tmp+=data
            else:
                tmp-=data
        tmp_time = abs(tmp)
        print(tmp_time)
        parking_fee = 0
        # 누적 주차 시간이 기본 시간이하라면, 기본 요금을 청구합니다
        if tmp_time > fees[0]:
            # 나누어 떨어지지않으면 올림
            tmp_mod = (tmp_time - fees[0]) % fees[2]
            tmp_div = (tmp_time - fees[0]) // fees[2]
            tmp_time = tmp_div
            if tmp_mod !=0:
                tmp_time+=1
            parking_fee = fees[1] + (tmp_time * fees[3])
            answer.append(parking_fee)
        else:
            parking_fee = fees[1]
            answer.append(parking_fee)
    return answer