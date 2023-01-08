from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]
visited = [[0 for _ in range(n)] for _ in range(n)]
start = []


def BFS(x, y, value):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        graph[x][y] = value
        for dx, dy in dir:
            nx, ny = dx + x, dy + y
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:
                continue
            if not graph[nx][ny]:
                continue
            visited[nx][ny] = 1
            q.append((nx, ny))


temp = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            BFS(i, j, temp)
            start.append((i, j))
            temp += 1


def BFS():
    global start
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for x, y in start:
        visited[x][y] = graph[x][y]
    while 1:
        q = deque(start)
        start = []
        while q:
            x, y = q.popleft()
            for dx, dy in dir:
                nx, ny = dx + x, dy + y
                if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny] == visited[x][y]:
                    continue
                if visited[nx][ny] != 0 and visited[x][y] != 0 and visited[nx][ny] != visited[x][y]:
                    return visited[x][y], visited[nx][ny]
                if graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]
                    start.append((nx, ny))
                else:
                    visited[nx][ny] = visited[x][y]
                    q.append((nx, ny))


def find(left, right, x, y):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = left
    temp = []
    temp.append((x, y))
    while 1:
        q = deque(temp)
        temp = []
        while q:
            x, y = q.popleft()
            for dx, dy in dir:
                nx, ny = dx + x, dy + y
                if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:
                    continue
                if graph[nx][ny] == right:
                    return visited[x][y]
                if graph[nx][ny] == 0:
                    temp.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                else:
                    visited[nx][ny] = visited[x][y]
                    q.append((nx, ny))


left, right = BFS()
s = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == left and not s:
            s.append((i, j))

x, y = s[0]
print(find(left, right, x, y) - graph[x][y])