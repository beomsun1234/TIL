## 소문난 칠공주 1941
#총 25명의 여학생들로 이루어진 여학생반은 5*5의 정사각형 격자 형태로 자리가 배치되었고, 
# 얼마 지나지 않아 이다솜과 임도연이라는 두 학생이 두각을 나타내며 다른 학생들을 휘어잡기 시작했다.
# 곧 모든 여학생이 ‘이다솜파’와 ‘임도연파’의 두 파로 갈라지게 되었으며, 
# 얼마 지나지 않아 ‘임도연파’가 세력을 확장시키며 ‘이다솜파’를 위협하기 시작했다.
# 위기의식을 느낀 ‘이다솜파’의 학생들은 과감히 현재의 체제를 포기하고, 
# ‘소문난 칠공주’를 결성하는 것이 유일한 생존 수단임을 깨달았다. 
# ‘소문난 칠공주’는 다음과 같은 규칙을 만족해야 한다.
# 1.이름이 이름인 만큼, 7명의 여학생들로 구성되어야 한다.
# 2. 강한 결속력을 위해, 7명의 자리는 서로 가로나 세로로 반드시 인접해 있어야 한다.
# 3. 화합과 번영을 위해, 반드시 ‘이다솜파’의 학생들로만 구성될 필요는 없다.
# 4. 그러나 생존을 위해, ‘이다솜파’가 반드시 우위를 점해야 한다. 
#    따라서 7명의 학생 중 ‘이다솜파’의 학생이 적어도 4명 이상은 반드시 포함되어 있어야 한다.
# 여학생반의 자리 배치도가 주어졌을 때, ‘소문난 칠공주’를 결성할 수 있는 모든 경우의 수를 구하는 프로그램을 작성하시오.
from collections import deque
import sys
input = sys.stdin.readline
# y= 임도연파  s = 이다솜파
class_room =[list(str(input().strip())) for _ in range(5)]
check_student=[False]*25
visted =[[False]*5 for _ in range(5)]
n=5
result=0
dx=[1,-1,0,0] #상하
dy=[0,0,1,-1]
def check_count_S(): # 4개이상이면
    cnt=0
    for i in range(25):
        if check_student[i]==True:
            x= i//5
            y= i%5
            if class_room[x][y]=='S':
                #print('s발견')
                cnt+=1
    if cnt>=4:
        return True
    else:
        return False

def check_adjust(): #인접한거찾기
    q_select =[[False]*5 for _ in range(5)] # 계속 q방문을 초기화해줘야함
    q=[]
    answer=False
    q=deque()
    Tmp=0
    for i in range(25):  # 뽑은 학생중에 앞에 하나 뽑고 
        if check_student[i]==True:
            x=i//5
            y=i%5
            q.append((x,y))
            q_select[x][y]=True
            break
    ck=1
    while q:  #인접한지 확인
        cur_x,cur_y= q.popleft()
        for way in range(4):
            nx = cur_x+dx[way]
            ny = cur_y+dy[way]
            if nx>=0 and ny>=0 and nx<5 and ny<5:
                if  q_select[nx][ny]==False and visted[nx][ny]:
                    q_select[nx][ny]=True
                    q.append((nx,ny))
                    ck+=1  
    if ck==7:
        return True
    return False
    

def pick_student(cur,pick,n): # 현재 학생번호, 픽획수, 길이를 매개변수로 하여 7명 학생뽑기
    global result
    if pick == 7: 
        if check_count_S():
            if check_adjust():
                result+=1
        return 1
    # 뽑기
    for i in range(cur,25):
        if check_student[i]==True and visted[i//5][i%5]:
            continue
        visted[i//5][i%5]=True
        check_student[i]=True # 뽑음
        pick_student(i,pick+1,n) # 다음학생 뽑기
        check_student[i]=False
        visted[i//5][i%5]=False

            

pick_student(0,0,n)

print(result)