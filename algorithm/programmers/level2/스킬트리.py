"""
프로그래머스 level2 - 스킬트리

정말 간단한 문제였다. 주어진 대로 구현하면 된다.

map을 이용해서 선행스킬인 skill을 맵의 키값으로 skill의 첫번째가 우선순위가 높으므로 순서대로 우선순위를 value로 지정해준다.

현재 우선순위를 기록하는 nowP 변수와 각 스킬트리에 대해 유효한지를 체크하기 위해 flag 변수를 선언해준다.

스킬트리에 대해 반복문을 통해 서치하고 만약 스킬트리에 스킬이 선행스킬 map에 있는지 확인 해서 있으면 우선순위를 체크해서 같이 않으면 flag값을 1로 변경해 주고 
만약 같다면 현재 우선순위를 1증가시켜준다. skill_tree에대한 스킬을 확인 완료했으면 flag 값이 0이면 스킬을 정상적으로 찍을 수 있다. answer+1 해준다. 이후 변수를 초기화 해주면 된다.


time = O(N^2)

space = O(N)

"""
def solution(skill, skill_trees):
    answer = 0
    
    map ={}
    
    priority = 0
    for s in skill:
        map[s] = priority
        priority+=1
    nowP = 0
    flag = 0
    for skill_tree in skill_trees:
        for skill in skill_tree:
            if skill in map:
                p = map[skill]
                if nowP != p:
                    flag = 1
                    break
                nowP+=1
        if flag == 0:
            answer+=1
        flag = 0
        nowP = 0
        
    return answer