lst = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
result = 0
t = ''
for i in range(3):
    temp = input()
    if i == 2:
        result = int(t) * 10 ** (lst.index(temp))
    else:
        t += str(lst.index(temp))

print(result)