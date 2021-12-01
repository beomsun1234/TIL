"""
79. Word Search, dfs, 백트랙킹
Input = m x n grid of characters , word - string
Output = bool

DS - DFS, backtracking

1. visited배열을 선언한다.
2. 상하 좌우로 확인 가능 하므로 상하, 좌우 배열을 만들어준다.
3. 시작점을 모든 위치로 잡고 dfs를 돌린다.
4. 만약 방문했으면 return
5. 현재 선택한 문자가 주어진 word의 값과 같지 않으면 리턴
ex) word[1] != board[m][n]

6. 위 조건을 통과하면 방문표시
7. 4가지 방향으로 dfs를 돌리고 다음 선택 문자를 1나 더 고른다.
8. pick한 횟수가 주어진 word의 길이와 같으면 return True (모두 같다는 뜻)


time = o(m*n)
space = o(m*n*2)
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dm = [1,-1,0,0]
        dn = [0,0,-1,1]
        ret = ['0']*len(word)
        visited = []
        for i in range(len(board)):
            visited.append([])
            for j in range(len(board[0])):
                visited[i].append(False)
        global ck
        ck = False
        ##----
        def dfs(m,n,visited,word,depth,ret,board):
            global ck
            if ck:
                return
            if visited[m][n]:
                return 
            if board[m][n]!=word[depth]:
                return 
            if depth == len(word)-1:
                print(ret)
                ret = []
                ck = True
                return
            visited[m][n] = True
            for i in range(4):
                nm = dm[i] + m
                nn = dn[i] + n
                if nm < 0 or nm >= len(board) or nn <0 or nn >= len(board[0]):
                    continue
                ret[depth] = board[m][n]
                dfs(nm,nn,visited,word,depth+1,ret,board)
            visited[m][n] = False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,visited,word,0,ret,board)
        
        return ck