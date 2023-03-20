from itertools import combinations
from math import lcm

num_list = list(map(int, input().split()))

combi = list(combinations(num_list, 3))

result = 1e9
for data in combi:
    temp = lcm(data[0], data[1])
    next = lcm(temp, data[2])
    result = min(result, next)

print(result)

