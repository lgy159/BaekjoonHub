alpha = ['A', 'B', 'C', 'D', 'E', 'F']
graph = [[0 for _ in range(6)] for _ in range(6)]
o = []
for _ in range(36):
    temp = input()
    o.append((alpha.index(temp[0]), int(temp[1]) - 1))

result = "Valid"
r, c = -1, -1
for nr, nc in o:
    if r == -1 and c == -1:
        r, c = nr, nc
        sr, sc = r, c
        graph[r][c] += 1
        continue

    if abs(r - nr) * abs(c - nc) != 2:
        result = "Invalid"
    r, c = nr, nc
    graph[r][c] += 1

if abs(r - sr) * abs(c - sc) != 2:
    result = "Invalid"

c = 0
for i in range(6):
    c += graph[i].count(1)

if c != 36:
    result = "Invalid"

print(result)