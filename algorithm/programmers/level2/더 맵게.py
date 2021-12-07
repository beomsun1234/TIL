import heapq
"""
더 맵게
level 2
Input = Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville, 원하는 스코빌 지수 K
OutPut = 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수


섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)


constraints
- scoville의 길이는 2 이상 1,000,000 이하입니다.
- K는 0 이상 1,000,000,000 이하입니다.
- scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
- 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

DS - 힙 큐

1. 주어진 스코빌 지수를 heap으로 만들어준다.
2. 스코빌지수에서 K보다 작은것이 있을때까지 반복문을 돌려준다
3. k보다 작을 경우 음식을 섞어 스코빌 지수를 높여야한다.
4. 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)공식을 사용해서 heap에서 값 두개를 빼온다.
5. 빼온 값중 첫번째는 가장 맵지 않은 스코빌 지수이고 두번째로 빼온것은 두 번째로 맵지 않은것이 된다.
6. 해당 값을 공식에 대입하여 heap에 다시 넣어준다.
7. 위 과정을 반복하고 만약 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 하는 조건을 걸어준다. 현재 힙의 길이가 1나만 남고 그 값이 k보다작으면 k이상으로 만들 수 없다.

time = 최고 O(1), 최악 O(n)
## 회고
7번 과정인 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 하는 조건을
생각하지 못해서 테스트케이스 1,3,8을 통과하지 못했다.. 생각이 않나서 도움을 받아서 해결 할 수 있었다. 아직 스킬이 부족한 것 같다
"""
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        val1 = heapq.heappop(scoville)
        val2 = heapq.heappop(scoville)
        heapq.heappush(scoville,val1 + (val2*2)) 
        answer+=1
        if len(scoville) ==1 and scoville[0] < K:
            return -1
    
    return answer
    