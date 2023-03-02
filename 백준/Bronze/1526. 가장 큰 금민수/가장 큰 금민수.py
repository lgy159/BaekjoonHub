n = input()

while int(n) > 0:
    n = str(n)
    temp = 0
    for data in n:
        if data != '4' and data != '7':
            temp = 1
            break
    if temp == 1:
        n = int(n) - 1
    else:
        print(n)
        break
