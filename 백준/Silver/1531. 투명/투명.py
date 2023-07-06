graph = [[0 for _ in range(100)] for _ in range(100)]

n, m = map(int, input().split())

answer = 0
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(x1 - 1, x2):
        for c in range(y1 - 1, y2):
            graph[r][c] += 1

for r in range(100):
    for c in range(100):
        if graph[r][c] > m:
            answer += 1
print(answer)