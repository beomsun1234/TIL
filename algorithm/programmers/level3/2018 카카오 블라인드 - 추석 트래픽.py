"""
카카오블라인드 - 추석 트래픽.py
level 3

처음에 문제를 이해하지 못한것같다.. 무작정 코드를 작성하려니 접근 방식이 떠오리지가 않았다. 이런문제는 무작정 코드를 작성하기 보다는 손으로 타임라인을 그려서 조건을 찾아내기만 하면 쉬운 문제였다.. 나는 그러지 않고 바로 접근하려니 문제를 이해하지 못했다.. 손으로 타임라인을 그리고 접근하니 문제를 이해할 수 있었다.. 처음에 전부 초로 바꿔줄 생각을 안했다.. 시간과 분을 무시하고 초가져와서 접근하니 답이 나오지 않았다.. 힌트를 보고 초로 바꾸라는 분들이 있어서 초로 바꿔서 접근하니 통과 할 수 있었다

"""
def getTime(log):
    ret = log.split(" ")
    end_time = ret[1].split(':')
    # 전부 초로 바꾼다.
    end_time = int(end_time[0]) * 3600000 + int(end_time[1])* 60000 + int(end_time[2].replace('.',''))
    start_time = end_time - int(float(ret[2][:-1])*1000) + 1
    if start_time >0:
        return start_time, end_time
    return 0, end_time
def solution(lines):
    answer = 0
    logs = []
    for line in lines:
        ## 시작시간과 끝나는 시간 초로 변환
        start_time, end_time = getTime(line)
        logs.append((start_time,end_time))
    maxThroughput = 0
    
    ## 최대 처리량 구하기
    for idx in range(len(logs)):
        ## 각 로그의 처리 구간(1초 구간)을 종료시간 + 1000으로 설정해준다
        section_end = logs[idx][1] + 1000
        throughput = 0
        ## 나를 제외한 다른 로그를 탐색
        for idx2 in range(idx,len(logs)):
            #현재 탐색한 로그의 시작값을 가져온다
            start_time = logs[idx2][0]
            # 현재 탐색한 로그의 시작값이 현재 처리 구간 안에 있을 경우 처리량 증가 
            if section_end > start_time:
                throughput+=1
        
        # 해당 처리 구간이 끝나면 max값 갱신
        maxThroughput = max(maxThroughput,throughput)
    
    return maxThroughput