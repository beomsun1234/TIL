"""
level2 - 구명보트, 섬 연결하기
DS - 투포인터

너무 쉽게 생각했다..
처음에 테스트는 모두 통과했지만 효율성 테스트 1,2,3을 통과하지 못했다....
def solution(people, limit):
    answer = 0
    people.sort()
    flag = [False] * len(people)
    if len(people) == 1:
        return 1
    for i,weight in enumerate(people):
        if not flag[i]:
            flag[i]=True
            if people[i] <= limit//2:
                for j in range(len(people)-1,i,-1):
                    if people[j] + people[i] <= limit and not flag[j]:   
                        flag[j] = True
                        break
                    else:
                        continue
            answer+=1
    return answer
당연한 것 같다 이미 탐색 완료한 자료도 탐색하기에 시간초과가 뜬다.. 끝나면 반복문 시작 위치를 바꾸어 주면 될 것같았다.. 이걸 너무 늦게 생각했다.. 20분 정도 넘게 걸린듯하다
------
수정 후 코드 이다. 정답 처리됐다~~
정말 간단했다. 처음에 정렬을 안해주고 시작했다가 [10, 20, 30, 40, 50, 60, 70, 80, 90] 이 케이스가 섞여 나올 경우를 생각했다. 그렇기에 오름차순으로 정렬해주고, 앞이랑 뒤랑 더해서 그 숫자가 limit과 같거나 작으면 반복문을 탈출했다.

자세한 로직은

flag[0],flag[1],flag[2], flag[6], flag[7],flag[8] == True # 사용했다는 뜻 

     0  1   2   3   4   5   6   7   8
   [10, 20, 30, 40, 50, 60, 70, 80, 90]
i            ^
ii                          ^
i -> people[2] =30
ii -> people[6]=70
limit = 100 >= people[2] + people[6]   True
ii = 6
투포인터 같은 느낌이다. 조건을 만족하면 ii인덱스를 옮겨준다.

time = 0(n)
space = 0(n)
---
아래는 좋은 풀이 법이고 투포인트를 이용한 풀이법 이다.
//-------------------------------
public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        int lt=0;
        int rt=people.length-1;
        while(lt<=rt) {
            int sum = people[lt]+people[rt];
            if(lt!=rt-- && sum<=limit) lt++;
            answer++;
        }
        return answer;
}
-- 파이썬 투포인터 이다
def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    if left == right:
        answer += 1

    return answer
people 오름차순 정렬

left는 0, right는 len(people) - 1의 값을 초기값으로 가짐.

남은 사람들 중, 가장 무거운 사람과 가장 가벼운 사람 무게의 합이,
3-1 limit값 이하일 경우, left는 1 더하기, right는 1 빼기
3-2 limit보다 클 경우, right만 1 빼기

3번 과정을 left가 right보다 작을 때 까지 반복하고, 매 반복 때 마다 answer에 1 더하기

반복을 마친 뒤, left가 right가
5-1 같으면, 한 명이 남은 것이니 answer에 1 더하기
5-2 left > right면, 모두 보트를 타고 나간 뒤므로 answer 그대로

"""
## 내 풀이
def solution(people, limit):
    answer = 0
    people.sort()
    flag = [False] * len(people)
    if len(people) == 1:
        return 1
    ii = len(people)-1
    for i,weight in enumerate(people):
        if not flag[i]:
            flag[i]=True
            if people[i] <= limit//2:
                for j in range(ii,i,-1):
                    if people[j] + people[i] <= limit and not flag[j]:   
                        flag[j] = True
                        ii = j
                        break
                    else:
                        continue
            answer+=1

    return answer
    
