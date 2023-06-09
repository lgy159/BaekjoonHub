a, b, c = map(int, input().split())
temp = [0] * 101
for _ in range(3):
    x, y = map(int, input().split())
    for data in range(x, y):
        temp[data] += 1

result = 0
for data in temp:
    if data == 1:
        result += a
    if data == 2:
        result += b * 2
    if data == 3:
        result += c * 3
print(result)