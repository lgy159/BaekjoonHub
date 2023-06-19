n, p = map(int, input().split())

temp = [n]
next = n
idx = 0
while 1:
    next = next * n % p
    if next in temp:
        idx = temp.index(next)
        break
    else:
        temp.append(next)

print(len(temp) - idx)