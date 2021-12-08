"""
level2 가장큰수
실패코드 (재귀로 모든 순열을 찾는다) 테스트케이스는 모두 통과하나 런타임 오류 발생(이방법으로 접근 하는것이 아니라는 것을 깨달았다. 레벨2라서 그냥 재귀 돌리면 쉽게구나 생각한 것 같다..  [6102, 6210, 1062, 1026, 2610, 2106] 보자마자 순열이 생각이 났다.)
def dfs(pick,ret,idx,numbers,visited):
    global maxV
    if pick == len(numbers):
        nowVal = int("".join(ret))
        maxV = max(maxV,nowVal)
        return
    for i in range(0,len(numbers)):
        if not visited[i]:
            visited[i] = True
            ret.append(str(numbers[i]))
            dfs(pick+1,ret,i,numbers,visited)
            visited[i] = False
            ret.pop()

def solution(numbers):
    global maxV
    maxV = -10000
    answer = ''
    visited = [False] * len(numbers)
    ret = []
    dfs(0,ret,0,numbers,visited)
    return str(maxV)
    
----
처음에 접근 방식은 주어진 숫자배열을 string으로 변환 후 첫번째 인덱스의 값을 받아서 아스키 코드 값을 비교하는 방법을 떠올렸지만 주어진 2번째 테스트 케이스인 [3,30,34,5,9]에서 막혔다. 이럴 경우 3이 3개가 나와서 어떤 숫자를 먼저 사용하는지 알 수가 없었다. 

"""

def solution(numbers):
    answer = ''
    ret = []
    for idx,num in enumerate(numbers):
        sNum = str(num)
        ret.append((sNum*3,idx))
    ret = sorted(ret,reverse = True)
    for i in ret:
        sNum = str(numbers[i[1]])
        answer+=sNum
    if answer.startswith('0'):
        return "0"
    return answer