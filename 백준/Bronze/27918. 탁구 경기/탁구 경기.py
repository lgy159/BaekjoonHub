a, b = 0, 0
for _ in range(int(input())):
    t = input()
    if t == "D":
        a += 1
    else:
        b += 1
    if abs(a - b) >= 2:
        break

print("%d:%d" % (a, b))