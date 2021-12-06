/*
아주 작은 sub problem 풀어서 큰 문제를 푸는 것! --> 추상적

작은 것 부터 시작하지만(선택할 수도 A, 안할수도 B) 내가 A라는걸 선택 할 수 있고 B라는 걸 선택 할 수 있다.

item과 cap(수용량)을 중요하게 봐라!

base case ---> input = [] or cap = 0

        
    dp table

        0 1 2 3 4 5 6 7 8 9 10
        
   []   0 0 0 0 0 0 0 0 0 0 0
[1,2]   0 0 1 1 1 1 1 1 1 1 1
[4,3]   0 0 1 4 4 5             ---> formulation 
 ^ ^
 value,weight                                                 현재 벨류,
                    dp[][]             dp[i][c]= math.max(dp[i-1][c], dp[i-1][c-curweight]+culVal)
                      ^ ^
                 [1,2],[4,3]  index, cab 
                   ^     ^
           index   0     1
!!중요!!! 패턴 찾기!!!


*/