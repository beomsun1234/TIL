"""

level 2 - 최솟값 만들기

dfs로 모두 탐색 했더니 시간초과가 발생했다.... 무지성 완탐은 쉽지만 통과가 안된다.. 조금 생각해 보았다 정렬를 이용해서 접근해 보았다. A배열은 오름차순, B배열은 내림차순으로 정렬하고, A,B 배열의 동일한 인덱스에 해당하는 값을 곱하여 answer에 더해주면 됐다.

예를 들면  A = [1, 4, 2] , B = [5, 4, 4] 를 생각해보면 A를 오름차순 정렬, B를 내림 차순 정렬하면

A = [1,2,4], B = [5,4,4] 가 된다. 이것을 동일한 인덱스의 값을 곱하면 (1*5)5,(2*4)8,(4*4)16이 되고 다 더하면 최소값인 29가 된다.


# 모든 경우의 수 탐색
def dfs(pick, visited,A, sumV, B):
    global answer
    if sumV > answer:
        return
    if pick == len(A):
        answer = min(answer, sumV)
        return
    for i in range(len(A)):
        if not visited[i]:
            visited[i] = True
            dfs(pick+1,visited,A, sumV+(B[i]*A[pick]),B)
            visited[i] = False

def solution(A,B):
    global answer
    answer = 1000000
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    # dfs(pick, visited, idxs,A)
    visited = [False] * len(A)
    dfs(0,visited,A,0,B)
    return answer
# 무지성 완탐은 성공하지 못한다...
"""
def solution(A,B):
    answer = 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    A = sorted(A)
    B = sorted(B,reverse = True)
    for i in range(len(A)):
        answer+=A[i]*B[i]
    return answer
