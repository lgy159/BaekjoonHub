import copy
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
v = [[0 for _ in range(n)] for _ in range(n)]
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i, j))
        if graph[i][j] == 1:
            v[i][j] = -1


def check():
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                return True
    return False


def BFS():
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] != 0:
                continue
            if graph[nx][ny] == 1:
                visited[nx][ny] = -1
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))


permu_virus = list(combinations(virus, m))
result = 1e9
for data in permu_virus:
    q = deque()
    visited = copy.deepcopy(v)
    for x, y in data:
        q.append((x, y))
        visited[x][y] = 1
    BFS()
    if check():
        continue
    temp = 0
    for i in range(n):
        temp = max(temp, max(visited[i]))
    result = min(result, temp - 1)

if result == 1e9:
    print(-1)
else:
    print(result)
