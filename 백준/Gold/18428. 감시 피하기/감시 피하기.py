import sys
from collections import deque
from itertools import permutations

n = int(input())
graph = [list(map(str, input().split())) for _ in range(n)]
empty = []
students = []
for r in range(n):
    for c in range(n):
        if graph[r][c] == 'X':
            empty.append((r, c))
        if graph[r][c] == 'S':
            students.append((r, c))
permu = list(permutations(empty, 3))
div = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def solve(walls):
    for x, y in students:
        for dx, dy in div:
            nx, ny = x, y
            while 1:
                nx, ny = dx + nx, dy + ny
                if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in walls:
                    break
                if graph[nx][ny] == 'T':
                    return False
    return True


for walls in permu:
    if solve(walls):
        print("YES")
        sys.exit(0)
print("NO")