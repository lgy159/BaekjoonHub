import heapq  # 우선순위 큐 구현을 위함

import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
# 주어지는 그래프 정보 담는 N개 길이의 리스트
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)  # 방문처리 기록용
distances = [INF] * (n + 1)  # 거리 테이블용

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):
    distances[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        now_distance, now_node = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.
        if distances[now_node] < now_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue
        for next_destination, next_distance in graph[now_node]:
            distance = now_distance + next_distance  # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[next_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distances[next_destination] = distance
                heapq.heappush(queue, [distance, next_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return distances


dijkstra(start)
print(distances[end])