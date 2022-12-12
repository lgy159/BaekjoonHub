n = int(input())
graph = [[] for _ in range(n + 1)]
result = 0
for _ in range(n):
    ip = list(map(int, input().split()))
    ip.pop()
    while len(ip) > 1:
        b = ip.pop()
        a = ip.pop()
        graph[ip[0]].append((a, b))
after = 0


def DFS(start):
    global result
    global after
    visited = [False for _ in range(n + 1)]
    stack = [(start, 0)]
    visited[start] = True
    while stack:
        node, plus = stack.pop()
        for next, cost in graph[node]:
            if not visited[next]:
                visited[next] = True
                stack.append((next, plus + cost))
                if result < plus + cost:
                    after = next
                result = max(result, plus + cost)


DFS(1)
DFS(after)
print(result)
