"""
우선 생각한게
이모티콘별 할인액을 정해야한다. dfs를 통해 10,20,30,40 중 하나를 뽑아가면서 할인액을 정하자
뽑은 할인액 기준으로 계산하며 주의할점이
이모티콘  플러스서비스 가입자를 최대한 늘리는것이 첫번째고 두번째는 판매액임으로 주의하면서 비교해보자!
"""
discount_rates = [0.1,0.2, 0.3, 0.4]
tran_histroys = []
def dfs(n, picks,users,emoticons):
    if n==len(emoticons):
        service_subscriber = 0
        total_price = 0
        emoticons_discount_rates = []
        for pick in picks:
            emoticons_discount_rates.append(discount_rates[pick])

        for user in users:
            price = 0
            for idx, emoticons_discount_rate in enumerate(emoticons_discount_rates):
                ##[40, 10000]
                if user[0] <= emoticons_discount_rate*100:
                    price += (emoticons[idx] - (emoticons_discount_rate*emoticons[idx]))

            if price >= user[1] :
                service_subscriber +=1
                price = 0
            total_price+=price
                
        tran_histroys.append((service_subscriber,total_price))
        return
    for i in range(4):
        picks.append(i)
        dfs(n+1, picks,users,emoticons)
        picks.pop()

def solution(users, emoticons):
    picks = []
    dfs(0,picks,users,emoticons)
    
    tran_histroys.sort(key=lambda x : (x[0], x[1]), reverse=True)
    answer = []
    answer.append(tran_histroys[0][0])
    answer.append( tran_histroys[0][1])
    return answer
