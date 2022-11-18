from collections import deque


# 위상 정렬 함수
def topology_sort():
    result = [0] * (v + 1)
    q = deque()  # 큐 기능을 위한 deque 라이브러리 사용
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = weight[i]
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for node in graph[now]:
            indegree[node] -= 1
            result[node] = max(weight[node] + result[now], result[node])
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[node] == 0:
                q.append(node)
    # 위상 정렬을 수행한 결과 출력
    print(result[goal_node])


for _ in range(int(input())):
    v, e = map(int, input().split())
    weight = [0] + list(map(int, input().split()))
    indegree = [0] * (v + 1)
    graph = [[] for i in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    goal_node = int(input())
    topology_sort()
