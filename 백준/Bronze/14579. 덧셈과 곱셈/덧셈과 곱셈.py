def s(n):
    return n * (n + 1) // 2


a, b = map(int, input().split())

result = 1
for i in range(a, b + 1):
    result *= s(i)

print(result % 14579)
