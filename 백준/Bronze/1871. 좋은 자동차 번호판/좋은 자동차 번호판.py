from string import ascii_uppercase

for _ in range(int(input())):
    a, b = input().split('-')
    alpha = ascii_uppercase
    n = 0
    for idx, c in enumerate(a):
        n += 26 ** (len(a) - idx - 1) * (alpha.index(c))
    print("nice" if abs(n - int(b)) <= 100 else "not nice")
