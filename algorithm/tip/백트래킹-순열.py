def permutation(p, k, n, used):
# 순열 p[0],...,p[k-1]이 정해진 상태에서 p[k-1] ...p[n-1]의 모든 순열을 생성
    if(k <= n-1):                                                       # 0 <= 2
        for i in range(1,n+1):
            if not used[i]:      # i가 순열에 사용되지 않은 수이면              # i = 1
                p[k] = i                                                # p[0] = 1
                used[i] = True
                if(k == n-1):  # 하나의 순열을 생성한 경우
                    for j in range(0,n):     # 순열 출력 
                        print(p[j], end = ' ')
                    print()
                    used[i] = False  # False로 두는 이유는?    "가능한 후보해로 만들기 위해"
                    return # continue 문장과의 차이점은?   "더이상 함수를 실행하지 않고 종료" continue는 "for문의 다음 i를 실행"
                permutation(p, k+1, n, used)                            # 1 <= 2
                used[i] = False      # False로 두는 이유는?    
                # 이미 두 번째 for문 안에서 가능한 후보해로 만들었다 하더라도 첫 번째 for문이 아직 남았다면, 
                # 가능한 후보해가 더 필요한 것이므로 False로 두어 다음 i가 들어가는 데에 지장이 없게 한다.

def main():
   
    n = int(input())
    p = [None] * n         # 하나의 순열을 저장하는 리스트
    used = [None]*(n+1) # 숫자 i가 순열에 사용되었는지를 나타내는 리스트

    for i in range(1,n+1):
        used[i] = False

    permutation(p, 0, n, used)        

if __name__ == '__main__':
    main()
