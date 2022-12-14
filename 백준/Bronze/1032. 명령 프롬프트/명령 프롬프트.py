n = int(input())
lst = [input() for _ in range(n)]
result = ""

for idx in range(len(lst[0])):
    temp = 0
    flag = 0
    for jdx in range(n):
        if temp == 0:
            temp = lst[jdx][idx]
        elif temp != lst[jdx][idx]:
            flag = 1
            break
    if flag:
        result += "?"
    else:
        result += temp

print(result)