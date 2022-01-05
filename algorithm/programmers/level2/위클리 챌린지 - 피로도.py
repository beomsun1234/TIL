"""

프로그래머스 level2 - 위클리 챌린지 - 피로도

처음에 순열을 생각했지만 더 좋은 방법이 없을까 하다가 정렬을 생각했었다.. 바로 정렬로 접근했다 소모피로도로 정렬하고 같을 경우 최소 피로도로 정렬해줬다.
테케 통과하고 제출하니 39점인가 맞았다.. 당연했다..  [80,20],[50,40],[30,10] 이 경우 정렬하면 [30,10],[80,20],[50,40] 이 나외서 2번만 돌 수 있었다..

결국 처음 방법인 순열로 접근했다. 정말 간단했다 던전의 탐헌 순서를 뽑아서 해당 탐헌 순서로 탐험 할 경우의 횟수를 리턴하고 최대값을 구해주면 됐다.

..
cnt = 0
#소모 피로도로 정렬 후 같으면 최소 피로도로 정렬
dungeons = sorted(dungeons,key = lambda x : (x[1], x[0]))
# 현재 피로도 k
for dungeon in dungeons:
    #0번인덱스 - 최소 피로도, 1번 - 소모피로도
    if dungeon[0] > k : # 현재 피로도가 최소 피로도보다 크면
        continue
    if k < dungeon[1]: # 현재 피로도가 최소 피로도보다 크지만 현재피로도가 소모피로도보다 작으면
        print(k)
        break
    ## 위 조건에 부합하지 않으면 던전 갈 수 있다.
    cnt+=1 # 던전 간 횟수 
    k = k-dungeon[1] # 피로도 감소

return cnt
처음 생각인 조합으로 접근하자
"""

# 리턴 던전 탐험 횟수
def getDungeonCount(idxs,dungeons,k):
    ret = 0
    pirodo = k
    for idx in idxs:
        if dungeons[idx][0] > pirodo: # 현재 피로도가 최소 피로도보다 크면
            continue
        if pirodo < dungeons[idx][1]: # 현재 피로도가 최소 피로도보다 크지만 현재피로도가 소모피로도보다 작으면
            break
        pirodo = pirodo-dungeons[idx][1] # 피로도 감소
        ret+=1 # 탐험횟수 카운트
    return ret

#탐험할 던전 순서 뽑기
def dfs(pick,visited, idxs,dungeons,k):
    global answer
    if pick == len(dungeons):
        answer = max(answer,getDungeonCount(idxs,dungeons,k))
        return
    for i in range(len(dungeons)):
        if not visited[i]:
            idxs.append(i)
            visited[i] = True
            dfs(pick+1,visited,idxs,dungeons,k)
            idxs.pop()
            visited[i] = False

def solution(k, dungeons):
    global answer
    answer = 0
    visited = [False] * len(dungeons)
    idxs = []
    # dfs(pick,visited, idxs,dungeons,k)
    dfs(0,visited,idxs,dungeons,k)
        
    return answer
    