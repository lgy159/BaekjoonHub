import sys
from collections import deque

start, end = map(int, input().split())
if start == end:
    print(0)
    sys.exit(0)


def change(idx):
    if idx == 0:
        return '*'
    if idx == 1:
        return '+'
    if idx == 2:
        return '/'


def operation(num, type):
    if type == 0:
        return num ** 2
    if type == 1:
        return num * 2
    if type == 2:
        return num // num


q = deque()
q.append((start, ""))
visited = set()
result = ''
while q:
    num, arr = q.popleft()
    if num == end:
        result = arr
        continue
    for idx in range(3):
        next = operation(num, idx)
        if next < 0 or next > max(start, end) or next in visited:
            continue
        visited.add(next)
        q.append((next, arr + str(idx)))
if result:
    for c in result:
        print(change(int(c)), end='')
else:
    print(-1)