n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = 0
for idx in range(n):
    result += graph[idx][0] * graph[idx-1][1] - graph[idx-1][0] * graph[idx][1]
result = round(abs(result) / 2, 1)
print(result)
