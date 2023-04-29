a, b, c = map(int, input().split())

now = a + b
result = 0
while 1:
    if a < 2 or b < 1 or a + b < c + 3:
        break
    a -= 2
    b -= 1
    result += 1

print(result)