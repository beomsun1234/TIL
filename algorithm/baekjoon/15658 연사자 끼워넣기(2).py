"""
백준 15658 연산자 끼워넣기(2)
"""
N = int(input())
A = list(map(int,input().split()))
cnt = list(map(int,input().split()))
op = []
global max_val
max_val = -1000000001
global min_val
min_val = 1000000001

# 계산
def cal(op):
    val = A[0]
    for idx, i in enumerate(op):
        if i == 0:
            val += A[idx +1]
        elif i == 1:
            val -= A[idx +1]
        elif i == 2:
            val *= A[idx +1]
        elif i == 3:
            val = int(val/A[idx +1])
    return val

# 연산자 뽑기
def dfs(pick):
    global max_val
    global min_val
    #연산자는 N-1개 뽑기
    if pick == N-1:
        val = cal(op)
        min_val = min(min_val,val)
        max_val = max(max_val,val)
        return
    #0 = '+', 1 = '-', 2 = '*', 3 = '/'
    for i in range(4):
        if cnt[i] != 0:
            cnt[i] -= 1
            op.append(i)
            dfs(pick+1)
            op.pop()
            cnt[i] += 1
            
dfs(0)
print(max_val)
print(min_val)