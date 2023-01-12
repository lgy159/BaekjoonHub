from collections import deque

n, m, t = map(int, input().split())
circle = []
for _ in range(n):
    temp = deque(map(int, input().split()))
    circle.append(temp)
test_case = []
for _ in range(t):
    x, d, k = map(int, input().split())
    test_case.append((x, d, k))


def solve(x, d, k):
    lst = []
    start = 0
    while start < n:
        if (start + 1) % x == 0:
            lst.append(start)
        start += 1
    if d:
        for idx in lst:
            for _ in range(k):
                circle[idx].rotate(-1)
    else:
        for idx in lst:
            for _ in range(k):
                circle[idx].rotate(1)

    delete = []
    for idx in range(n):
        for jdx in range(m):
            if circle[idx][jdx] == circle[idx][jdx - 1] and circle[idx][jdx] != 0:
                delete.append((idx, jdx))
                delete.append((idx, jdx - 1))
            if circle[idx][jdx] == circle[idx - 1][jdx] and idx != 0 and circle[idx][jdx] != 0:
                delete.append((idx, jdx))
                delete.append((idx - 1, jdx))
    if delete:
        for x, y in delete:
            circle[x][y] = 0
    else:
        s = 0
        c = 0
        ever = 0
        for i in range(n):
            s += sum(circle[i])
            for j in range(m):
                if circle[i][j]:
                    c += 1
        if c != 0:
            ever = s / c
        for idx in range(n):
            for jdx in range(m):
                if circle[idx][jdx] == 0:
                    continue
                elif circle[idx][jdx] == ever:
                    pass
                elif circle[idx][jdx] > ever:
                    circle[idx][jdx] -= 1
                else:
                    circle[idx][jdx] += 1


for x, d, k in test_case:
    solve(x, d, k)

s = 0
for i in range(n):
    s += sum(circle[i])
print(s)