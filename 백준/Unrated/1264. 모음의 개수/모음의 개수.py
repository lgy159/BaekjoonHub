while 1:
    temp = input()
    temp = temp.lower()
    if temp == '#':
        break
    print(temp.count('i') + temp.count('e') + temp.count('o') + temp.count('u') + temp.count('a'))