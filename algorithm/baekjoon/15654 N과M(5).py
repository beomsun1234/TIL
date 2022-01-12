"""
백준 15654 n과 m(5) 정말 쉬웠다.. 문제의 조건에서 수열을 사전순으로 증가하는 순서로 출력해야 하므로

우선 입력받은 수열을 정렬해하여 dfs로 뽑을 수 만큼 탐색하면 된다. 나는 공백 부분에서 

tmp = "" + num[:numsize]
for i in range(numsize, len(num), numsize):
    tmp += " " + num[i:numsize+i]
    print(tmp[-1])

출력문을 위와 같이 작성해서 테스트케이스는 모두 통과했지만 제출하니 실패했다.... 왜그런지는 모르겠지만 다른 방법으로 출력했다. 배열을 선언해서 거기에 값을 넣어주고
map을 통해 int형 리스트를 조인해주고 print 해주니 성공했다.


"""
# 숫자 입력
n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []
numsize = len(str(nums[0]))
visited = [False] * n
## 순열
def dfs(pick,visited):
    if pick == m:# m개 뽑았으면 종료
        # ex) [1231, 1234, 1233, 1232] -> 1231 1234 1233 1232
        print(' '.join(map(str,ans)))
        return
    for i in range(len(nums)):
        if not visited[i]:
            ans.append(nums[i])
            visited[i] = True
            dfs(pick+1, visited)
            visited[i] = False
            ans.pop()

dfs(0,visited)
