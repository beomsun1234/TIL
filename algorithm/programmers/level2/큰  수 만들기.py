

"""
프로그래머스 level2 그리디
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

- 내가 작성한 코드 (테스트케이스 ,8,10,12 시간초과 및 런타임에러)
로직은 주어진 number에서 k만큼 의 숫자 중에 가장 큰 값을 앞에 노면 그수는 앞에 올수 있는 가장 큰 수가 된다. ex) 4177252841, k = 4 일 경우 주어진 number중에 0 ~ 4까지의 인덳의 값을 가져오면 4,1,7,7,2 이다 이 중 가장 큰 값이 맨 앞에 올 경우 가장 큰 값이 된다.
최대값이 7이기에 우리는 앞에 2개 숫자를 빼기보다 k의 값을 최대값에 해당하는 인덱스를 찾을때까지 -1 해주면 현재 k는 2가 남게 된다. 즉 4,1 을 제거했다라고 이해하면 되겠다.
현제 인덱스의 값은 2이되고, k는 2가 될 것이다. 우리는 현제 인덱스 다음 숫자들을 확인해서 k만큼 확인 해서 가장 큰값을 뽑아주면 두번째 큰 값이 될 것이다. 7,2,5 중 우리는 바로 인덱스를 찾았기에 k를 -안해주고 for문을 탈출하며 현재 인덱스는 3이된며 k=2이다. 이제 우리가 확인 할 곳은 2,5,2이며 max = 5이기에  2를 삭제할 수 있다. k=1이 된다. index = 5가 될 것이고
2,8 중 8이 더 크키에 k -1 해주면 k=0이되며 가장큰 앞자리들을 모두 뽑게 된다. 이제 마지막 인덱스 이후에 값들을 모두 붙여주는 식으로 접근 했지만 시간초과가 발생한다..
def solution(number, k):
    maxV = -10000
    ret = []
    tmpK = k
    index = 0
    s_number = [int(i) for i in str(number)]
    if len(number) == 1: # 숫자의 길이가1이면 처음값 바로 리턴
        return "".join(number[0])
    if s_number.count(s_number[0]) == len(s_number): #숫자들이 다 같은 숫자이면
        s_number = s_number[:len(s_number)-k]
        print('1')
        return "".join([str(s) for s in s_number])
    while k >0: # 제거 할 수 있는 카우트가 0이 될때까지 반복
        for i in range(index,k+index+1): # 최대값 찾기, 인덱스부터 ,k+인덱스+1 까지 중
            maxV = max(maxV,int(number[i]))
        nowK = k # 현재 K값 저장
        for j in range(index,nowK+index+1): # 최대값을 가지고있는 인덱스를 찾을때까지 -(즉 최대값보다 작은 수 이면 제거)
            if maxV == int(number[j]):
                index = j+1 # 다음인덱스 설정
                ret.append(number[j]) 
                break   
            else:
                k-=1
        maxV = 0
    if len(ret) == len(number) - tmpK: # 최대값으로 이루어진 ret의 길이가 주어진 number의 길이와 주어진 k의 값을 뺀 값과 같다면 뒤에 숫자 붙일 필요 없이 바로 리턴
        return "".join(ret)
    for i in range(index, len(number)): # 나머지 숫자 붙여준다.
        ret.append(number[i])
    return "".join(ret)

"""
def solution(number, k):
    answer = []
    s_number = []
    for num in number:
        # answer에 뭐라도 존재하고, k가 0보다 크며, answer의 맨 위 값이 현재의 num보다 작으면
        while answer and k > 0 and answer[-1] < num:
            # answer의 맨 위 값을 제거하고 k도 -1 해준다
            answer.pop()
            k -= 1
        # 현재의 num값은 무조건적으로 answer에 넣어준다
        answer.append(num)
    
    # k가 남았다면
    # answer는 number의 길이 - k만큼 슬라이싱 해준다.
    # -> 슬라이싱은 index 바깥으로 나가도 괜찮음! 
    # 일반적으로 k는 0일텐데 ex) k = 4 number = 99999999999999 이런 경우엔 k는 처음 인풋받은 그대로 유지됨
    
    # 이럴 때 답은 뒷 숫자를 k개만큼 없애준 9999999999 이므로 슬라이싱을 len(number) - k로 해주는 것
    answer = ''.join(answer[:len(number)-k])
    print(answer)
    return answer
