from collections import deque

row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]
visited = [[0 for _ in range(col)] for _ in range(row)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
group = [0] * (row * col)


def BFS(x, y, num):
    q = deque()
    q.append((x, y))
    visited[x][y] = num
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= row or ny >= col or visited[nx][ny] or not graph[nx][ny]:
                continue
            q.append((nx, ny))
            visited[nx][ny] = num
    return cnt


cnt = 1
for r in range(row):
    for c in range(col):
        if graph[r][c] and not visited[r][c]:
            number = BFS(r, c, cnt)
            group[cnt] = number
            cnt += 1

result = []


def s(x, y):
    temp = set()
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= row or ny >= col:
            continue
        if visited[nx][ny] and not visited[nx][ny] in temp:
            temp.add(visited[nx][ny])
    cnt = 0
    for a in temp:
        cnt += group[a]
    return cnt


answer = 0
for r in range(row):
    for c in range(col):
        if graph[r][c] == 0:
            answer = max(answer, s(r, c))

print(answer + 1)
