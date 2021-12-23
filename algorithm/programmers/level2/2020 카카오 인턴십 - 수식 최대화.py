"""
2020 카카오 인턴십 - 수식 최대화

1. dfs로 각 연산자에 대한 우선 순위 조합을 만들어 준다.
2. expression을 숫자(numbers)와 연산자(operation)로 나누어준다(스택).
3. 각 만들어진 우선순위에 대해 expression을 나눈 숫자와 연사자를 우선선위에 맞게 계산한다.
4. 반복문을 돌면서 우선순위 연산자가 operation에 있으면 operation의 인덱스를 찾고 numbers[인덱스], numbers[인덱스+1]에 연산자를 더해 numbers[인덱스]를 연산한 숫자로 바꿔주고 사용한 연산자와 숫자를 제거해준다.
5. 연산이 종료되면 최대값을 비교하여 교체해준다

나름 쉬웠다고 생각했는데 연산자를 어떤식을 초기화 할 지 잘 몰랐다
ex) * > + > - 100-200*300-500+20
 *  100-60000-500+20 [-,-,+] 
 +  100-60000-520  [-,-]
 
 이렇게 배열의 값을 어떤식으로 바꿔줘야하는지 감이 잡히지 않았지만 while문으로 접근하니 생각보다 쉬웠다..
"""
## 우선순위 구하기
def dfs(pCnt,miCnt,muCnt,pick,visited,ret,m,prioritys):
    ret+=m
    if pCnt >1 or miCnt >1 or muCnt >1:
        return
    if pick == 3:
        prioritys.append(ret)
        return
    dfs(pCnt+1,miCnt,muCnt,pick+1,visited,ret,"+",prioritys)
    dfs(pCnt,miCnt+1,muCnt,pick+1,visited,ret,"-",prioritys)
    dfs(pCnt,miCnt,muCnt+1,pick+1,visited,ret,"*",prioritys)

import re
def solution(expression):
    answer = 0
    visited = [False] * 3
    ret = []
    tmp = expression
    prioritys = []
    dfs(0,0,0,0,visited,'','',prioritys)
    # +를 붙이면 연속됨
    #reg = re.compile('[0-9]+')
    for priority in prioritys:
        numbers = re.findall(r'\d+',expression) # 숫자
        operation = re.findall(r'\D',expression) # 연산자
        for i in priority: # 연산자 우선순위가 높은 것 부터 시작
            while i in operation: # 연산자가 operation에 있으면
                k = operation.index(i) # 해당 연산자의 인덱스를 가져옴
                if i == "*":
                    # 연산자와 ,숫자로 분리하였으므로
                    # 연산자 index는 숫자 인덳의 첫번째와 +1번째 사이에 있으므로
                    # 숫자의 첫번째 인덱스에 값과 두번째 인덱스의 값과 연산자를 계산하여
                    # 첫번째 인덱스를 바꿔준다
                    numbers[k] = int(numbers[k]) * int(numbers[k+1])
                elif i == '+':
                    numbers[k] = int(numbers[k]) + int(numbers[k+1])
                elif i == '-':
                    numbers[k] = int(numbers[k]) - int(numbers[k+1])
                #연산이 끝났으므로 연산자 제거
                del operation[k]
                # 첫번째 인덱스를 바꿔주는 것이므로 사용했던 숫자 제거
                del numbers[k+1]
        # 연산이 끝난 숫자의 절대값을 씌운 후 최대값을 구한다
        answer = max(answer,abs(numbers[0]))
    return answer