"""
프로그래머스 level4 - 징검다리
"""

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    #돌사이의 거리 최솟값 
    left = 1
    #최악의 경우 가장 먼 거리의 거리값
    right = distance
    
    while left <= right:
        
        #돌 사이의 거리의 값
        mid = (left+right) // 2
        #거리
        prev_rock = 0
        remove_cnt = 0
        
        for rock in rocks:
            #돌의 거리가 현재 설정한 돌 사이의 거리보다 작으면
            # 제거하지
            if rock - prev_rock < mid:
                remove_cnt +=1
            else:
                prev_rock = rock
            #n개보다 초과되서 삭제됐다면 종료
            if remove_cnt > n:
                break

        #삭제한게 n개 초과라면
        if remove_cnt > n:
            #최대값 갱신
            right = mid-1
        else:
            #삭제했다면
            answer = mid
            # 최솟값 갱신
            left = mid+1 
            
    return answer