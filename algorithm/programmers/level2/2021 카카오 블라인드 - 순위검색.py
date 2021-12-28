"""

이 코드는 정확성은 다 맞으나 효율성에서 시간 초과가 발생했다... 쉽다고 생각해서 제한사항을 읽어보지도 않고 풀었다.. info의 배열의 크기가 1<=size<=50000 이기에 시간초과를 생각하고 풀어야했다... 아직 초보라 그런가 시간을 단축시킬 방법으 떠오르지 않았다.. 카카오 기술블로그와 다른 브로그를 보고 풀었다..
info에 대한 모든 조합을 만들어준다. ex) java , javabackend, javabackendjunior ...로 16가지의 경우의 수가 만들어진다. -를 고려하는 경우 따로 '-' 를 넣어주지 않고 info조건을 모아 key를 만듬. ex) python - junior pizza -> pyhonjuniorpizza로 변경해 준다. info를 통해 만들어진 조합을 map에 key로하고 value를 info에 score값으로 해준다. 이제 해당 map에 있는 정보와 query조건이 일치하는 경우 query스코어보다 높은 점수의 지원자가 몇명인지 구한다(lower_bound(이진탐색이용))


import re
def solution(info, query):
    answer = []
    infoList = []
    queryList = []
    # 정보
    for i in info:
        infoList.append(i.split(" "))
    # 검색조건
    for i in query:
        reg = re.findall('\d+|\w+|[-]+',i)
        for j in reg:
            if j == 'and':
                reg.remove(j)
        queryList.append(reg)
    cc = 0
    for i in queryList:
        print(i)
        for j in infoList:
            cnt = 0
            for k in range(len(infoList[0])):
                # 숫자 체크
                regNum = re.findall('\d+',j[k])
                if j[k] == i[k]:
                    cnt +=1   
                elif i[k] == '-':
                    cnt+=1
                elif regNum:
                    if int(j[k]) >= int(i[k]):
                        cnt+=1
            if cnt == len(infoList[0]):
                cc +=1
        answer.append(cc)
        cc = 0
    return answer

"""
from itertools import combinations
import re
def solution(info, query):
    answer = []
    ret = []
    map = {}
    for i in info:
        infoList = i.split( )
        key = infoList[:-1]
        score = int(infoList[-1])
        for j in range(5):
            for c in combinations(key,j): # info들의 조합을 뽑는다(ex java, javabackend ... )
                tmp = ''.join(c)
                if tmp in map:
                    map[tmp].append(score) # map에 해당 score를 넣는다
                else:
                    map[tmp] = [score]
    for k in map:
        map[k].sort()  # dict안의 조합들을 점수순으로 정렬
        
    # 쿼리정보도 똑같이 분리해준다.
    for i in query:
        queryList = i.split(' ')
        scoreQ = int(queryList[-1])
        queryList = queryList[:-1]
        while 'and' in queryList:
            queryList.remove('and')
        while '-' in queryList:
            queryList.remove('-')
        key = "".join(queryList)
        if key in map: #info의 조합이 key인 map에 쿼리정보가 있다면 
            scores = map[key] # 스코어를 가져온다.
            if len(scores) > 0: # lower_bound
                start, end = 0, len(scores)
                # 정렬된 배열에서 찾고자하는 값 이상이 처음 나타나는 위치 찾기
                while start < end: #start와 end가 만나는 지점이 target값 이상이 처음 나오는 위치
                    mid = (start+end) // 2
                    if scores[mid] >= scoreQ:
                        end = mid
                    else:
                        start = mid+1
                answer.append(len(scores)- start)
        else:
            answer.append(0)

    return answer
