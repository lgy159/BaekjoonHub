n, power = map(int, input().split())

numbers = [n]


def solve(n):
    temp = 0
    for data in str(n):
        temp += int(data) ** power
    return temp


while 1:
    temp = solve(numbers[-1])
    if not temp in numbers:
        numbers.append(temp)
    else:
        print(numbers.index(temp))
        break
