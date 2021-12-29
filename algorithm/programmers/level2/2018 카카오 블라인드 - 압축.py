"""
2018 카카오 블라인드- 압축

현재글자 + 다음글자가 사전에 없다면 w = c , c = c + 1
현재글자 + 다음글자가 사전에 있다면 w는 변화없음, c = c + 1

"""
def solution(msg):
    answer = []
    map = {}
    
    # 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
    for i in range(1,27):
        map[chr(64+i)] = i
    
    # 문자열 w 찾기
    w, c =0,0
    while True:
        # 만약 map에 있다면 다른 문자열를 찾는다
        c+=1
        if c == len(msg):
            answer.append(map[msg[w:c]])
            break
        # map에 없다면 즉 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
        if msg[w:c+1] not in map:
            print(msg[w:c+1], msg[w:c])
            map[msg[w:c+1]] = len(map) +1
            answer.append(map[msg[w:c]])
            w = c
    return answer