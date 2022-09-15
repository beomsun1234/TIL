N, M = map(int, input().split())

trees = list(map(int,input().split()))
trees.sort()

left_t = 0
right_t = trees[-1]

answer = 0

while left_t+1<right_t:
    cut_t = (left_t+right_t)//2
    cutting_tree_len = []
    for idx in range(N):
        tmp_tree_len = trees[idx] - cut_t
        if tmp_tree_len <= 0:
            tmp_tree_len = 0
        cutting_tree_len.append(tmp_tree_len)

    if sum(cutting_tree_len) >= M:
        answer = max(answer, cut_t)
        left_t = cut_t
    else:
        right_t = cut_t

print(answer)
