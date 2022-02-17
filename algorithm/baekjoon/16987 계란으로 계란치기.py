"""
16987 계란으로 계란치기


"""

N = int(input())
egg = []
for i in range(N):
    d,w = map(int,input().split())
    egg.append([d,w])
global answer
answer = -100000
def dfs(pick):
     global answer
     # 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우
     if pick == N:
          cnt = 0
          for i in egg:
               if i[0] <=0:
                    cnt+=1
          answer = max(answer,cnt)
          return
     
     # 현재 손에 든 계란이 깨졌다면 다음계란 손에 든다
     if egg[pick][0] <=0:
          dfs(pick+1)
          return
     else:
          flag = False
          for i in range(N):
               if i!= pick and egg[i][0] >0:
                    # 손에든 계란쳐서 내구도 감소
                    egg[pick][0] -= egg[i][1] 
                    # 친 계란 내구도 감소
                    egg[i][0] -= egg[pick][1]
                    flag = True
                    dfs(pick+1)
                    #되돌리기
                    egg[pick][0] += egg[i][1] 
                    #되돌리기
                    egg[i][0] += egg[pick][1]
          # 깰 계란이 없다면 마지막으로 이동
          if not flag:
               dfs(N)
               return

dfs(0)
print(answer)