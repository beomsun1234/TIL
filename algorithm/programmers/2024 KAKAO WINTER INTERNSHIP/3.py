"""
# 시간초과 50점짜리 코드



def solution(dice):
    answer = []
    
    n = len(dice)
    for i in range(n//2):
        answer.append(0)
    n2 = len(dice[0])
    pick = []
    global win_late
    win_late = 0
    def 계산(pick2,pick):
        cnt1 = 0
        cnt2 = 0
        c = 0 
        tmp_db = {}
        for i in range(len(pick)):
            tmp_db[pick[i] -1] = 1
            cnt1 +=  dice[(pick[i]-1)][pick2[i]]
            c+=1
        
        for i in range(n):
            if i not in tmp_db:
                cnt2 += dice[i][pick2[c]]
                c+=1
        return cnt1, cnt2
    pick2 = []
    
    
    def 합치기(nn,pick):
        global win
        global lose
        global draw
        if nn == n:
            #print(pick, pick2)
            a, b = 계산(pick2, pick)
            if a > b:
                win +=1
            elif a < b:
                lose +=1
            else:
                draw +=1
            return
        for i in range(n2):
            pick2.append(i)
            합치기(nn+1, pick)
            pick2.pop()
            
    def dfs(pick_cnt, idx):
        if pick_cnt == (n//2):
            global win_late
            global win
            global lose
            global draw
            win = 0
            lose = 0
            draw = 0
            #print(win, lose, draw)
            합치기(0,pick)
            tmp_win_late = (win / (win+draw+lose)) * 100 
            if win_late < tmp_win_late:
                win_late = tmp_win_late
                for i in range(len(pick)):
                    answer[i] = pick[i]
            return
        for i in range(idx,n+1):
            pick.append(i)
            dfs(pick_cnt+1, i+1)
            pick.pop()
    dfs(0,1)
    
    return answer

"""
