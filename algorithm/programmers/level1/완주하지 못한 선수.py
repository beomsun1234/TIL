"""
level 1 -> 완주하지 못한 선수
"""
def solution(participant, completion):
    answer = ''
    map = {}
    for i in completion:
        if i in map:
            map[i] = map[i]+1
            print(i)
        else:
            map[i]=1
    print(map)
    for i in participant:
        if i not in map: ## 중복 없을때
            return i
        if map[i] == 0:  ## 중복 있을때
            return i
        map[i] = map[i]-1
    return answer