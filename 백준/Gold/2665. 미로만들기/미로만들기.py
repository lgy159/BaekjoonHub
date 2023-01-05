from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def BFS():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == n and y == n:
            break
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 0:
                if visited[nx][ny]:
                    if visited[nx][ny] > visited[x][y] + 1:
                        q.append((nx, ny))
                    visited[nx][ny] = min(visited[x][y] + 1, visited[nx][ny])
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                continue
            if visited[nx][ny]:
                if visited[nx][ny] > visited[x][y]:
                    q.append((nx, ny))
                visited[nx][ny] = min(visited[x][y], visited[nx][ny])
                continue

            visited[nx][ny] = visited[x][y]
            q.append((nx, ny))

BFS()
print(visited[n - 1][n - 1] - 1)