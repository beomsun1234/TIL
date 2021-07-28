lst = []
result = 0
nine = 9
for i in range(9):
    N = int(input())
    lst.append(N)

lstsum = sum(lst)
for i in range(nine-1):
    for j in range(i+1, nine): ##전체 값에서 두명의 값을 뻇을때 100이 되는 것 찾아서 삭제
        if (lstsum-lst[i]-lst[j]) == 100:
            del lst[j]
            del lst[i]
            break
    if len(lst) < 9:
        break

lst = sorted(lst)
for i in lst:
    print(i,end=' ')
