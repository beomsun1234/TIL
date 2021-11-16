## 547. Number of Provinces

class Solution:
    """
    Input = isConnected 2차원 정수 배열 1또는 0으로 이루어짐
    Output = int 형 province 수 return
    
    Constraints
    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] is 1 or 0.
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]
    
    DS - DFS
    
    [0][0] -> 1 
    [1][1] -> 1 
    [2][2] -> 1
    ex)
    [0][1] == 1 0번 도시와 1번 도시는 연결되어있다 라는 뜻으로 이해
    
    1.  0번 도시 부터 dfs를 돌린다. 0번 도시를 방문표시하고 다음 도시를 방문하고 방문 표시 한다.  
    2.  만약 방문하려는 곳이 방문 했다면 return 0
    3.  아니면 계속 방문 후 return 1
    4.  위 과정을 반복하면 총 몇개의 주가 있는지 알 수 있다.
    Time  - o(n) n개중 방문 하지 않은 지역만을 n번 탐색하기에
    Space - o(n) - n개의 방문자 표시 배열과 dfs를 사용할 때 연결된 도시를 n만큼 스택에 넣기에 o(n)     
    """
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visted = [False] * len(isConnected)
        ret = 0
        
        def dfs(cityI, visted):
            if visted[cityI] == True:
                return 0            
            visted[cityI] = True
            for cityJ in range(len(isConnected)):
                if isConnected[cityI][cityJ] == 1:
                    dfs(cityJ,visted)
            return 1
        for cityI in range(len(isConnected)):
            if visted[cityI]==False:
                ret += dfs(cityI, visted)
        
        return ret
        
        
        
        