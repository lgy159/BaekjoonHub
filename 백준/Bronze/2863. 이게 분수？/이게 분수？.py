from collections import deque

q = deque()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for data in a:
    q.append(data)

for data in b[::-1]:
    q.append(data)

result = []
for _ in range(4):
    result.append(q[0] // q[2] + q[1] // q[3])
    q.rotate(1)

print(result.index(max(result)))