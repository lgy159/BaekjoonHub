n = int(input())
g = []

for num in range(1, n + 1):
    if n % num == 0:
        g.append(num)


result = (0, 1e9)
for a in g:
    for b in g:
        for c in g:
            if a * b * c == n and result[1] > a + b + c:
                result = ((a, b, c), a + b + c)

print(*result[0])