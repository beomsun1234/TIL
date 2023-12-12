s = input()

window_size = 0

for i in s:
    if i == "a":
        window_size +=1



l = len(s) -1


def countB(ss)->int:
    cnt = 0
    for i in ss:
        if i == "b":
            cnt+=1
    return cnt

b_cnt = countB(s[:window_size])


minVal = b_cnt
for i in range(1,len(s)):
    cnt = 0
    ss = ""
    if s[i-1] == "b":
        b_cnt-=1
    # 윈도우 사이즈보다 크면 앞에 친구를 넣어준다.
    if (i + window_size) > len(s):
        if s[(i+window_size-1)-len(s)] == "b":
            b_cnt +=1
    else:
        if s[(i+window_size-1)] == "b":
            b_cnt +=1
    minVal = min(b_cnt, minVal)


print(minVal)
