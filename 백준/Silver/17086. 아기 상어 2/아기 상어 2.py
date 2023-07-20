from collections import deque

row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]
sharks = []

def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0 for _ in range(col)] for _ in range(row)]
    visited[x][y] = 1
    temp = []
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= row or ny >= col or visited[nx][ny]:
                continue
            if graph[nx][ny]:
                return visited[x][y]
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))


result = []
for r in range(row):
    for c in range(col):
        if not graph[r][c]:
            result.append(BFS(r, c))

print(max(result))
