from itertools import combinations


def find_value(count_arr):
    combi = list(combinations(count_arr, 2))

    temp = 1
    for data in combi:
        temp *= data[0] + data[1]

    return temp % 100


name = input()
result = (-1, "")
for _ in range(int(input())):
    team = input()
    temp = []
    for data in "LOVE":
        temp.append(team.count(data) + name.count(data))

    c = find_value(temp)
    if result[0] < c:
        result = (c, team)
    elif result[0] == c and result[1] > team:
        result = (c, team)
print(result[1])

