row, col = map(int, input().split())

graph = [list(input()) for _ in range(row)]

answer = 1
for n in range(2, min(row, col) + 1):
    for r in range(row - n + 1):
        for c in range(col - n + 1):
            if graph[r][c] == graph[r + n - 1][c] == graph[r][c + n - 1] == graph[r + n - 1][c + n - 1]:
                answer = max(answer, n ** 2)

print(answer)
