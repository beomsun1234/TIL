S = input()
global T
T = input()


global N

N = len(T) - len(S)

global ret
ret = 0

pick = []

#연산
def op(pick):
    # 0 - 문자열의 뒤에 A를 추가한다.
    # 1 - 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
    tmp = S
    for i in pick:
        if i == 0:
            tmp += "A"
        else:
            tmp += "B"
            tmp = tmp[::-1]
    if tmp == T:
        return True
    return False
def find2(t):
    global T
    global ret
    if t == S:
        ret = 1
        return
    if len(S) > len(t):
        return
    if t[-1]=="A":
        a = t[:-1]
        T = a
        find2(T)
    if t[0] == "B":
        a = t[1:]
        T = a[::-1]
        find2(T)

if len(S) == len(T):
    if S == T:
        print(1)
    else:
        print(0)
else:
    find2(T)
    print(ret)
