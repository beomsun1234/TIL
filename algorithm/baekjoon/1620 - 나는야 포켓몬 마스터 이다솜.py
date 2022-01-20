"""
1620 - 나는야 포켓몬 마스터 이다솜 
"""
pN = {} #포켓몬 넘버가 key
pS = {} # 포켓몬 이름이 key

#N = 포켓몬 도감 수, M맞춰야하는 수
N, M = map(int,input().split())

for i in range(1,N+1):
    data = input()
    pS[data] = i
    pN[str(i)] = data


ret = []

for i in range(M):
    data = input()
    if data in pN:
        ret.append(pN.get(data))
    if data in pS:
        ret.append(pS.get(data))


for i in ret:
    print(i)
    