"""
프로그래머스 level3 다단계 칫솔 판매(2021데브매칭)
https://programmers.co.kr/learn/courses/30/lessons/77486
"""
import sys
sys.setrecursionlimit(10**8)
from collections import defaultdict
def dfs(start_node, graph,db,revenue):
    if revenue == 0 or start_node == '-':
        return
    for refer in graph[start_node]:
        distribution = revenue//10
        #수익에서 분배금을 빼면 내가 가져가는 수입이다.
        db[start_node] += revenue - distribution
        dfs(refer, graph,db, distribution)

def solution(enroll, referral, seller, amount):
    answer = []
    global flag
    graph = defaultdict(list)
    db = defaultdict(int)
    for i in range(len(enroll)):
        db[enroll[i]] = 0
        graph[enroll[i]].append(referral[i])
    for idx, s in enumerate(seller):
        revenue = amount[idx]*100 
        dfs(s,graph,db,revenue)
    for i in db.values():
        answer.append(i)
    return answer