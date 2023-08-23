import sys

lst = list(map(int, input().split()))

for idx in range(1, len(lst)):
    if lst[idx] < lst[idx - 1]:
        print("Bad")
        sys.exit(0)

print("Good")