import sys

input = sys.stdin.readline

for i in range(int(input().rstrip())):
    a, b = map(int, input().rstrip().split())
    temp = a
    arr = []
    idx = 1
    while idx <= b:
        if a ** idx % 10 not in arr:
            arr.append(a ** idx % 10)
        else:
            break
        idx += 1
    b -= 1
    if 0 in arr:
        arr.remove(0)
        arr.append(10)
    print(arr[b % len(arr)])