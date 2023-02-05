import sys

row, col = map(int, input().split())
if row > col:
    row, col = col, row
if row == col:
    print(0)
    sys.exit(0)
print(col - row - 1)
for i in range(row + 1, col):
    print(i, end=' ')