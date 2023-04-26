import math

n = int(input())
lst = list(map(int, input().split()))

first, second = 0, 0

for data in lst:
    first += math.ceil(data / 30) * 10
    second += math.ceil(data / 60) * 15

    if data % 30 == 0:
        first += 10
    if data % 60 == 0:
        second += 15

if first > second:
    print("M", second)
elif first == second:
    print("Y M", second)
else:
    print("Y", first)