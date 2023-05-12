import sys

graph = [list(map(int, input().split())) for _ in range(9)]


def check(graph, x, y, num):
    for r in range(9):
        if graph[r][y] == num:
            return 1
        if graph[x][r] == num:
            return 1

    for r in range(x // 3 * 3, x // 3 * 3 + 3):
        for c in range(y // 3 * 3, y // 3 * 3 + 3):
            if graph[r][c] == num:
                return 1
    return 0


def DFS(graph, zero_arr, zero_idx):
    if zero_idx == len(zero_arr):
        for r in range(9):
            print(*graph[r])
        sys.exit(0)
    for num in range(1, 10):
        r, c = zero_arr[zero_idx]
        if check(graph, r, c, num):
            continue
        graph[r][c] = num
        DFS(graph, zero_arr, zero_idx + 1)
        graph[r][c] = 0


zero = []
for row in range(9):
    for col in range(9):
        if graph[row][col] == 0:
            zero.append((row, col))

DFS(graph, zero, 0)

