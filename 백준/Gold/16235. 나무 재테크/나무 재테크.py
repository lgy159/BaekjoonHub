import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().rstrip().split())
# m : 나무의 개수, k : 몇 년 뒤
nutrient = [[5 for _ in range(n)] for _ in range(n)]
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, age = map(int, input().rstrip().split())
    trees[x-1][y-1].append(age)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def spring():
    for r in range(n):
        for c in range(n):
            treeLength = len(trees[r][c])
            for tree in range(treeLength):
                if trees[r][c][tree] <= nutrient[r][c]:
                    nutrient[r][c] -= trees[r][c][tree]
                    trees[r][c][tree] += 1
                else:
                    for _ in range(tree, treeLength):
                        nutrient[r][c] += trees[r][c].pop() // 2
                    break


def fall():
    for r in range(n):
        for c in range(n):
            for tree in trees[r][c]:
                if tree % 5 == 0:
                    for idx in range(8):
                        x, y = r + dx[idx], c + dy[idx]
                        if 0 <= x < n and 0 <= y < n:
                            trees[x][y].appendleft(1)
            nutrient[r][c] += arr[r][c]


for _ in range(k):
    spring()
    fall()
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(trees[i][j])
print(cnt)
