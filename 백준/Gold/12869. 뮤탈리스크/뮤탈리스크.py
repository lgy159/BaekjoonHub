from collections import deque

n = int(input())
lst = list(map(int, input().split()))
move = [9, 3, 1]
visited = [[[False for _ in range(61)] for _ in range(61)] for _ in range(61)]
lst.sort()
lst.reverse()
while len(lst) <= 3:
    lst.append(0)

visited[lst[0]][lst[1]][lst[2]] = True
q = deque([lst])
while q:
    one, two, three, cnt = q.popleft()
    if one <= 0 and two <= 0 and three <= 0:
        break
    for idx in range(3):
        new_one = one - move[idx]
        new_two = two - move[idx - 1]
        new_three = three - move[idx - 2]
        if new_one < 0:
            new_one = 0
        if new_two < 0:
            new_two = 0
        if new_three < 0:
            new_three = 0
        if not visited[new_one][new_two][new_three]:
            visited[new_one][new_two][new_three] = True
            q.append((new_one, new_two, new_three, cnt + 1))
        new_two = two - move[idx - 2]
        new_three = three - move[idx - 1]
        if new_two < 0:
            new_two = 0
        if new_three < 0:
            new_three = 0
        if not visited[new_one][new_two][new_three]:
            visited[new_one][new_two][new_three] = True
            q.append((new_one, new_two, new_three, cnt + 1))

print(cnt)
