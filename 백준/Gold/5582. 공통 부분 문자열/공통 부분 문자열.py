a = input()
b = input()

dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
result = 0

for idx in range(1, len(a) + 1):
    for jdx in range(1, len(b) + 1):
        if a[idx - 1] == b[jdx - 1]:
            dp[idx][jdx] = dp[idx - 1][jdx - 1] + 1
    result = max(result, max(dp[idx]))

print(result)