"""
level 2 오픈채팅방

보자마자 해시가 생각나는 문제였다. 해시로 접근 했다. ret라는 딕셔너리를 생성해주고 Enter와 Change시에만 ret에 key를 유저아이디로 value를 닉네임으로해서 값을 넣어주고 갱신해준었다. 또 order이라는 맵을 생성해서 key를 인덱스로 하는 enter, leave가 발생되는 순서를 저장한 맵이다. 맵에 값을 다 넣어준 후 oders에 아이템들을 가져와서 order에 values에는 ret의 키값과 Enter,Change 등 과같은 operation이 있다. order에 item들을 가져와서 ret에 해당하는 닉네임을 가저오면 정답이 된다. 생각해 보니 order라는 딕셔너리가 필요가없을 것 같아서. 
코드를 리팩토링하고 다시 제출했다.  시간이 조금 걸린 부분이 처음에 Leave시에도 ret의 값을 ''로 초기화 시켰다.. 이랬더니 여기서 주어진 케이스는 통과하지만 다른 케이스들을 통과하지 못했다.. 이유는 Leave시 해당 유저의 아이디의 닉네임을 ''로초기화하면 enter 이후 leave할 시 해당 유저의 닉네임은 알 수 없게 된다.. 
아래는 리팩토링 전 코드이다
    answer = [] 
    ret = {}
    order = {}
    cnt = 0
    for idx,i in enumerate(record):
        userRecord = i.split(" ")
        if userRecord[0] == 'Enter':
            ret[userRecord[1]] = userRecord[2]
            order[idx] = (userRecord[1],'E')
        elif userRecord[0] == 'Change':
            ret[userRecord[1]] = userRecord[2]
        elif userRecord[0] == 'Leave':
            order[idx] = (userRecord[1],'L')
    
    # 0 -> 인덱스, 1-> key,val -> [1][0]->key, [1][1] -> index
    for i in order.items():
        if i[1][1] == 'E':
            answer.append(ret.get(i[1][0])+"님이 들어왔습니다.")
        elif i[1][1]:
            answer.append(ret.get(i[1][0])+"님이 나갔습니다.")

    return answer
    
"""
def solution(record):
    answer = []  
    ret = {}
    for r in record:
        userRecord = r.split(" ")
        # 0-> operation, 1-> 유저아이디, 2-> 닉네임
        if userRecord[0] == 'Enter':
            ret[userRecord[1]] = userRecord[2]
        elif userRecord[0] == 'Change':
            ret[userRecord[1]] = userRecord[2]
    
    for r in record:
        userRecord = r.split(" ")
        if userRecord[0] == 'Enter':
            answer.append(ret.get(userRecord[1])+"님이 들어왔습니다.")
        elif userRecord[0] == 'Leave':
            answer.append(ret.get(userRecord[1])+"님이 나갔습니다.")

    return answer