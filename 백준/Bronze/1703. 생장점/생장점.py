while 1:
    t = list(map(int, input().split()))
    if t[0] == 0:
        break
    count = 1
    for idx in range(1, len(t), 2):
        count *= t[idx]
        count -= t[idx + 1]
    print(count)