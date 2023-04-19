while 1:
    n = int(input())
    if n == 0:
        break
    words = []
    for _ in range(n):
        t = input()
        words.append((t.lower(), t))
    words.sort()
    print(words[0][1])