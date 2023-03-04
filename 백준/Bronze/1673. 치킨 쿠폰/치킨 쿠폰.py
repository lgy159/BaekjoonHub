while True:
    try:
        n, k = map(int, input().split())
        cnt = n
        while n // k > 0:
            cnt += n // k
            n = n % k + n // k

        print(cnt)
    except EOFError:
        break