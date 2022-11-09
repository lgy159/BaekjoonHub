from collections import deque


def solve(arr):
    q = deque(arr)
    while 1:
        for i in range(1, 6):
            q[0] -= i
            if q[0] <= 0:
                q[0] = 0
                q.rotate(-1)
                return q
            q.rotate(-1)


for _ in range(10):
    test_case = int(input())
    nums = list(map(int, input().split()))
    result = solve(nums)
    print("#%d " % test_case, end='')
    print(*result)
