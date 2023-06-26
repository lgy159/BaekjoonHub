for _ in range(int(input())):
    n = int(input())
    temp = [True] * (n + 1)
    for x in range(2, n + 1):
        for y in range(x, n + 1, x):
            temp[y] = not temp[y]
    print(sum(temp) - 1)