t = [0, 1, 0, 0]

for _ in range(int(input())):
    l, r = map(int, input().split())
    t[l], t[r] = t[r], t[l]

print(t.index(1))