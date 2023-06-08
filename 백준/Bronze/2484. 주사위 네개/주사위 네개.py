n = int(input())
result = 0
for _ in range(n):
    temp = list(map(int, input().split()))
    c = set(temp)
    many = 0
    num = 0
    for data in c:
        if many < temp.count(data):
            many = temp.count(data)
            num = data
    if len(c) == 4:
        result = max(result, max(c) * 100)
    elif len(c) == 3:
        result = max(result, 1000 + num * 100)
    else:
        if many == 2:
            result = max(result, 2000 + 500 * sum(c))
        if many == 3:
            result = max(result, 10000 + num * 1000)
        if many == 4:
            result = max(result, 50000 + num * 5000)

print(result)
