graph = []

col = 0
for idx in range(5):
    temp = input()
    graph.append(temp)
    col = max(col, len(temp))

row = 5

for c in range(col):
    for r in range(row):
        if len(graph[r]) > c:
            print(graph[r][c], end='')