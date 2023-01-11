import sys

n = int(input())
num_list = list(map(int, input().split()))

def find(num):
    return num * a + b


def verification():
    start = num_list[0]
    for idx in range(1, n):
        if find(start) != num_list[idx]:
            return False
        start = num_list[idx]
    return True


if n == 1:
    print("A")
    sys.exit(0)
elif n == 2:
    if num_list[1] - num_list[0] == 0:
        print(num_list[0])
    else:
        print("A")
    sys.exit(0)

if num_list[1] - num_list[0] == 0:
    a = 1
    b = 0
    if not verification():
        print("B")
    else:
        print(num_list[0])
    sys.exit(0)

else:
    a = (num_list[2] - num_list[1]) // (num_list[1] - num_list[0])
    b = num_list[1] - num_list[0] * a




if not verification():
    print("B")
else:
    print(find(num_list[n - 1]))
