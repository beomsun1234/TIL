# 15961
N, D, K, C = map(int, input().split()) 

window_size = K
belt = []
db = [0] * (D + 1)
cnt = 0

for i in range(N):
    val = int(input())
    belt.append(val)

for i in belt[:window_size]:
    if db[i] == 0:   
        cnt +=1
    db[i] +=1    

if db[C] == 0:
    maxV = cnt+1
else:
    maxV = cnt

for i in range(1,len(belt)):
    #앞에꺼 제거
    db[belt[i-1]] = db[belt[i-1]] - 1
    if db[belt[i-1]] == 0:
        cnt -=1
    #뒤에 추가
    if (i+window_size) > len(belt): 
        db[belt[(i+window_size-1)-len(belt)]] = db[belt[(i+window_size-1)-len(belt)]] +1
        if db[belt[(i+window_size-1)-len(belt)]] == 1:
            cnt +=1
    else:
        db[belt[(i+window_size-1)]] = db[belt[(i+window_size-1)]] +1
        if db[belt[(i+window_size-1)]] == 1:
            cnt +=1

    if db[C] == 0:
        maxV = max(maxV, (cnt+1))
    else:
        maxV = max(maxV, cnt)
    

print(maxV)
