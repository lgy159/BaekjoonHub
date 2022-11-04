from collections import deque
import copy
from itertools import permutations

row, col, attackRange = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(row)]
artchers_permu = list(permutations([i for i in range(col)], 3))

dx = [0, -1, 0]
dy = [-1, 0, 1]
result = []


def moveEnemy():
    enemys = deque()
    for r in range(row):
        for c in range(col):
            if graph[r][c] == 1:
                graph[r][c] = 0
                enemys.append((r + 1, c))
    while enemys:
        x, y = enemys.popleft()
        if x < 0 or y < 0 or x >= row or y >= col:
            continue
        graph[x][y] = 1


def attackEnemy(atchers):
    rmv = []
    rmvCnt = 0
    for c in atchers:
        visited = [[0 for _ in range(col)] for _ in range(row)]
        q = deque()
        visited[row - 1][c] = 1
        q.append((row - 1, c))
        while q:
            x, y = q.popleft()
            if graph[x][y]:
                rmv.append((x, y))
                break
            for i in range(3):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= row or ny >= col or visited[nx][ny] or visited[x][y] >= attackRange:
                    continue
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    while rmv:
        x, y = rmv.pop()
        if graph[x][y]:
            graph[x][y] = 0
            rmvCnt += 1
    return rmvCnt


def checkZero():
    graphSize = row * col
    zeroCnt = 0
    for r in range(row):
        zeroCnt += graph[r].count(0)
    return zeroCnt != graphSize


for data in artchers_permu:
    graph = copy.deepcopy(graphs)
    cnt = 0
    while checkZero():
        cnt += attackEnemy(data)
        moveEnemy()
    result.append(cnt)


print(max(result))