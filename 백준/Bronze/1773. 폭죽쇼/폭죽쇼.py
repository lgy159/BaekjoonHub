n, l = map(int, input().split())
t = [False] * (l + 1)
for _ in range(n):
    for idx in range(0, l + 1, int(input())):
        t[idx] = True
t[0] = False
print(sum(t))
