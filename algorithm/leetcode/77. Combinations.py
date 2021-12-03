"""
11:10 ~ 11:42
77. Combinations
Input = int n, k -> n은 수, k는 조합된 수의 길이
Output = k길이의 숫자의 조합 배열

Constraints:
    1 <= n <= 20
    1 <= k <= n
    
DS - DFS, backtracking

1. visited 배열을 선언해준다
2. 각 숫자를 저장해줄 ret배열을 선언해준다
3. 정답을 return할 answer 배열 선언
4. 숫자 1부터 시작하므로 시작인덱스를 1로 하여 dfs 수행
5. k만큼 수를 뽑았으면 저장된 값을 answer배열에 저장
6. 방문하지않았으면 방문표시후 dfs 수행
7. 숫자를 사용했으면 반환(백트랙킹)
8. 방문완료 후 반환(백트랙킹)

time = O(n)
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        visited = [False]*(n+1)
        ret = []
        answer = []
        def dfs(idx,ret,pick,k,n,visited):
            if pick == k:
                answer.append(ret[:])
                print('2개뽑음')
                print(ret)
                return
            else:
                for i in range(idx,n+1):
                    if not visited[i]:
                        visited[i] = True
                        ret.append(i)
                        dfs(i,ret,pick+1,k,n,visited)
                        ret.pop()
                        visited[i] = False
        
        dfs(1,ret,0,k,n,visited)
        print(answer)
        return answer
        
## 다른풀이
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        answer = []
        def dfs(idx,ret,pick,k,n):
            if pick == k:
                answer.append(ret[:])
                print('2개뽑음')
                print(ret)
                return
            else:
                for i in range(idx,n+1):
                    ret.append(i)
                    dfs(i+1,ret,pick+1,k,n)
                    ret.pop()
        dfs(1,ret,0,k,n)
        print(answer)
        return answer
        
        
