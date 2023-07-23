for _ in range(int(input())):
    n = int(input())
    temp = []
    for x in range(n // 2 + 1):
        for y in range(n):
            if x == y:
                continue
            if x + y == n:
                temp.append((x, y))

    print("Pairs for %d: " % n, end='')
    for idx in range(len(temp)):
        if idx == len(temp) - 1:
            print(*temp[idx], end='')
            break
        else:
            print(*temp[idx], end=', ')
    print()
