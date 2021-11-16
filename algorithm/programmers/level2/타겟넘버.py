"""
input : 숫자가 담긴 배열 numbers 음이 아닌 정수,  타겟 넘버 target
output :  숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return  int


constraint
- 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
- 각 숫자는 1 이상 50 이하인 자연수입니다.
- 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

DS - DFS

1. 체크 배열을 만든다. 사용했던 배열 숫자 처음 값으로 사용하지 않게 체크 한다. dfs종료 후 다시 풀어준다.
2. 레벨을 설정한다.(numbers 배열의 길이)
3. 레벨이 끝에 다다르면 return
4. 값이 타켓과 같으면 카운트 증가 후 return
5. 배열에서 다음 숫자의 값을 더하거나 빼준 값을 썸에 넣어 dfs를 돌린다

!!중요 이것 때문에 엄청 헷갈렸다...순열 문제라고 생각하고 막 풀다가 답이 나오지 않았다... 입력 값의 순서에 대한 명확한 조건 제시가 필요하다.. 인풋으로 들어오는 수의 순서가 유지가 되어야 하는지 아닌지 명시 되어있지 않아 처음에 순열을 생각해서 인풋으로 들어오는 수의 순서가 유지 되지 않아야한다고 생각했다.. ex) 인풋이 [1,2] 일때 ->  [+1+2],[-1+2],[+1,-2],[-1-2] 만 고려해야하는지 아니면  (+2+1), (+2-1), (-2+1), (-2-1)도 고려해야하는지 적혀있지 않았다.. 당연히 후자라고 생각했지만 문제는 아니였다...
"""

def solution(numbers, target):
    answer = 0
    level = 0
    global ck
    ck = 0
    sum = 0
    def dfs(level,sum,target):
        global ck
        if level == len(numbers):
            if sum == target:
                ck+=1
            return
        else:
            dfs(level+1, sum+numbers[level], target)
            dfs(level+1, sum-numbers[level], target)       

    dfs(0,0,target)
    answer = ck
    return answer