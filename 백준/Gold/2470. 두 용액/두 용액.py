import math

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

start, end = 0, n - 1
result = math.inf
x, y = lst[start], lst[end]

# -100, -87, -3, 0, 3

while start < end:
    l = lst[end] + lst[start]
    if abs(l) < result:
        result = abs(l)
        x, y = lst[start], lst[end]

    if l < 0:
        start += 1
    elif l > 0:
        end -= 1
    else:
        break

print(x, y)

