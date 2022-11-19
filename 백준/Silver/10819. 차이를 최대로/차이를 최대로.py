from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
permu = list(permutations(nums, n))


def solve(arr):
    result = 0
    for idx in range(1, n):
        result += abs(arr[idx - 1] - arr[idx])
    return result


answer = 0
for data in permu:
    answer = max(answer, solve(data))

print(answer)
