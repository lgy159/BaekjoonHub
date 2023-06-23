import sys

p, k = map(int, input().split())

t = 0
for n in range(2, p + 1):
    if p % n == 0:
        t = n
        p = p // n
        break
    if n >= k:
        print("GOOD")
        sys.exit(0)

if p < k or t < k:
    print("BAD", min(p, t))
else:
    print("GOOD")