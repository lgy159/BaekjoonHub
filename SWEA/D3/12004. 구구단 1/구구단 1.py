T = int(input())
space = [0] * 101
for i in range(1, 10):
    for j in range(1, 10):
        space[i * j] = 1

for test_case in range(1, T + 1):
    n = int(input())
    if space[n]:
        print("#%d Yes" % test_case)
    else:
        print("#%d No" % test_case)

