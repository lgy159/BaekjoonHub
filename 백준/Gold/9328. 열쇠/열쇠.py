from collections import deque

n = int(input())
dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for _ in range(n):
    result = 0
    row, col = map(int, input().split())
    graph = [list(input()) for _ in range(row)]
    keys = list(input())
    q = deque()
    wait = []
    visited = [[0 for _ in range(col)] for _ in range(row)]
    if keys[0] == '0':
        keys.clear()
    for r in range(row):
        if graph[r][0] != '*':
            if graph[r][0].isupper():
                wait.append((r, 0, graph[r][0]))
            else:
                q.append((r, 0))
                visited[r][0] = 1
                if graph[r][0].islower():
                    keys.append(graph[r][0])
        if graph[r][col - 1] != '*':
            if graph[r][col - 1].isupper():
                wait.append((r, col - 1, graph[r][col - 1]))
            else:
                q.append((r, col - 1))
                visited[r][col - 1] = 1
                if graph[r][col - 1].islower():
                    keys.append(graph[r][col - 1])
    for c in range(col):
        if graph[0][c] != '*':
            if graph[0][c].isupper():
                wait.append((0, c, graph[0][c]))
            else:
                q.append((0, c))
                visited[0][c] = 1
                if graph[0][c].islower():
                    keys.append(graph[0][c])
        if graph[row - 1][c] != '*':
            if graph[row - 1][c].isupper():
                wait.append((row - 1, c, graph[row - 1][c]))
            else:
                q.append((row - 1, c))
                visited[row - 1][c] = 1
                if graph[row - 1][c].islower():
                    keys.append(graph[row - 1][c])

    q = deque(set(q))
    for data in wait:
        if data[2].lower() in keys:
            q.append((data[0], data[1]))
    while q:
        x, y = q.popleft()
        if graph[x][y] == '$':
            result += 1
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= row or ny >= col or graph[nx][ny] == '*' or visited[nx][ny]:
                continue
            if graph[nx][ny].isupper():
                if graph[nx][ny].lower() in keys:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                else:
                    wait.append((nx, ny, graph[nx][ny].lower()))

            elif graph[nx][ny].islower():
                keys.append(graph[nx][ny])
                for data in wait:
                    if data[2].lower() in keys:
                        q.append((data[0], data[1]))
                q.append((nx, ny))
                visited[nx][ny] = 1

            elif graph[nx][ny] == '.' or graph[nx][ny] == '$':
                q.append((nx, ny))
                visited[nx][ny] = 1
    print(result)
