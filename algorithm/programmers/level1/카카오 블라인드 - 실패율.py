"""
카카오 블라이든 - 실패율
쉽게 풀긴 풀었는데 TimeLimit에서 간당간당한 느낌이 든다.. 좀더 효율적인 방법을 고려해봐야겠다

정말 효율성있게 푸신 분을 보았다...

import collections

def solution(N, stages):
    stop = collections.Counter(stages)
    fail = collections.defaultdict(float)

    fail[1] = len(stages)
    for i in range(1, N + 1):
        if fail[i] != 0:
            fail[i + 1] = fail[i] - stop[i]
            fail[i] = stop[i] / fail[i]

    if N + 1 in fail:
        del fail[N + 1]
    return sorted(fail, key=lambda x: -fail[x])
반복문을 통한 list.count()는 시간복잡도 O(n2 )으로 풀이시간이 낭비됨
collections.Counter()로 한번에 종합하면 시간복잡도 단축
"""
def solution(N, stages):
    answer = []
    ret = 0
    map = {}
    stageInPeople = len(stages)
    for i in range(1,N+1):
        if stages.count(i)==0:
            map[i] = 0 
        else:
            map[i] = stages.count(i)/stageInPeople 
        stageInPeople -=stages.count(i)
    map=sorted(map.items(), key=lambda x: x[1],reverse = True)
    for key in map:
        answer.append(key[0])
    return answer
    
