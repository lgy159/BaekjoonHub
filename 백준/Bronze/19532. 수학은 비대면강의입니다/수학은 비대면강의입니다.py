a, b, c, d, e, f = map(int, input().split())

def solve(x, y):
    if a * x + b * y == c and d * x + e * y == f:
        return 1
    return 0


for x in range(-999, 1000):
    for y in range(-999, 1000):
        if solve(x, y):
            print(x, y)