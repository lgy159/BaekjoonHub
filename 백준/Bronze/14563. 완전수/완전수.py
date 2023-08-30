n = int(input())
nums = list(map(int, input().split()))


def solve(num):
    temp = []
    for i in range(1, num):
        if num % i == 0:
            temp.append(i)

    t = sum(temp)

    if t == num:
        return "Perfect"
    elif t < num:
        return "Deficient"
    else:
        return "Abundant"


for num in nums:
    print(solve(num))
