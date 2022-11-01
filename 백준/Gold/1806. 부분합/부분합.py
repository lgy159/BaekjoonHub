n, s = map(int, input().split())
nums = list(map(int, input().split()))
start, end = 0, 0
result = []
now = 0
while start < n and end <= n:
    if now < s:
        if end == n:
            break
        now += nums[end]
        end += 1
    if now >= s:
        result.append(end - start)
        now -= nums[start]
        start += 1

if result:
    print(min(result))
else:
    print(0)