from collections import deque

row, col = map(int, input().split())
graph = [list(input()) for _ in range(row)]
result = 0


def direction(x, y):
    if graph[x][y] == 'L':
        return x, y - 1
    if graph[x][y] == 'R':
        return x, y + 1
    if graph[x][y] == 'U':
        return x - 1, y
    if graph[x][y] == 'D':
        return x + 1, y


def solve(r, c):
    global result
    space = []
    visited[r][c] = True
    q = deque()
    q.append((r, c))
    space.append((r, c))
    while q:
        x, y = q.popleft()
        nx, ny = direction(x, y)
        if (nx, ny) in space:
            result += 1
            return
        if visited[nx][ny]:
            continue
        visited[nx][ny] = True
        space.append((nx, ny))
        q.append((nx, ny))


visited = [[False for _ in range(col)] for _ in range(row)]
for r in range(row):
    for c in range(col):
        if not visited[r][c]:
            solve(r, c)

print(result)