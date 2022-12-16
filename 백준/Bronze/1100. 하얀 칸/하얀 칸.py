graph = [input() for _ in range(8)]

result = 0
for idx in range(8):
    for jdx in range(8):
        if not (idx + jdx) % 2 and graph[idx][jdx] == 'F':
            result += 1

print(result)
