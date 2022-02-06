"""
17219 비밀번호 찾기

"""

db = {}

N, M = map(int,input().split())

for _ in range(N):
    key, value = map(str,input().split())
    db[key] = value

for _ in range(M):
    cc = input()
    print(db.get(cc))
                    
