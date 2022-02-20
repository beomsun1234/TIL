"""
22951 송이의 카드게임
"""
N, K = map(int,input().split())
card_cnt = N*K
card = []

for i in range(N):
    data = map(int,input().split())
    for j in data:
        card.append([j,i])

idx = 0
while card_cnt>1:
    # 선택된 카드에 적힌 수 X를 확인한 후 
    x = card[idx][0]
    # 카드를 제거한다.
    card[idx][0] = 0
    # 제거된 카드의 오른쪽 X번째에 위치한 카드를 다시 선택한다
    while x >0:
        idx+=1
        # 되돌아 오는거 생각
        if idx > len(card) -1:
            idx = 0
        # 버린카드가 아니라면 탐색했다 표시
        if card[idx][0] !=0:
            x-=1
    card_cnt-=1

for i in card:
    if i[0] != 0:
        print(i[1]+1, i[0]) 
        
