# 2번
def solution(ability):
    answer = 0
    visited = [False] * len(ability)
    pick = []
    
    global ans 
    ans = 0
    
    def dfs(n):
        # 종목수만큼 뽑는다.
        if n == len(ability[0]):
            global ans 
            val = sum(pick)
            ans = max(val, ans)
            return


        # 행의 길이 = 학생수
        for i in range(0,len(ability)):
            if not visited[i]:
                pick.append(ability[i][n])
                visited[i] = True
                dfs(n+1)
                pick.pop()
                visited[i] = False
    dfs(0)
    
    answer = ans
    return answer
