import math
from itertools import combinations

n = int(input())
for _ in range(n):
    lst = list(map(int, input().split()))
    m = 0
    for a, b in list(combinations(lst, 2)):
        m = max(m, math.gcd(a, b))
    print(m)