import sys

input = sys.stdin.readline
row, col = map(int, input().rstrip().split())
graph = [list(map(str, input().rstrip())) for _ in range(row)]
result = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    global result
    result = max(result, len(alpha))
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= row or ny >= col or graph[nx][ny] in alpha:
            continue
        alpha.add(graph[nx][ny])
        DFS(nx, ny)
        alpha.remove(graph[nx][ny])


alpha = set()
alpha.add(graph[0][0])
DFS(0, 0)
print(result)