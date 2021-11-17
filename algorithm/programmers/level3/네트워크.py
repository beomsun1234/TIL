"""
Input : 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers
Output: 네트워크의 개수를 int

constraint
- 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
- 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
- i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
- computer[i][i]는 항상 1입니다.

DS - DFS

computer[i][i]는 항상 1입니다.

n = 3이라는 뜻은
computer[0][0]=1
computer[1][1]=1
computer[2][2]=1
로 해석했다.

1. [i][j]의 i를 현재 컴퓨터로 i를 기준으로 j(연결된 컴퓨터)가 있는지 확인 한다. ([i][j] =1 이면 존재한다)
2. 존재하면 j를 현재 컴퓨터로 하고 다음 컴퓨터를 찾는다.
3. 만약 현재 컴퓨터를 이미 확인했다면 return 해준다.
4. 민약 확인 하지 않았다면 dfs 계속 돈다. 1-2-3 연결되어 있다면 return 값은 1이다. 1-2 연결되고, 3은 연결되지 않았으면 return 1을 총 2번하고 리턴값을 더해주면 연결된 네트워크를 알 수 있다.

"""
def solution(n, computers):
    answer = 0
    c = 0
    ck= [False]*n
    def dfs(level,n,ck):
        if ck[level]:
            print(level,'은 이미 방문했다')
            return 0
        for i in range(n):
                if computers[level][i] == 1:
                    #print(ck)
                    ck[level] = True
                    #print(level)
                    dfs(i,n,ck)  
        return 1

    for i in range(n):
        if ck[i] == False:
            print(i)
            answer += dfs(i,n,ck)
            
    print(answer)
    return answer