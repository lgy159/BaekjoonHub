import copy
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

n = int(input())
graphs = [list(map(int, input().split())) for _ in range(n)]
type = [0, 1, 2, 3]  # 하 우 좌 상
result = 0

def DFS(arr):
    global result
    global graph
    if len(arr) == 5:
        graph = copy.deepcopy(graphs)
        for data in arr:
            solve(data)
        for row in range(n):
            result = max(result, max(graph[row]))
        return

    for idx in range(4):
        arr.append(type[idx])
        DFS(arr)
        arr.pop()


def merge(q, type, row):
    # type 0 : 오른쪽, 아래
    temp = [0] * n
    req = deque()
    idx = len(q) - 1
    while idx > 0:
        if q[idx] == q[idx - 1] and not temp[idx] and not temp[idx - 1]:
            temp[idx], temp[idx - 1] = 1, 1
            req.appendleft(q[idx] * 2)
        if not temp[idx]:
            req.appendleft(q[idx])
        idx -= 1
    if not temp[0] and q:
        req.appendleft(q[0])

    if type == 0:  # 우
        idx = n - 1
        while idx >= 0:
            if req:
                graph[row][idx] = req.pop()
            else:
                graph[row][idx] = 0
            idx -= 1
    if type == 1:  # 좌
        idx = 0
        while idx < n:
            if req:
                graph[row][idx] = req.pop()
            else:
                graph[row][idx] = 0
            idx += 1
    if type == 2:  # 상
        idx = n - 1
        while idx >= 0:
            if req:
                graph[idx][row] = req.pop()
            else:
                graph[idx][row] = 0
            idx -= 1
    if type == 3:  # 하
        idx = 0
        while idx < n:
            if req:
                graph[idx][row] = req.pop()
            else:
                graph[idx][row] = 0
            idx += 1


def solve(type):
    if type == 0:  # 우
        for row in range(n):
            q = deque()
            for col in range(n):
                if graph[row][col]:
                    q.append(graph[row][col])
            merge(q, 0, row)
    if type == 1:  # 좌
        for row in range(n):
            q = deque()
            for col in range(n - 1, -1, -1):
                if graph[row][col]:
                    q.append(graph[row][col])
            merge(q, 1, row)
    if type == 2:  # 상
        for row in range(n):
            q = deque()
            for col in range(n):
                if graph[col][row]:
                    q.append(graph[col][row])
            merge(q, 2, row)
    if type == 3:  # 하
        for row in range(n):
            q = deque()
            for col in range(n - 1, -1, -1):
                if graph[col][row]:
                    q.append(graph[col][row])
            merge(q, 3, row)


DFS([])
print(result)
