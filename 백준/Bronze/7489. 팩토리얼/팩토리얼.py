for _ in range(int(input())):
    n = int(input())
    result = 1
    for num in range(2, n + 1):
        result *= num
        if result % 10 == 0:
            result = result // 10

    print(str(result).rstrip('0')[-1])