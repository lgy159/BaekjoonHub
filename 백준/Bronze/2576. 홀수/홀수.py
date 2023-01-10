l = []
for i in range(7):
    a = int(input())
    if a % 2:
        l.append(a)

if not l:
    print(-1)
else:
    print(sum(l))
    print(min(l))