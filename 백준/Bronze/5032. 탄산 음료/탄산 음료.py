e, f, c = map(int, input().split())

e = e + f
q = 0
count = 0
while 1:
    q = e % c
    count += e // c
    e = e // c + q
    if e < c:
        break

print(count)
