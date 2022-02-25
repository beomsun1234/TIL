"""
17779 게리맨더링 2

내 로직은 이렇다. 우선 x,y를 기준으로 조건에 부합하는 d1과 d2를 뽑는다. x,y,d1,d2를 바탕으로 선거구를 나누고 값을 도출했다.
처음에 코드를 작성하고 제출했을 때 실패가 계속 발생했다... 원인을 찾을 수 가 없었다.. 알고있는 반례랑 테스트케이스는 다 통과 되는데 어디서 틀렸는지 감을 잡지 못했다..
코드를 보니 경계선을 나누고 경계션 안의 구역을 5로 설정하는 부분에서 잘못 될 수 있구나 생각하고 코드를 수정했다. 

처음 코드는 아래와 같았다

for i in range(rr, rr+d1+1):
        tmp_city[i][idx] = 5
        if i != rr:
            tmp_city[i][idx+1] = 5
        idx-=1
        
    # 2
    idx = cc
    for i in range(rr,rr+d2+1):
        tmp_city[i][idx] = 5
        if i != rr:
            tmp_city[i][idx-1] = 5
        idx+=1
    # 3
    idx = cc-d1
    for i in range(rr+d1, rr+d1+d2+1):
        tmp_city[i][idx] = 5
        if i != rr+d1+d2:
            tmp_city[i][idx+1] = 5
        idx +=1
    # 4
    idx = cc+d2
    for i in range(rr+d2, rr+d2+d1+1):
        tmp_city[i][idx] = 5
        if i !=  rr+d2+d1:
            tmp_city[i][idx-1] = 5
        idx -=1  
    ## 경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구다
    # 여기만 하면 끝이다.
    idx = rr+2
    while 1:
        if tmp_city[idx][cc] == 5:
            break
        tmp_city[idx][cc] = 5
        idx+=1

    idx = rr+d2+d1 -2
    tmp = cc+d2-d1
    while 1:
        if tmp_city[idx][tmp] == 5:
            break
        tmp_city[idx][tmp] = 5
        idx-=1

이런식으로 경계선과 경계선의 안에 포함되어있는 5번 선거구를 나태냈다.. 이렇게 하니 오류가 발생한 것 같다. 이런식의 접근 보다는 
1번 선거구를 주어진 범위만큼 탐색해 가면서 경계선을 만나면 해당 구역 선거구를 만드는 것을 종료하였다. 이런식으로 4개의 선거구를 구하고 나머지 빈 곳은 5번 선거구가 된다.
이 후 각 선거구의 인구를 담는 배열을 선언해서 각 선거구의 최대값과 최솟값을 뺀 값을 리턴해주면 정답을 도출 할 수 있다. 



"""

global min_val
min_val = int(1e9)
N = int(input())
city = [[0 for _ in range(N + 1)]]

for i in range(N):
    data =[0]+ list(map(int,input().split()))
    city.append(data)

global total
total = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        total += city[i][j]

bound = []
# 선거구 나누기
def divide_city(boundary, rr,cc):
    global total
    global min_val
    tmp_city = [[0]*(N+1) for _ in range(N+1)]
    val = [0] * 5
    d1 = boundary[0]
    d2 = boundary[1]
    ## 경계선과 경계서안에 포함되어있는곳 = 5
    # 1
    idx = cc
    for i in range(rr, rr+d1+1):
        tmp_city[i][idx] = 5
        idx-=1
    # 2
    idx = cc
    for i in range(rr,rr+d2+1):
        tmp_city[i][idx] = 5
        idx+=1
    # 3
    idx = cc-d1
    for i in range(rr+d1, rr+d1+d2+1):
        tmp_city[i][idx] = 5
        idx +=1
    # 4
    idx = cc+d2
    for i in range(rr+d2, rr+d2+d1+1):
        tmp_city[i][idx] = 5
        idx -=1  
    
    ## 5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다
    """
    1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
    2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
    3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
    """
    # 1번
    for i in range(1,rr+d1):
        for j in range(1,cc+1):
            if tmp_city[i][j]==5:
                break
            val[0]+=city[i][j]
    # 2번
    for i in range(1, rr + d2 + 1):
        for j in range(N,cc,-1):
            if tmp_city[i][j] == 5:
                break
            val[1] += city[i][j]
    # 3번
    for i in range(rr + d1,N+1):
        for j in range(1, cc-d1+d2):
            if tmp_city[i][j] == 5:
                break
            val[2] += city[i][j]

    #4번 
    for i in range(rr+d2+1, N+ 1):
        for j in range(N, cc-d1+d2-1,-1):
            if tmp_city[i][j] == 5:
                break
            val[3] += city[i][j]
    
    val[4] = total - sum(val)
    tmp = max(val) - min(val)
    min_val = min(min_val,tmp)

# 경계선과, 경계의 길이 구하기
def dfs(pick,r,c):
    # d1,d2 를뽑으면 종료
    if pick == 2:
        if bound[0] < 1 and bound[1] <1:
            return
        if 1<=r<r+bound[0]+bound[1]<=N and 1<=c-bound[0] < c < c+bound[1] <=N:
            divide_city(bound,r,c)
        return
    for i in range(1,N+1):
        bound.append(i)
        dfs(pick+1,r,c)
        bound.pop()

# 모든 도시를 기준점으로 잡고 경계의 길이를 정한다. 
for i in range(1,N+1):
    for j in range(1,N+1):
        dfs(0,i,j)


print(min_val)