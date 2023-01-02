from collections import deque
from copy import deepcopy

n = int(input())
dices = deque()
for _ in range(n):
    lst = deque(map(int, input().split()))
    dices.append(lst)


def switch(idx):
    if idx == 0:
        return 5
    if idx == 1:
        return 3
    if idx == 2:
        return 4
    if idx == 3:
        return 1
    if idx == 4:
        return 2
    if idx == 5:
        return 0

result = 0
for i in range(6):
    t = 0
    end = dices[0][i]
    end_idx = i
    for j in range(n):
        start_idx = dices[j].index(end)
        end_idx = switch(start_idx)
        start = dices[j][start_idx]
        end = dices[j][end_idx]
        temp_sum = 0
        for d in range(6):
            if d == start_idx or d == end_idx:
                continue
            temp_sum = max(temp_sum, dices[j][d])
        t += temp_sum
    result = max(result, t)
print(result)