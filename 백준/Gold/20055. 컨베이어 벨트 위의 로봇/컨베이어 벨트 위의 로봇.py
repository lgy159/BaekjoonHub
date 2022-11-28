from collections import deque

n, k = map(int, input().split())
container = deque(map(int, input().split()))
robots = []
cnt = 1
while 1:
    # 1번
    container.rotate(1)
    for idx in range(len(robots)):
        robots[idx] += 1
    # 내리기
    if n - 1 in robots:
        robots.remove(n - 1)
    # 2번
    for idx, robot in enumerate(robots):
        if container[robot + 1] and robots[idx] + 1 not in robots:
            container[robot + 1] -= 1
            robots[idx] += 1

    # 내리기
    if n - 1 in robots:
        robots.remove(n - 1)
    # 3번
    if container[0]:
        robots.append(0)
        container[0] -= 1

    # 4번
    if container.count(0) >= k:
        break
    cnt += 1
print(cnt)

