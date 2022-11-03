from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

sword = 1e9
def BFS(q):
    global sword

    while q:
        x, y = q.popleft()
        if graph[x][y] == 2:
            sword = visited[x][y] - 1 + row - x - 1 + col - y - 1
        if x == row - 1 and y == col - 1:
            return min(sword, visited[x][y] - 1)
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or ny < 0 or nx >= row or ny >= col or visited[nx][ny] or graph[nx][ny] == 1:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
    return sword


row, col, limitTime = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]
visited = [[0 for _ in range(col)] for _ in range(row)]
q = deque()
visited[0][0] = 1
q.append((0, 0))
result = BFS(q)

if result <= limitTime:
    print(result)
else:
    print("Fail")