lst = [list(map(int, input().split())) for _ in range(9)]
result = 0

x, y = 0, 0
for r in range(9):
    for c in range(9):
        if result < lst[r][c]:
            result = lst[r][c]
            x, y = r, c

print(result)
print(x + 1, y + 1)