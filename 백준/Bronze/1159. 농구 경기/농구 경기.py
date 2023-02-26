n = int(input())
d = {}
for _ in range(n):
    temp = input()[0]
    if not temp in d:
        d[temp] = 1
    else:
        d[temp] += 1

r = 0
for data in d.values():
    r = max(r, data)

d = sorted(d.items())
if r < 5:
    print("PREDAJA")
else:
    for key, value in d:
        if value >= 5:
            print(key, end='')
