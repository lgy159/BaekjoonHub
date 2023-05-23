import sys

result = 1
input = sys.stdin.readline
for _ in range(int(input())):
    result += int(input()) - 1
print(result)

