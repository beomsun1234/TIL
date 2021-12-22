"""
카카오 블라인드 - 뉴스클러스터링
합집합을 만드는 부분이 가장 헷갈렸다..

str1을 세팅해놓고 str2를 넣어보면서 같은 값이면 str1을 복사해둔 candidate의 값을 제거하고 아니면 합집합 배열에 값을 넣어준다 완성해 나간다. 

"""

def makeGroup(str):
    ret = []
    check = re.compile('[a-z]')
    for idx in range(0,len(str)-1):
        if len(check.findall("".join(str[idx:idx+2])))==2:#두개다 a~z일 경우
            ret.append("".join(str[idx:idx+2]))
    return ret
def changeLower(str):
    str = str.lower()
    return str
import re
def solution(str1, str2):
    answer = 0
    str1 = changeLower(str1)
    str2 = changeLower(str2)
    gstr1 = makeGroup(str1)
    gstr2 = makeGroup(str2)
    ## 합집합 = max, 교집합은 min
    mapStr1 = {}
    for i in gstr1:
        if i in mapStr1:
            mapStr1[i] +=1
        else:
            mapStr1[i] = 1
    ## 교집합
    ii = []
    for i in gstr2:
        if i in mapStr1 and mapStr1[i]>0:
            mapStr1[i]-=1
            ii.append(i)
    ## 합집합
    condidates = gstr1.copy()
    u = gstr1.copy()
    for i in gstr2:
        if i not in condidate:
            u.append(i)
        else:
            condidate.remove(i)
    if len(u) ==0: ## 합집합이 0이면 
        return 65536
    return int((len(ii)/len(u) * 65536))