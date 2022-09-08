"""

식재료 N개 중에서 몇 개를 선택해서
이들의 영양분(단백질, 탄수화물, 지방, 비타민)이 
일정 이상이 되어야 한다. 
아래 표에 제시된 6가지의 식재료 중에서 
몇 개를 선택해서 이들의 영양분의 
각각 합이 최소 100, 70, 90, 10가 되도록 하는 경우를 생각해보자. 
이 경우 모든 재료를 선택하면 쉽게 해결되지만, 
우리는 조건을 만족시키면서도 비용이 최소가 되는 선택을 하려고 한다.
"""





N = int(input())

least_nutrition_info = list(map(int, input().split()))
nutrition_infos =[] 
for i in range(N):
    nutrition_info = list(map(int, input().split()))
    nutrition_infos.append(nutrition_info)

pick_diet_num = []
ret = []
global least_price
least_price = 99999999
def cal_nutrition(combi_diet_num):
    #단백질, 지방, 탄수, 비타민
    d = 0
    g = 0
    t = 0
    b = 0
    price = 0
    ret_nutrition_info = []
    for diet_num in combi_diet_num:
        d += nutrition_infos[diet_num][0]
        g += nutrition_infos[diet_num][1]
        t += nutrition_infos[diet_num][2]
        b += nutrition_infos[diet_num][3]
        price += nutrition_infos[diet_num][4]
            
    ret_nutrition_info = [d,g,t,b,price]
    return ret_nutrition_info

def is_gt_eq_nutrition(a_nutrition_info):
    global least_price
    for idx in range(4):
        if a_nutrition_info[idx]<least_nutrition_info[idx]:
            return False
    return True
def dfs(pick,idx):
    if pick == N:
        if is_gt_eq_nutrition(cal_nutrition(pick_diet_num)):
            p = 0
            tmp = []
            for num in pick_diet_num:
                p+=nutrition_infos[num][4]
        
            for t in pick_diet_num:
                tmp.append(t+1)
            ret.append((p,tmp))
         
        return   
    if is_gt_eq_nutrition(cal_nutrition(pick_diet_num)):
        p = 0
        tmp = []
        for num in pick_diet_num:
            p+=nutrition_infos[num][4]
        
        for t in pick_diet_num:
            tmp.append(t+1)
        ret.append((p,tmp))
    # 식단 뽑기
    for i in range(idx,N):
        pick_diet_num.append(i)
        dfs(pick+1, i+1)
        pick_diet_num.pop()

    # 다 뽑지 않아도 영양성분 검사


dfs(0,0)
if len(ret) <1:
    print(-1)
else:
    ret.sort()
    print(ret[0][0])
    print(*ret[0][1])
