from collections import deque

row, col = map(int, input().split())
graph = [list(input()) for _ in range(row)]
visited = [[0 for _ in range(col)] for _ in range(row)]
q = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS():
    while q:
        x, y, type = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= row or ny < 0 or ny >= col or graph[nx][ny] == 'X':
                continue

            if type == 0 and (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and not visited[nx][ny] and graph[x][y] != '*': 
                if graph[nx][ny] != 'D':
                    graph[nx][ny] = 'S'
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny, type))
                if graph[nx][ny] == 'D' and type == 0:
                    return visited[nx][ny]
            if type == 1 and graph[nx][ny] != '*' and graph[nx][ny] != 'D':
                graph[nx][ny] = '*'
                visited[nx][ny] = 0
                q.append((nx, ny, type))


for r in range(row):
    for c in range(col):
        if graph[r][c] == 'S':
            q.append((r, c, 0))
            visited[r][c] = 1

for r in range(row):
    for c in range(col):
        if graph[r][c] == '*':
            q.append((r, c, 1))

result = BFS()
if result:
    print(result - 1)
else:
    print("KAKTUS")


