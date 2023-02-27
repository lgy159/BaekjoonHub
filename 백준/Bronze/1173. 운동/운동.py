import sys

n, m, M, T, R = map(int, input().split())

start = m
t = 0
while n > 0:
    if start + T <= M:
        start += T
        n -= 1
    else:
        before = start
        start = max(start - R, m)
        if before == start:
            print(-1)
            sys.exit(0)
    t += 1
print(t)