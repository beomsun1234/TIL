from collections import deque
# deque를 사용하면 리스트 pop(0)할때보다 빠르다
def solution(prices):
    answer = []
    pos = 0
    qPrices = deque(prices)
    while qPrices:
        price = qPrices.popleft()
        ck=0
        # 남은 queue를 순회하며 값이 작아지기 전까지 초를 증가
        for p in qPrices: 
            ck +=1 
            if price > p:
                break
        answer.append(ck)
    return answer
    