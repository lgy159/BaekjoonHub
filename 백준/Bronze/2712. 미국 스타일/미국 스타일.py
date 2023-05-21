def solve(num, p):
    if p == 'kg':
        return round(num * 2.2046, 4), "lb"
    if p == 'l':
        return round(num * 0.2642, 4), "g"
    if p == 'lb':
        return round(num * 0.4536, 4), "kg"
    if p == 'g':
        return round(num * 3.7854, 4), "l"


for _ in range(int(input())):
    a, b = input().split()
    n, m = solve(float(a), b)
    n = format(n, ".4f")
    print(n, m)
