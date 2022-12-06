import sys

input = sys.stdin.readline

s = input().rstrip()
boom = list(map(str, input().rstrip()))
stack = []

for c in s:
    stack.append(c)
    if stack[len(stack) - len(boom):len(stack)] == boom:
        for _ in range(len(boom)):
            stack.pop()

if stack:
    print(*stack, sep='')
else:
    print("FRULA")