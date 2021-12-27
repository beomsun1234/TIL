"""
LRU만 알면 정말 간단한 문제였다.. LRU는 가장 오랫동안 참조되지 않은 페이지를 교체하는 알고리즘이다.
처음에 어떤식으로 교체할지 막막했는데 LRU를 검색하니 쉽게 접근 할 수 있었다


ex) cacheSize = 3, cities ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"] 입력된 도시이름 배열을 순서대로 처리

1. Jeju 
cache = [Jeju], time = 5

2. Pangyo 
cache = [Jeju, Pangyo], time = 10

3. Seoul
cache = [Jeju, Pangyo,Seoul] time = 15

여기서 cache배열 가장 끝에 있는 요소가 가장 최근에 사용한 캐시가 된다. 만약 캐시를 사용하지 않는다면 가장 최근에 사용하지 않은 캐새인 cache리스트의 앞을 제거해 나가면 된다.
4. Jeju는 캐시에 있으며 참조되었으므로 우선순위를 변경해 주어야한다.
cache = [Jeju, Pangyo,Seoul] time = 16
우선순위 변경 로직
remove[Jeju] 
append(Jeju)
cache =  [Pangyo,Seoul, Jeju] 
....

다른 케이스를 살펴보자
ex) cacheSize = 2, cities = ["Jeju", "Pangyo", "NewYork", "newyork"]

1. Jeju 
cache = [Jeju], time = 5
2. Pangyo 
cache = [Jeju,Pangyo], time = 10
3. NewYork를 검색할 시 캐시 크기가 꽉찼으므로 캐시를 교체해줘야한다. 가장 오랫동안 참조되지 않은 캐시를 교체해주자. Jeju가 우선순위가 가장 낮으므로 Jeju를 삭제하고 [Pangyo,NewYork]으로 캐시를 변경해 주어야한다. 
cache = [Pangyo,NewYork] , time = 15

로직
if len(cache) == cacheSize:
    cache.pop(0)   # 리스트의 맨 앞 요소 제거(리스트 앞쪽부터 들어오므로 맨 앞이 우선순위가 가장 낮다)
cache.append(city)

"""
def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities)*5
    cache = []
    # 우선순위 변경
    for i in cities:
        i = i.lower()
        #캐시가 있을 경우
        if i in cache: 
            # 캐쉬 우선순위 변경을 위해 삭제 후
            cache.remove(i)
            # 맨뒤로 이동(우선순위 변경)
            cache.append(i)
            answer += 1
        else: # 캐시가 없을 경우
            ## 만약 캐시가 다 찾으면 캐시 삭제 후
            if len(cache) == cacheSize:
                cache.pop(0) #앞에있는 캐쉬 삭제
            # 해당 도시 캐시 추가
            cache.append(i)
            answer += 5
    print(cache)
    return answer