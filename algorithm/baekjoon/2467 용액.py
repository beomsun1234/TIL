"""
2467 용액
"""
N = int(input())
solution = list(map(int,input().split()))
solution.sort()

l, r = 0, N-1
sum_solution = 2000000000
answer_solution = [0] * 2
while l < r:
    tmp_sum_solution = solution[l] + solution[r]
    if abs(tmp_sum_solution) < sum_solution:
        sum_solution = abs(tmp_sum_solution)
        answer_solution[0] = solution[l]
        answer_solution[1] = solution[r]
    if tmp_sum_solution < 0:
        l+=1
    else:
        r-=1

print(answer_solution[0], answer_solution[1])