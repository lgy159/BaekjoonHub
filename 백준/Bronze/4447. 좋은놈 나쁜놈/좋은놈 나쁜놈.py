for _ in range(int(input())):
    s = input()
    t = s.lower()
    g = t.count('g')
    b = t.count('b')
    if g > b:
        print(s, "is GOOD")
    elif g == b:
        print(s, "is NEUTRAL")
    else:
        print(s, "is A BADDY")