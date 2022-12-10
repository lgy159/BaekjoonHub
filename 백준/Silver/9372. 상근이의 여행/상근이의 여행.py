test_Case = int(input())
for _ in range(test_Case):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(m)]
    print(n - 1)