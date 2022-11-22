import sys

n = int(input())
if n == 1:
    print(0)
    sys.exit(0)
visited = [False, False] + [True] * (n - 1)
left = right = cnt = 0
primes = []


def arsto():
    for i in range(2, n + 1):
        if visited[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                visited[j] = False


def solve(start, end):
    temp = 0
    for i in range(start, end + 1):
        temp += primes[i]
    return temp


arsto()
while 1:
    temp = solve(left, right)
    if temp < n:
        right += 1
    elif temp == n:
        cnt += 1
        right += 1
    else:
        left += 1
    if right == len(primes) and left == len(primes) - 1:
        break

print(cnt)
