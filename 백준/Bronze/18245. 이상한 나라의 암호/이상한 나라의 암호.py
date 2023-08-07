idx = 2
while 1:
    s = input()
    if s == "Was it a cat I saw?":
        break
    for i in range(0, len(s), idx):
        print(s[i], end='')
    print()
    idx += 1