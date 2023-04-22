temp = []
result = 1000
for _ in range(10):
    n = int(input())
    if temp:
        temp.append(temp[-1] + n)
    else:
        temp.append(n)
    result = min(result, abs(temp[-1] - 100))

if 100 + result in temp:
    print(100 + result)
else:
    print(100 - result)