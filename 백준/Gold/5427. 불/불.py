# test_case = int(input())
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def spread(q):
    while q:
        x, y, type, cnt = q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if type == '@' and graph[x][y] == '*':
                continue
            if type == '@' and (nx < 0 or ny < 0 or nx >= row or ny >= col):

                result.append(cnt)
                return cnt
            if nx < 0 or ny < 0 or nx >= row or ny >= col or graph[nx][ny] == '#':
                continue
            if type == '@' and graph[nx][ny] != '.':
                continue
            if type == '*' and graph[nx][ny] == '*':
                continue
            visited[nx][ny] = 1
            graph[nx][ny] = type
            q.append((nx, ny, type, cnt + 1))
    return -1


def BFS(q):
    result = spread(q)

    if result == -1:
        print("IMPOSSIBLE")
    else:
        print(result + 1)


test_case = int(input())
for _ in range(test_case):
    col, row = map(int, input().split())
    graph = [list(input()) for _ in range(row)]
    visited = [[0 for _ in range(col)] for _ in range(row)]
    q = deque()
    result = []
    for r in range(row):
        for c in range(col):
            if graph[r][c] == '@':
                q.append((r, c, '@', 0))
                visited[r][c] = 1
    for r in range(row):
        for c in range(col):
            if graph[r][c] == '*':
                q.append((r, c, '*', 0))
                visited[r][c] = 1
    BFS(q)
