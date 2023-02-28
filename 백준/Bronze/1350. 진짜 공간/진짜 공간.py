import math

n = int(input())
cd = list(map(int, input().split()))
k = int(input())

result = 0
for data in cd:
    if data == 0:
        continue
    temp = math.ceil(data / k)
    result += temp * k

print(result)