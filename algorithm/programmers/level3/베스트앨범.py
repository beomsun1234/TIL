## 도움을 받지 않고 통과했다~~~~~~ 1시간 10분이 걸렸지만

"""
13:15 ~ 14:25
level3 베스트앨범
Input  = 노래의 장르를 나타내는 문자열 배열 genres, 노래별 재생 횟수를 나타내는 정수 배열 plays
Output =  베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return -> 정수 배열

constraints
-genres[i]는 고유번호가 i인 노래의 장르입니다.
-plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
-genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
-장르 종류는 100개 미만입니다.
-장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
-모든 장르는 재생된 횟수가 다릅니다.

DS - 딕셔너리

time  = o(n*m)
space = o(n*m)
"""
from collections import defaultdict
def solution(genres, plays):
    answer = []
    total = {} # 각 genres의 총 개수 ex) classic 장르는 1,450, pop 장르는 3,100회
    countGenres = {} #각 genres의 사용 개수 2개만 사용 가능하다.
    playMap = {}  # 내림차순으로 정렬된 재생 횟수
    ret = defaultdict(list)
    
    #o(n)
    # 인덱스별 재생 횟수 map에 저장
    for idx,play in enumerate(plays): 
        if idx in playMap:
            playMap[idx] = play
        else:
            playMap[idx] = play
    
    #내림차순 정렬
    playMap = sorted(playMap.items(),key = lambda item: item[1],reverse = True)
    
    #각 genres별 총 개수 저장(total), countGenres각 genre별 사용 횟수 초기화 후 저장(countGenres)
    o(n)
    for idx,genre in enumerate(genres):
        if genre in total:
            total[genre] = total[genre] + plays[idx] 
        else:
            countGenres[genre] = 0 
            ret[genre] = []
            total[genre] = plays[idx]
    
    # genres별 총 개수 내림차순 정렬
    total = sorted(total.items(),key = lambda item: item[1],reverse = True)
    
    #  countGenres에서 genre에 인덱스와 내림차순으로 정렬된 재생횟수의 인덱스와 같으면 해당 인덱스를 genre를 키로가지는 ret 맵에 넣어주고 1번 사용했으므로 countGenres에서 genre해당하는 value를 1증가시킨다.
    o(n*m)
    for playIdx in playMap:
        for idx,genre in enumerate(genres):
            if genre in countGenres:
                if countGenres[genre] == 2: ## 2번 사용하면 종료
                    continue
                if idx==playIdx[0]:
                    countGenres[genre]+=1
                    ret[genre].append(idx)
    
    # 내림차순으로 정렬된 genres를 저장한 total의 키(gnere)를 가지고 ret의 value를 answer에 저장해주면 끝~~~
    for i in total:
        for j in ret[i[0]]:
            answer.append(j)

    return answer
