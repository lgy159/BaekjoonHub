v, e = map(int, input().split())
# 부모 테이블 초기화
parent = [i for i in range(v + 1)]


# find 연산
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


# union 연산
def union_parent(a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 간선 정보 담을 리스트와 최소 신장 트리 계산 변수 정의
edges = []
total_cost = 0

# 간선 정보 주어지고 비용을 기준으로 정렬
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선 정보 비용 기준으로 오름차순 정렬
edges.sort()

# 선택된 간선
selected = []

# 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
for i in range(e):
    cost, a, b = edges[i]
    # find 연산 후, 부모노드 다르면 사이클 발생 X으므로 union 연산 수행 -> 최소 신장 트리에 포함!
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    if parent_a != parent_b:
        union_parent(parent_a, parent_b)
        total_cost += cost
        selected.append(cost)

total_cost -= selected.pop()
print(total_cost)