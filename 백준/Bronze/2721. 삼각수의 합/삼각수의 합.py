for _ in range(int(input())):
    print(sum([i for i in range(1, sum([i for i in range(1, int(input()) + 2)]))]))