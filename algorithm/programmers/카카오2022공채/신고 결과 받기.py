"""

프로그래머스 카카오 블라인드 2022 신고 결과 받기


간단했다. map을 사용해서 db를 이용하는 것 처럼 풀면 된다.

"""

from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    #유저가 신고한 id
    #(신고자,피신고자)
    db = defaultdict(set)
    tmp = set()
    for i in report:
        r = i.split(" ")
        # 0인덱스는 신고인 1인덱스는 피신고인
        db[r[0]].add(r[1])
        tmp.add((r[0],r[1]))
    report_db = defaultdict(list)
    ##피신고 개수
    for i in tmp:
        if not report_db[i[1]]:
            report_db[i[1]] = 1
        else:
            report_db[i[1]]+=1
    ## K개 이상인 피신고인 저장
    ban_list = defaultdict(list)
    for i in report_db:
        #k번이상일 경우 list
        if report_db.get(i) >= k:
            ban_list[i] = 1
    print(ban_list)
    # 벤할게 하나도 없으면 전부 0으로 리턴
    if not ban_list:
        return [0] * len(id_list)
    for id in id_list:
        search_data = db.get(id)
        cnt = 0
        if search_data:
            for data in search_data:
                if data in ban_list:
                    cnt +=1
        answer.append(cnt)
    return answer