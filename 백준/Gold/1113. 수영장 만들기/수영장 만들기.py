from collections import deque

row, col = map(int, input().split())
graph = [list(map(int, input())) for _ in range(row)]
dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]
start_q = deque()
result = 0

def start_find():
    visited = [[False for _ in range(col)] for _ in range(row)]
    flag2 = False
    for r in range(row):
        for c in range(col):
            if visited[r][c]:
                continue
            visited[r][c] = True
            flag = False
            q = deque()
            q.append((r, c))
            while q:
                x, y = q.popleft()
                for dx, dy in dir:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= row or ny >= col:
                        flag = True
                        continue
                    if graph[x][y] > graph[nx][ny]:
                        flag = True
                    if visited[nx][ny]:
                        continue
                    if graph[x][y] == graph[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
            if not flag:
                flag2 = True
                start_q.append((r, c))
    if flag2:
        return True
    else:
        return False


def find_edge():  # 변환
    global result
    visited = [[False for _ in range(col)] for _ in range(row)]
    for x, y in start_q:
        visited[x][y] = True

    while start_q:
        sx, sy = start_q.popleft()
        q = deque()
        q.append((sx, sy))
        change = deque()
        change.append((sx, sy))
        min_value = 1e9
        while q:
            x, y = q.popleft()
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= row or ny >= col or visited[nx][ny]:
                    continue
                if graph[x][y] == graph[nx][ny]:
                    q.append((nx, ny))
                    change.append((nx, ny))
                    visited[nx][ny] = True
                else:
                    min_value = min(min_value, graph[nx][ny])

        for x, y in change:
            result += min_value - graph[x][y]
            graph[x][y] = min_value

while 1:
    if not start_find():
        break
    find_edge()

print(result)