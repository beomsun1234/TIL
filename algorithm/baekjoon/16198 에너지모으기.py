"""
16198 에너지 모으기

1시간 정도 걸린 것 같다.. 간단했지만 처음에 이상하게 접근해서 시간을 많이 날렸다... 빠르게 버리고 다른 접근을 찾는게 더 이상적인 것 같다.


처음 접근은 1개를 뽑을 때마다 dfs를 계속 돌려주었고 하나를 뽑고 나서 N의 개수를 감소 시키면서 N의 개수가 2 이하일 경우 종료했다.

다른 테스트 케이스는 통과하나 예제 3 아래 케이스를 통과 못해서 버리지 못했다... print를 통해 디버그 해보니 내 처음 접근 첫번째 수만 변하고 나머지 이후 의 수들을 변하지 않았다..
 
7
2 2 7 6 90 5 9

위의 풀이를 버리고 빠르게 다른 접근을 생각했다.. 내가 총 뽑을 수 있는 개수는 N-2 이다. 5일경우 3개를 7일 경우 5개를 뽑을 수 있다.
인덱스를 뽑은 후 에 해당 인덱스를 쉬프트도 생각해 주어야한다. 예를 들어 
1 2 3 4 값을 가진  배열에서 2,1 의 순서로 인덱스를 뽑았다고 하면 2를 뽑고나서 사용한 값은 버리면 1,2,4 가 된다. 이럴 경우 인덱스 1은 아무런 지장이 없다.

하지만 1,2의 인덱스를 뽑을 경우이다. 1을 뽑고나면 1,3,4가 된다. 여기서 2인덱스의 뒤 값을 계산 할 수 없으므로 에러가 발생한다.

이를 위해 계산하기 전에 쉬프트를 해주어야한다. 현재 사용한 인덱스 값보다 크면 모두 -1 을 해준다. 아니면 그대로 둔다. 이렇게 하면 정답을 도출할 수 있다.


"""
N = int(input())
data = list(map(int,input().split()))

ret = []
global answer
answer = 0
visited = [False] * N
def dfs(pick, idx):
    global answer
    if idx == 0 or idx == N-1:
        return
    if pick == N-2:
        val = 0
        tmp_data = data[:]
        # 쉬프트
        for i in range(len(ret)):
            for j in range(i+1,len(ret)):
                if ret[i] < ret[j]:
                    ret[j] -=1
        for i in range(len(ret)):
            val += tmp_data[ret[i]-1] * tmp_data[ret[i]+1] 
            del tmp_data[ret[i]]
        answer = max(answer,val)
        return
    for i in range(1,N-1):
        if not visited[i]:
            visited[i] = True
            ret.append(i)
            dfs(pick+1,i)
            visited[i] = False
            ret.pop()

dfs(0,1)

print(answer)