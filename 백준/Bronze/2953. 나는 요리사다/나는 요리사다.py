t = [list(map(int, input().split())) for _ in range(5)]
a = []
for data in t:
    a.append(sum(data))

print(a.index(max(a)) + 1, max(a))