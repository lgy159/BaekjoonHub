n = int(input())

while 1:
    temp = int(input())
    if temp == 0:
        break

    if temp % n == 0:
        print("%d is a multiple of %d." % (temp, n))
    else:
        print("%d is NOT a multiple of %d." % (temp, n))
