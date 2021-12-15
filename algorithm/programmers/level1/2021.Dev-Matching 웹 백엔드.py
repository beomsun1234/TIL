"""
level 1
2021 Dev-Matching: 웹 백엔드 

Input  = 민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums
Output = 이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return

constrints 
- lottos는 길이 6인 정수 배열입니다.
- lottos의 모든 원소는 0 이상 45 이하인 정수입니다.
- 0은 알아볼 수 없는 숫자를 의미합니다.
- 0을 제외한 다른 숫자들은 lottos에 2개 이상 담겨있지 않습니다.
- lottos의 원소들은 정렬되어 있지 않을 수도 있습니다.
- win_nums은 길이 6인 정수 배열입니다.
- win_nums의 모든 원소는 1 이상 45 이하인 정수입니다.
- win_nums에는 같은 숫자가 2개 이상 담겨있지 않습니다.
- win_nums의 원소들은 정렬되어 있지 않을 수도 있습니다.
DS - 완탐


time - O(n)
"""

def changeRank(cnt):
    if cnt == 6:
        return 1
    elif cnt == 5:
        return 2
    elif cnt == 4:
        return 3
    elif cnt == 3:
        return 4
    elif cnt == 2:
        return 5
    else:
        return 6
def solution(lottos, win_nums):
    answer = []
    zeroCnt = lottos.count(0)
    if zeroCnt == len(win_nums):
        return [1,6]
    
    cnt = 0
    for num in lottos:
        if num in win_nums:
            cnt+=1
    
    ## 다 맞추면 항상 1등
    if cnt == 6:
        return [1,1]
    
    return [changeRank(cnt+zeroCnt), changeRank(cnt)]