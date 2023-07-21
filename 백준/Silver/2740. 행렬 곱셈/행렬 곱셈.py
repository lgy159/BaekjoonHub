n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

graph = [[0 for _ in range(k)] for _ in range(n)]


# n, m = 3, 2
# m, k = 2, 3
for r in range(n):
    for c in range(k):
        temp = 0
        for x in range(m):
            temp += a[r][x] * b[x][c]
        graph[r][c] = temp

for r in range(n):
    print(*graph[r])