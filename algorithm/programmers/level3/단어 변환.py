"""
Level 3 단어 변환 dfs

Input  - 두 개의 단어 begin, target-> String , 단어의 집합 words -> 1차원 문자 배열
Output -  begin을 target으로 변환할 수 있는 최소 횟수 

Constraints 
- 각 단어는 알파벳 소문자로만 이루어져 있습니다.
- 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
- words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
- begin과 target은 같지 않습니다.
- 변환할 수 없는 경우에는 0를 return 합니다.

edge case
  - words배열에 target이 없을 경우 ex) 테스트 케이스 2번
    0을 리턴한다.

DS - DFS

1   - begin으로 주어진 단어를 가지고 words에 배열과 비교하여 begin단어의 1글자만 바꿔서 words의 배열에 주어진 단어가 되면 begin을 바꿔주면서 탐색을 진행한다. 순열과 비슷하다.

1.1 - begin를 교체하기 위해 words중에서 탐색 할 단어와 현재 begin을 비교해서 만약 다른 문자가 1개일 경우 true를 주고 나머지는 false를 준다.

1.2 - 두문자를 비교해서 true을 경우 cnt를 증가해시켜주고 탐색을 진행한다.

2   -  visited 배열을 선언해 주고 방문 한 고을 다시 방문하지 않도록 한다. 여기서 방문된 값을 빼고 계속 처리해야한다. 여기서 주의 할 점은
1번 예시에서 정답 후보는 아래와 같다
    1. hot - dot - dog - cog = 4
    2. hot - dot - lot - log - cog = 5
    3. hot - lot - log - cog = 4
탐색하고 나서 백트래킹을 하지 않으면(visited를 풀어주지 않으면) 2.이 먼저 나올 경우, 1.을 체크 할 수 없다..

3. 만약 현재 begin이 target이면 count값을 리턴해준다.

4. 탐색하면서 최소 변환 횟수를 저장하고 return 하면 된다.

# tip 순열과 비슷한 문제이다.

time - O(n) 


"""


def compareWords(nowWord, compareWord):
        difference = 0
        for i in range(len(nowWord)):
            if nowWord[i] != compareWord[i]:
                difference +=1
        if difference == 1:
            return True
        return False

def dfs(begin,target, words,visited,count):
    global minVale
    for i in range(len(words)):
        if not visited[i] and compareWords(begin, words[i]):
            visited[i] = True
            minVale = min(minVale,dfs(i,words[i],target, words, visited, count+1))
            visited[i] = False
    if begin == target:
        return count
    
    return minVale
    
def solution(begin, target, words):
    answer = 0
    global minVale 
    if not target in words:
        return 0
    visited = [False] * len(words)
    minVale = 100000
    dfs(begin ,target, words,visited,0)
    print(minVale)
    return minVale
    