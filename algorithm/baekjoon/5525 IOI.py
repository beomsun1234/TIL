"""

ioi - 5525

N = int(input())

# Pi 만들기
if N != 1:
    for i in range(1,N):
        db[0] += 'OI' 

## 몇군데 포함인지 확인
M = int(input())
s = input()
idx = s.index('I')
cnt= 0
while idx < M:
    if s[idx:idx+len(db[0])] == db[0]:
        cnt+=1
        idx +=1
    else:
        idx+=1
print(cnt)

"""

N = int(input())
M = int(input())
S = input()
ret = 0
idx = 0
while idx < M:
    if S[idx] == "I":
        cnt = 0
        while S[idx+1:idx+3] == "OI":
            cnt += 1
            idx += 2
        if cnt >= N:
            ret += cnt - N + 1
        idx += 1
    else:
        idx += 1
print(ret)
