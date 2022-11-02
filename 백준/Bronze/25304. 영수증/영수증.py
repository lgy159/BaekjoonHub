goal = int(input())
n = int(input())
now = 0
for _ in range(n):
    a, b = map(int,input().split())
    now += a * b
if now == goal:
    print("Yes")
else:
    print("No")