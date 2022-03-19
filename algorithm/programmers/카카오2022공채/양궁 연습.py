"""
프로그래머스 2022 KAKAO BLIND RECRUITMENT 양궁 연습

간단했다.. 중복 조합이 아닌 중복 순열을 만드는 방법으로 하다가 시간 많이 날렸다.. 계속 3,4 케이스가 시간 초과가 나길래 dfs코드를 살펴보니... 나는 분명 조합으로 접근했는데 순열이었다..
하.. 이것 때문에 시간 진짜 많이 날려먹었다... 다시 코드를 조합을 구하는 식으로 바꾸니 나머지는 정말 간단했다.. 로직은 이렇다.

우선 dfs를 통해 내가 얻을 수 있는 점수의 조합을 구한다.. 여기서 주어진 문제는 범위로는 가지치기를 안해도 돌아가지만 시간 효율을 고려하여 라이언이 쏜 타켓의 인덱스의 개수가 어피치가 쏜 타켓의 인덱스 수보다 작거나 같을 경우만 돌아가게 하면 최적화를 할 수 있다.
예를 들어 어피치가 10점을 2번 쐈다면, 라이언은 10점을 3번 이상만 쏘면 이길 수 있다. 가장 이상적인 횟수는 3이 될 것이다. 그러기 위해서는 어피치가 쏜 해당 타켓의 개수보다 같거나 작을 경우만 쏜 걸로 치면 된다.
이렇게 모든 조합을 구하고 구한 조합으로 point를 계산한다. 만약 라이언이 점수를 얻기 위해서는 어피치보다 많이 쏴야한다. 즉 해당 인덱스를 맞춘 개수가 어피치가 쏜 해당 타켓의 개수보다 많아야 라이언이 얻는다.
라이언이 점수를 얻었다면 라이언에 포인트를 적립하고, 어피치가 이겼다면 어피치에 포인트를 적립해준다. 이 후 라이언의 포인트와 어피치의 획득한 포인트를 비교해서 라이언이 이길 경우의 둘의 포인트차를 구해준다.
해당 포인트 차가 가장 큰 값을 구하면 된다. 여기서 주의 할 점은 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우 리턴해주어야한다.
이 부분은 포인트의 조합을 구할 때 낮은 포인트 부터 조합을 구하면 해결 가능하다.

"""
import copy
#라이언, 어피치 포인트 계산
def cal_point(lion_shots, info):
    #0인덱스 10점, 1->9점 .... 0
    lion_point = 0
    appech_point = 0
    for idx in range(11):
        #라이언이 이기기 위해서는 어피치보다 많이 쏴야함
        if lion_shots[idx]!=0 or info[idx]!=0:
            if lion_shots[idx] > info[idx]:
                lion_point += 10-idx
            else:
                appech_point += 10-idx
    return  lion_point, appech_point

def get_dif_win_lionPoint(lion_point,appech_point):
    dif = 0
    if lion_point > appech_point:
        dif = lion_point - appech_point
        return dif
    return 0
     
#낮은 점수부터 중복 조합을 통해 경기당 얻을 수 있는 점수를 구한다.
def dfs(pick,n,lion_shots,info,idx):
    global answer
    global max_val
    if pick == n:
        lion_point, appech_point = cal_point(lion_shots,info)
        dif = get_dif_win_lionPoint(lion_point,appech_point)
        if dif == 0:
            return
        if dif > max_val:
            max_val = dif
            answer = copy.deepcopy(lion_shots)
        return
    for i in range(idx,-1,-1):
        if lion_shots[i] <= info[i]:
            lion_shots[i] +=1
            dfs(pick+1,n,lion_shots,info,i)
            lion_shots[i] -=1

def solution(n, info):
    global answer
    global max_val
    answer = []
    max_val = -1
    lion_shots = [0] * 11
    dfs(0,n,lion_shots,info,10)
    if answer == []:
        return [-1]
    return answer