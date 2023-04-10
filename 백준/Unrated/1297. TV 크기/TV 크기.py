import math

l, x, y = map(int, input().split())

n = math.sqrt(l ** 2 / (x ** 2 + y ** 2))
x = math.floor(x * n)
y = math.floor(y * n)
print(x, y)