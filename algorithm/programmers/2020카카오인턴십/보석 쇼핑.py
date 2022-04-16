"""

프로그래머스 보석쇼핑(2020카카오 인턴십)


진열대 번호 : 1 2 3 4 5 6 7 8
인덱스 번호 : 0 1 2 3 4 5 6 7
보석의 종류 : D R R D D E S D

start = 0   end = 0   구간안에있는 보석 : []
start = 0   end = 1   구간안에있는 보석 : [D]
start = 0   end = 2   구간안에있는 보석 : [D, R]
start = 0   end = 3   구간안에있는 보석 : [D, R, R]
start = 0   end = 4   구간안에있는 보석 : [D, R, R, D]
start = 0   end = 5   구간안에있는 보석 : [D, R, R, D, D]
start = 0   end = 6   구간안에있는 보석 : [D, R, R, D, D, E]
start = 0   end = 7   구간안에있는 보석 : [D, R, R, D, D, E, S] 조건만족: O
start = 1   end = 7   구간안에있는 보석 : [D, R, R, D, D, E, S] 조건만족: O
start = 2   end = 7   구간안에있는 보석 : [R, R, D, D, E, S]    조건만족: O
start = 3   end = 7   구간안에있는 보석 : [R, D, D, E, S]       조건만족: O
start = 4   end = 7   구간안에있는 보석 : [D, D, E, S]          조건만족: X

배열의 left 와 right 구간이 “모든 종류의 보석을 포함하는 구간”이 될 때 까지 right 인덱스를 증가시킨다. 이후 
“구간 중 가장 짧은 구간” 을 구해야 하기 때문에 start 인덱스를 하나씩 증가시켜보며 구간의 길이를 줄여본다. 
줄어든 구간이 “모든 종류의 보석을 적어도 1개 이상 포함” 한다는 조건을 만족시키면 left , right 를 저장하고, 
조건이 만족되지 않을 때까지 구간의 길이를 줄인다.
현재 구간이 조건을 만족시키지 않는다면 다시 end 인덱스를 증가시키면서 구간을 탐색한다.




"""
from collections import defaultdict
def solution(gems):
    answer = [0,0]
    kind = set()
    for i in gems:
        kind.add(i)
    kind_len = len(kind)
    gem_dict = defaultdict(int)
    candidate = []
    left, right = 0,0
    while 1:
        now_kind = len(gem_dict)
        
        #시작지점이 끝이면 종료
        if left == len(gems):
            break
            
        ##모든 종류의 보석이 있다면 시작점을 옮겨서 구간탐색(left+1)
        if now_kind == kind_len:
            candidate.append((left+1,right))
            #이전 시작지점 제거
            gem_dict[gems[left]] -=1
            if gem_dict[gems[left]] == 0:
                del gem_dict[gems[left]]        
            left+=1
            continue
        if right == len(gems):
            break
        ## 현재 보석의 종류의 개수가 총 보석의 개수와 같지 않다면 구간에 보석 종류 추가
        if now_kind != kind_len:
            #보석종류 추가
            gem_dict[gems[right]] +=1
            #구간 늘리기
            right+=1
            continue
    min_val = 1000000
    for c in candidate:
        if min_val > c[1] - c[0]:
            min_val = c[1] - c[0]
            answer[0] = c[0]
            answer[1] = c[1]
    return answer
    