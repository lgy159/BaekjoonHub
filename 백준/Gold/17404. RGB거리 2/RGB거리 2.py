import copy

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = []
for a in range(3):
    dp = copy.deepcopy(graph)
    for i in range(3):
        dp[0][i] = dp[0][a]
    dp[1][a] = 1e9
    for idx in range(1, n):
        dp[idx][0] = min(dp[idx - 1][1], dp[idx - 1][2]) + dp[idx][0]
        dp[idx][1] = min(dp[idx - 1][0], dp[idx - 1][2]) + dp[idx][1]
        dp[idx][2] = min(dp[idx - 1][0], dp[idx - 1][1]) + dp[idx][2]

    for i in range(3):
        if a != i:
            result.append(dp[n - 1][i])
print(min(result))