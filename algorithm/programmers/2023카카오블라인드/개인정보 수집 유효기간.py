def getAfterDay(period, start_day):
    year  = int(start_day[:4])
    month = int(start_day[5:7])
    day   = str(int(start_day[8:]) -1)
    for i in range(period):
        month +=1
        if month >12:
            year +=1
            month = 1
    if day == "0":
        month = month-1
        day = '28'
    if month < 10:
        return str(year)+'.'+ '0'+str(month)+ '.' +day
    return str(year)+'.'+str(month)+ '.' +day

def isExpired(deadline, now):
    print(deadline, now)
    if int(deadline[:4]) > int(now[:4]):
        return False
    elif int(deadline[:4]) < int(now[:4]):
        return True
    else:
        if int(deadline[5:7]) > int(now[5:7]):
            return False
        elif int(deadline[5:7]) < int(now[5:7]):
            return True
        else:
            if int(deadline[8:]) < int(now[8:]):
                return True
    return False
            
    
def solution(today, terms, privacies):
    answer = []
    terms_table = {}
    
    #약관저장
    for val in terms:
        term = val.split()
        terms_table[term[0]] = int(term[1]) 
    #개인정보 검사
    for idx,val in enumerate(privacies):
        privacie = val.split()
        start = privacie[0]
        period = terms_table.get(privacie[1])
        after = getAfterDay(period,start)
        if not isExpired(after,today): 
            continue
        answer.append(idx+1)
    return answer
