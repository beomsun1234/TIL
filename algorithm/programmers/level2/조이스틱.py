"""
level2 그리디 조이스틱

Input = 만들고자 하는 이름 name -> String, 
Output = 조이스틱 조작 횟수의 최솟값을 

Constrints
- name은 알파벳 대문자로만 이루어져 있습니다.
- name의 길이는 1 이상 20 이하입니다.

EdgeCase
- name  = AAA, AAAA 일경우 return 0
 if name.count('A') == len(name): #전부 A일 경우 return 0
        return 0


DS - 완전탐색??

time = O(2N) -> O(N)
space = O(N)

처음 보자마자 bfs가 생각났다... bfs로 접근하려고 했는데 문제를 자세히 보니 조이스틱 위,아래 일경우 패턴이 보였다. 주어진 문자가 알파벳 O보다 큰 경우는 Z에서부터 시작해야 빠르고, 작을 경우 A에서 부터 시작해야 빠르다
로직은 아래와 같다.
if alphabet < 'O':
            answer += ord(alphabet) - 65
        else:
            answer += 91-ord(alphabet)

가장 어려웠던 커서 이동문제가 남았다. 위아래의 최소값은 구했으니 커서가 남았다..

처음에는  	"JEROEN" 이 경우만 생각해서 minMoveCusor값을 len(name)-1으로 초기화 하여 해당 경우는 해결 할 수 있었는데 나머지 경우가 생각이 안났다..

 도저히 생각을 해도 접근 방법이 떠오르지 않았다... 모든 경우의 수를 다 돌아 볼까도 생각해 보았다.. 그래도 방법이 떠오르지 않았다.. 다른사람의 풀이를 보아도 이해가 되지 않았다.. 역시 손으로 풀어보니 이해가 됐다

ex)
2가지 경우가 있다
1) 왼쪽에서 시작해서 오른쪽으로 한방향으로만 이동하는 경우 
2) 왼쪽에서 시작해서 오른쪽으로 이동하다가 방향을 바꾸어 왼쪽으로 이동하는 경우

 왼쪽에서 오른쪽으로 한방향으로 갈 경우 len(name)-1 이다
 하지만 왼쪽에서 시작해서 오른쪽으로 이동하가 방향을 바꾸어 이동하는 경우는
 특정 문자까지 이동한 후(해당 문자의 인덱스) 다시 처음 글자로 되돌아가(+ 해당 문자의 인덱스) 연속된 A문자의 다음 문자까지 마지막 위치에서부터 거꾸로 이동(+ 문자열 길이 - 연속된 A문자가 끝나는 위치 + 1)하면 된다.
 
 BAAAB     -> idx = 0
 ^         -> 연속된 A가 끝나는 위치 = 4
           거꾸로 가서 B를 변경 할 경우 idx+len(number)-finshedA+idx = 1
           한쪽으로 쭉 가서 B를 변경 할 경우 = 4
           
    
"""
def solution(name):
    answer = 0
    minMoveCusor = len(name)-1;  
    if name.count('A') == len(name): #전부 A일 경우 return 0
        return 0
    ## 위,아래 조작 횟수 저장, 알파벳 O를 기준으로 O보다 작으면 A부터 시작해야 최소횟수 같거나 크면 Z+1 부터 시작해야 최소횟수 
    for alphabet in name:
        if alphabet < 'O':
            answer += ord(alphabet) - 65
        else:
            answer += 91-ord(alphabet)
    ## 커서 조작
    for idx,alphabet in enumerate(name):
        next = idx+1
        while (next < len(name) and name[next] == 'A'):
            next+=1 # 현재 위치 이후 연속된 A 다음의 문자를 가리킴
        
        print(next,idx)
        print(idx+len(name)-next+idx)
        minMoveCusor = min(minMoveCusor, idx+len(name)-next+idx) # 한 방향으로만 이동하는 경우와, 오른쪽으로 이동했다가 왼쪽으로 이동하는 경우를 비교
        print(minMoveCusor)
        print('--------------------')
        
    return answer + minMoveCusor