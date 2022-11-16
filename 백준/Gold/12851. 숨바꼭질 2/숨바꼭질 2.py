from collections import deque

start, end = map(int, input().split())
visited = [0] * 100001


def solve(num, type):
    if type == 0:
        return num * 2
    if type == 1:
        return num + 1
    if type == 2:
        return num - 1


q = deque()
q.append(start)
visited[start] = 1
result = 0
while q:
    num = q.popleft()
    if num == end:
        result += 1
    for i in range(3):
        next = solve(num, i)
        if next < 0 or next > 100000:
            continue
        if visited[next] == 0 or visited[next] == visited[num] + 1:
            visited[next] = visited[num] + 1
            q.append(next)
print(visited[end] - 1)
print(result)