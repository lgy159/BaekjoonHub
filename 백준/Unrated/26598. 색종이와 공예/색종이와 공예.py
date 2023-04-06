import sys

row, col = map(int, input().split())
graph = [input() for _ in range(row)]
visited = [[0 for _ in range(col)] for _ in range(row)]


def BFS(x, y):
    word = graph[x][y]
    many = 0
    for r in range(y, col):
        if word == graph[x][r]:
            if visited[x][r]:
                return 0
            many += 1
            visited[x][r] = 1
        else:
            break

    for r in range(x + 1, row):
        temp = 0
        for c in range(y, col):
            if word == graph[r][c]:
                if visited[r][c]:
                    return 0
                temp += 1
                visited[r][c] = 1
            else:
                if temp == 0:
                    for d in range(c + 1, c + many):
                        if word == graph[r][d]:
                            return 0
                break
        if temp == 0:
            break
        if many != temp:
            return 0

    return 1


for r in range(row):
    for c in range(col):
        if not visited[r][c]:
            if not BFS(r, c):
                print("BaboBabo")
                sys.exit(0)

print("dd")
