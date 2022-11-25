import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n)]
parent = [i for i in range(n)]


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parent[max(x, y)] = min(x, y)
        return False
    return True


result = 0
for idx in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    if not result and union(a, b):
        result = idx + 1
print(result)
