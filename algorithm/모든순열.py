from itertools import permutations
n = int(input());
arr = [];
for i in range(1, n+1):
    arr.append(i);

result = list(permutations(arr,n));
for i in result:
    for j in i:
        print(j, end=' ')
    print()