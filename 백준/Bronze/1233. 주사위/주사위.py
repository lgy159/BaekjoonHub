a, b, c = map(int, input().split())
d = {}
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for m in range(1, c + 1):
            if not i + j + m in d:
                d[i + j + m] = 1
            else:
                d[i + j + m] += 1

m = 0
for data in d:
    m = max(m, d[data])

for data in d:
    if d[data] == m:
        print(data)
        break