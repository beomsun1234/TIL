## 서로소 집합을 활용한 사이클 판별
# 참고로 방향그래프에서 사이클 여부는 dfs를 이요ㅕㅇ하여 판별할수 있습니다.
# 
# 사이클 판별 알고리즘이란?
# 1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인합니다
#  1) 루트 노드가 서로 다르다면 두 노드에 대하여 합집합(유니온)연산을 수행.
#  2) 루트 노드가 서로 같다면 사이클이 발생한 것
# 
# 2. 그래프에 포함되어 있는 모든 간선에 대하여 1 번과정을 반복   


#알고리즘

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])

    return parent[x]

def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)

    if a<b:
        parent[b]=a

    else:
        parent[a]=b


# 노드의 개수와 간선 입력받기
v, e = map(int,input().split())


parent=[0] * (v+1)

## 부모테이블을 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

cycle = False # 사이클 발생 여부


for i in range(e):
    a,b = map(int,input().split())
    # 사이클이 발생할경우 종료
    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        break
    else:
        union_parent(parent,a,b)

if cycle:
    print('사이클발생')
else:
    print('사이클이발생하지아늠')

