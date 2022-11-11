from collections import deque

n = int(input())

visited = [0] * (n + 1)
nums = [[] for _ in range(n + 1)]


def cal(num, type):
    if type == 0 and num % 3 == 0:
        return num // 3
    if type == 1 and num % 2 == 0:
        return num // 2

    return num - 1


def solve():
    q = deque()
    q.append(n)
    while q:
        num = q.popleft()
        if num == 1:
            return
        for i in range(3):
            next = cal(num, i)
            if visited[next]:
                continue
            visited[next] = visited[num] + 1
            nums[next].append(next)
            for data in nums[num]:
                nums[next].append(data)
            q.append(next)


solve()
nums[1].append(n)
nums[1].reverse()
#print(visited)
#print(nums)
print(visited[1])
print(*nums[1])