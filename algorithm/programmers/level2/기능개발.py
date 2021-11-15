"""
# 진짜 오래 걸렸다.....
Input  = 순서대로 작업의 진도가 적힌 1차원 정수 배열 progresses, 업의 개발 속도가 적힌 1차원 정수 배열 speeds
Oupput =  각 배포마다 몇 개의 기능이 배포되는지 return 1차원 정수 배열

DS - 완전탐색

1. check라는 배열의 디폴트 값을 false로 선언하고 각 작업의 진도가 100이 되면 True로 바꿔준다.
2. times라는 배열을 선언해주고 각 progresses별 작업의 진도가 100이 되기까지 얼마나 걸리는지 넣어준다.
3. 0번째 인덱스가 완료되어야 다음 배포를 할 수 있기에 times의 0번째를 taskTime으로 선언해준다. 
4. times를 비교 한다. 현재 taskTime이 다음 taskTime보다 크면 다음 task는 이미 완수 하여 배포만 남았다는 뜻이다. 그러므로
count를 증가 시켜준다.
5. 아닐경우 다음 taskTime을 설정해 주고 answers에 count를 넣어주고 count를 초기화 시켜주자
"""

def solution(progresses, speeds):
    answer = []
    ck = 0
    check = [False] *len(progresses)
    times = [1]*len(progresses)
    while ck<len(progresses):
        for i in range(0,len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
            if progresses[i] >= 100 and check[i] == False:
                check[i]=True
                ck +=1
            if check[i] == False:
                times[i] += 1
    count = 1
    taskTime = times[0]
    for i in range(1,len(times)):
        if times[i] <= taskTime:
            count+=1
        else:
            answer.append(count)
            count = 1
            taskTime = times[i]
    answer.append(count)
    print(answer)
    return answer