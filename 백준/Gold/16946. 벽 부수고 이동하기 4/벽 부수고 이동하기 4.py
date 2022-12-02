from collections import deque
from copy import deepcopy

row, col = map(int, input().split())
graph = [list(map(int, input())) for _ in range(row)]
result = deepcopy(graph)
visited = [[0 for _ in range(col)] for _ in range(row)]
cnt = 0
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
data = []


def BFS(x, y):
    global cnt
    cnt += 1
    num_count = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = cnt
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= row or ny >= col or visited[nx][ny] or graph[nx][ny]:
                continue
            visited[nx][ny] = cnt
            q.append((nx, ny))
            num_count += 1
    data.append([cnt, num_count])


def solve(x, y):
    temp = 0
    v = []
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= row or ny >= col or graph[nx][ny]:
            continue
        if not visited[nx][ny] in v:
            temp += data[visited[nx][ny] - 1][1]
            v.append(visited[nx][ny])
    return (temp + 1) % 10


for r in range(row):
    for c in range(col):
        if graph[r][c] == 0 and not visited[r][c]:
            BFS(r, c)

for r in range(row):
    for c in range(col):
        if graph[r][c] == 1:
            result[r][c] = solve(r, c)

for i in range(row):
    print(*result[i], sep='')

