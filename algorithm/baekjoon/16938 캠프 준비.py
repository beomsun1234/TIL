"""
16938 캠프 준비

간단했다. 주어진 조건을 활용해서 탐색해 주면 된다.

문제 난이도의 합은 L보다 크거나 같고, R보다 작거나 같아야 한다. 
또, 다양한 문제를 경험해보기 위해 가장 어려운 문제와 가장 쉬운 문제의 난이도 차이는 X보다 크거나 같아야 한다.

L<=문제난이도 합<= R

가장 어려운 - 가장쉬운 >= X
문제를 N개 가지고 있고 2문제 이상 선택해야한다.


"""
N,L,R,X = map(int,input().split())
problem= list(map(int,input().split()))
visited = [False] * N
combi = [] 
global cnt
cnt = 0
# 문제의 조합이 주어진 조건과 일치하는지 검사
def is_fit_condition(combi):
    total_level = 0
    min_level = 1000000
    max_level = 0
    for i in combi:
        total_level+= problem[i]
        min_level = min(min_level, problem[i])
        max_level = max(max_level, problem[i])
    max_minu_min = max_level - min_level
    if L<=total_level<=R and max_minu_min >=X:
        return True
    return False

## 문제를 고른다.
def dfs(pick,idx):
    global cnt
    if pick == N: # 문제를 전부 다 고르거나
        if is_fit_condition(combi):
            cnt+=1
        return
    if pick >= 2: # 2문제 이상 골랐을 때
        if is_fit_condition(combi):
            cnt+=1
    for i in range(idx,N):
        combi.append(i)
        dfs(pick+1, i+1)
        combi.pop()
  
dfs(0,0)
print(cnt)