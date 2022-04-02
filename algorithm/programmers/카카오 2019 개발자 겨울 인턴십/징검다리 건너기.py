"""
프로그래머스 2019 카카오 개발자 겨울 인턴십 징검다리 건너기

이분탐색으로 접근했지만 정확성만 통과했다... 이유는 건널 수 있는 사람을 정해서 해당인원이 모두 건널수 있는지 체크하기위해 아래의 코드를 사용했다

## 해당인원 모두 건널수 있는지 체크
def check(stones,k):
    now_idx = 0
    while 1:
        flag = 0
        if now_idx >= len(stones):
            break
        if stones[now_idx] == 0:
            for i in range(k):
                flag = 0
                tmp_idx = now_idx+i
                if tmp_idx >= len(stones):
                    return True
                elif stones[tmp_idx] != 0:
                    #stones[tmp_idx]-=1
                    now_idx = tmp_idx
                    break
                flag = 1
        if flag == 1:
            return False
        elif stones[now_idx] >0:
            stones[now_idx]-=1
            now_idx+=1
        
    return True

이 체크하는 코드로 인해 효율성을 통과하지 못했다.. 도저히 방법이 생각이 나지 않아서 해설을 보니 체크하는 로직이 신박했다. 각 위치에 스톤들을 mid(건널 수 있는 사람)만큼 빼서 해당 0이 몇개가 만들어지는지 확인하면서 만들어진 0이 k보다 크거나 같아지면 건널 수 없다. 만약 건널 수 없는 인원이면 최대값을 갱신해주고 건널 수 있다면 최소값을 갱신하고 answer에 최솟값을 넣어주면된다.

"""
def solution(stones, k):
    answer = 0
    left = 1
    right = 200000000 
    while left <= right:
        #건널 수 있는 사람
        mid = (left + right) //2
        zero_block_cnt = 0
        for stone in stones:
            if stone - mid <=0:
                zero_block_cnt +=1
            else:
                zero_block_cnt = 0
            if zero_block_cnt >= k:
                break
        if zero_block_cnt >= k:
            right = mid -1
            continue
        left = mid +1
        answer = left
        
    return answer