import heapq
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
start = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    start[b] += 1

q = []
for idx in range(1, n + 1):
    if not start[idx]:
        heapq.heappush(q, idx)


while q:
    node = heapq.heappop(q)
    print(node, end=' ')
    for data in graph[node]:
        if start[data] == 1:
            heapq.heappush(q, data)
        else:
            start[data] -= 1
    graph[node] = []
