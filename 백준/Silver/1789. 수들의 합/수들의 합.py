import sys

num = int(input())
if num == 1:
    print(1)
    sys.exit(0)
idx = 0
now = 0
while 1:
    now += idx
    if now == num:
        break
    elif now > num:
        idx -= 1
        break
    idx += 1


print(idx)