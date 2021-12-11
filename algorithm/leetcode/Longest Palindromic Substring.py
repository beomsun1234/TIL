class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret =[]
        visited = [False] * len(s)
        answer = set([])
        global maxV
        maxV = -100000
        def dfs(idx,ret,s,nowS,pick,visited,answer):
            global maxV
            if "".join(ret) != '' and ret[::-1] == ret:
                maxV = max(maxV,len(ret))
                answer.add(''.join(ret))
            if pick == len(s):
                return
            for i in range(idx,len(s)):
                if not visited[i]:
                    visited[i] = True
                    ret.append(s[i])
                    dfs(i,ret,s,nowS,pick+1,visited,answer)
                    ret.pop()
        
        ## 각 첫번재 문자를 이어 만들수 있는 모든 조합
        for i in range(len(s)):
            dfs(i,ret,s,'',0,visited,answer)
            visited = [False] * len(s)  

        for i in answer:
            if maxV == len(i):
                return i