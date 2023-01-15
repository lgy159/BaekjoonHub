from collections import deque

n, m = map(int, input().split())
switch = [[[] for _ in range(n)] for _ in range(n)]
graph = [[0 for _ in range(n)] for _ in range(n)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(m):
    x, y, a, b = map(int, input().split())
    switch[x - 1][y - 1].append((a - 1, b - 1))

q = deque()
q.append((0, 0))  # 0 -> 어두운 곳
graph[0][0] = 1  # 1 -> 방문한 곳
for sx, sy in switch[0][0]:
    graph[sx][sy] = 2  # 2 -> 불 켜진 곳


def BFS(q):
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 2:
                if switch[nx][ny]:
                    for sx, sy in switch[nx][ny]:
                        if graph[sx][sy] == 0:
                            graph[sx][sy] = 2
                q.append((nx, ny))
                graph[nx][ny] = 1


def solve(x, y):
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == 1:
            return True
    return False



while q:
    BFS(q)
    q = deque()
    for r in range(n):
        for c in range(n):
            if graph[r][c] == 2 and solve(r, c):
                q.append((r, c))
    for x, y in q:
        graph[x][y] = 1
        for sx, sy in switch[x][y]:
            if graph[sx][sy] == 0:
                graph[sx][sy] = 2

result = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            result += 1
print(result)
