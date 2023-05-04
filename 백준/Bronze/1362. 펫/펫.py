test_case = 1
while 1:
    o, w = map(int, input().split())
    if o == 0 and w == 0:
        break
    while 1:
        order, n = input().split()
        if order == '#' and n == '0':
            break
        if order == 'F':
            w += int(n)
        elif order == 'E':
            w -= int(n)
        if w <= 0:
            w = -1e9
    if w <= 0:
        print("%d RIP" % test_case)
    elif o // 2 < w < o * 2:
        print("%d :-)" % test_case)
    else:
        print("%d :-(" % test_case)
    test_case += 1