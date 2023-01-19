import math

start = int(input())
end = int(input())

result = []
for i in range(start, end + 1):
    if int(math.sqrt(i)) ** 2 == i:
        result.append(i)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)