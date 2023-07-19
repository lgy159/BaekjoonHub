

for _ in range(int(input())):
    temp = input()
    row, col = map(int, input().split())
    graph = [list(input()) for _ in range(row)]
    count = 0
    for r in range(row):
        for c in range(col):
            if graph[r][c] == 'v':
                if r + 1 < row and graph[r + 1][c] == 'o':
                    if r + 2 < row and graph[r + 2][c] == '^':
                        count += 1
            if graph[r][c] == '>':
                if c + 1 < col and graph[r][c + 1] == 'o':
                    if c + 2 < col and graph[r][c + 2] == '<':
                        count += 1
    print(count)



