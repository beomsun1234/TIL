"""
2661 - 좋은 수열
"""

visited = [False] * 3
N = int(input())

ret = []


##수열을 받아서 체크한다.
def isGood(nums):
    #절반을 검사해서 일치하지 않으면 좋은 수열
    print('nums=',nums)
    for i in range(1, len(nums)//2+1):
        if nums[-i:] == nums[-(i*2):-i]:
            print("nums[-i:] = ",nums[-i:])
            print("nums[-(i*2):-i]",nums[-(i*2):-i])
            return False
    print("--------------------")
    return True

# 사용했던 숫자는 다음에 사용불가.
def dfs(pick):
    if pick == N:
        print(''.join(ret))
        exit()
    for i in range(1,4):
        ret.append(str(i))
        if isGood(ret): ## 좋은 수열일 경우만 다음 수 dfs 수행
            dfs(pick+1)
        ret.pop()
dfs(0)
