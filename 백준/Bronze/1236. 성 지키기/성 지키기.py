row, col = map(int, input().split())
graph = [list(input()) for _ in range(row)]


def solve():
    rx, ry = [], []
    for r in range(row):
        if graph[r].count('X') == 0:
            rx.append(r)

    for c in range(col):
        temp = 0
        for r in range(row):
            if graph[r][c] == 'X':
                temp += 1
        if temp == 0:
            ry.append(c)

    return max(len(rx), len(ry))

print(solve())