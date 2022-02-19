"""
3967 - 매직 스타

조금 노가다 스러웠지만 간단했다.. "마지막에 사전순으로 정렬해서 가장 앞선 순서를 출력해야한다"라는 문구를 보고 만들 수 있는 방법들을 정렬 하고 그 중 앞선 순서를 출력하여 제출하였더니 22% 시간초과가 발생했다..
정렬 코드를 지우고 제일 처음 만들어지는 방법을 출력하니 성공 할 수 있었다..

나의 풀이는 이렇다. 
뽑는 순서가 중요하다고 생각해서 순열을 생각했다. 
알파벳 순열을 숫자로 표현하였고 이를 변환해주는 함수 두개 만들어 주었다.
처음에 주어진 알파벳들을 방문 표시해서 사용하지 못하도록 한다.
이 후 숫자가 비어있는 칸에서 만들수 있는 순열을 구한다. 뽑은 순열을 알파벳으로 변환해서 그리드에 그려주고 매직스타가 만들어 지는 체크했다. 


1 ~ 12
r = 5
c = 9
"""

N = 5
grid = []
for i in range(5):
    data = input()
    grid.append(list(data))
x_cnt = 0
x_pos = []
# 0부터 ~ 12 [ A ~~ L]
visited = [False] * 12
answer = []

def convertAlpha(num):
    if num == 0:
        return 'A'
    if num == 1:
        return 'B'
    if num == 2:
        return 'C'
    if num == 3:
        return 'D'
    if num == 4:
        return 'E'
    if num == 5:
        return 'F'
    if num == 6:
        return 'G'
    if num == 7:
        return 'H'
    if num == 8:
        return 'I'
    if num == 9:
        return 'J'
    if num == 10:
        return 'K'
    if num == 11:
        return 'L'

def convertNum(alpha):
    if alpha == 'A':
        return 0
    if alpha == 'B':
        return 1
    if alpha == 'C':
        return 2
    if alpha == 'D':
        return 3
    if alpha == 'E':
        return 4
    if alpha == 'F':
        return 5
    if alpha == 'G':
        return 6
    if alpha == 'H':
        return 7
    if alpha == 'I':
        return 8
    if alpha == 'J':
        return 9
    if alpha == 'K':
        return 10
    if alpha == 'L':
        return 11

for i in range(5):
    for j in range(9):
        if grid[i][j] == 'x':
            x_cnt +=1
            x_pos.append((i,j))
        if grid[i][j] != 'x' and grid[i][j] != '.':
            visited[convertNum(grid[i][j])] = True

combi = []

## 대입한 순열을 계산하여 매직스타 조건이 부합하는지 체크 숫자 4개로 이루어진 줄의 합이 26이 되는지
def is_ok(tmp):
    # 대각선 왼쪽 기준(컬럼 4에서 시작)
    now_c = 4
    val = 0
    for i in range(4):
        val += convertNum(tmp[i][now_c])
        now_c-=1
    if val+4 != 26:
        return False
    # 바텀 라이트
    val = 0
    for i in range(1,9,2):
        val +=convertNum(tmp[3][i])
    if val+4 != 26:
        return False
    # 바텀 대각선으로 업
    val = 0
    now_c = 7
    for i in range(3,-1, -1):
        val += convertNum(tmp[i][now_c])
        now_c -=1
    if val+4 != 26:
        return False
    ## ---- 거꾸로된 삼각형
    val = 0
    now_c = 1
    # 대각선 라이트 다운 r =1 c =1 에서 시작
    for i in range(1,5):
        val += convertNum(tmp[i][now_c])
        now_c+=1
    if val+4 != 26:
        return False
    # 대각선 라이트 업
    val = 0
    now_c = 4
    for i in range(4,0,-1):
        val += convertNum(tmp[i][now_c])
        now_c+=1
    if val+4 != 26:
        return False
    # 탑 레프트
    val = 0
    for i in range(7,0, -2):
        val += convertNum(tmp[1][i])
    if val+4 != 26:
        return False
    ret = ''
    for i in tmp:
        ret+= ''.join(i)
    answer.append(ret)
    # 다 통과하면
    return True

## 뽑은 순열을 바탕으로 x에 대입한다.
def apply_perm(combi):
    tmp = grid
    for idx, pos in enumerate(x_pos):
        tmp[pos[0]][pos[1]] = str(convertAlpha(combi[idx]))
    return tmp
# x의 순열을 뽑는다.
def dfs(pick):
    if pick == x_cnt:
        if is_ok(apply_perm(combi)):
            for i in range(0,45, 9):
                print(answer[0][i:i+9])
            exit(0)
        return
    for i in range(12):
        if not visited[i]:
            visited[i] = True
            combi.append(i)
            dfs(pick+1)
            visited[i] = False