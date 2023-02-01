lst = []
for _ in range(3):
    temp = list(map(int, input().split()))
    lst.append(temp)

s = 0
for row in range(3):
    if lst[row].count(0) == 0:
        s = sum(lst[row])

for col in range(3):
    c = 0
    cs = 0
    for row in range(3):
        if lst[row][col] != 0:
            c += 1
            cs += lst[row][col]
    if c == 3:
        s = cs

if lst[0][0] != 0 and lst[1][1] != 0 and lst[2][2] != 0:
    s = lst[0][0] + lst[1][1] + lst[2][2]
if lst[2][0] != 0 and lst[1][1] != 0 and lst[0][2] != 0:
    s = lst[2][0] + lst[1][1] + lst[0][2]

if lst[0][0] == 0 and lst[1][1] == 0 and lst[2][2] == 0:
    for num in range(1, 20001):
        temp = - sum(lst[2]) + sum(lst[0]) + num
        if num + temp == sum(lst[1]):
            lst[0][0] = num
            s = sum(lst[0])
            break

if lst[2][0] == 0 and lst[1][1] == 0 and lst[0][2] == 0:
    for num in range(1, 20001):
        temp = - sum(lst[2]) + sum(lst[0]) + num
        if num + temp == sum(lst[1]):
            lst[0][2] = num
            s = sum(lst[0])
            break
# start
for _ in range(3):
    for row in range(3):
        if lst[row].count(0) == 1:
            for col in range(3):
                if lst[row][col] == 0:
                    lst[row][col] = s - lst[row][col - 1] - lst[row][col - 2]
                    break

    for col in range(3):
        c = 0
        for row in range(3):
            if lst[row][col] == 0:
                c += 1
        if c == 1:
            for row in range(3):
                if lst[row][col] == 0:
                    lst[row][col] = s - lst[row - 1][col] - lst[row - 2][col]
                    break

    for col in range(3):
        c = 0
        for row in range(3):
            if lst[row][row] == 0:
                c += 1
        if c == 1:
            for row in range(3):
                if lst[row][row] == 0:
                    lst[row][row] = s - lst[row - 1][row - 1] - lst[row - 2][row - 2]
                    break

    for col in range(3):
        c = 0
        for row in range(3):
            if lst[row][2 - row] == 0:
                c += 1
        if c == 1:
            for row in range(3):
                if lst[row][2 - row] == 0:
                    lst[row][2 - row] = s - lst[row - 1][2 - row - 1] - lst[row - 2][2 - row - 2]
                    break

for idx in range(3):
    print(*lst[idx])