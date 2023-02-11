from itertools import combinations
from math import gcd

for _ in range(int(input())):
    lst = list(map(int, input().split()))
    lst.pop(0)
    combi = list(combinations(lst, 2))
    result = 0
    for data in combi:
        result += gcd(*data)
    print(result)
