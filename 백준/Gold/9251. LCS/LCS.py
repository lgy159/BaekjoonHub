firstWord = input()
lastWord = input()

arr = [[0 for _ in range(len(lastWord) + 1)] for _ in range(len(firstWord) + 1)]

for r in range(1, len(firstWord) + 1):
    for c in range(1, len(lastWord) + 1):
        if firstWord[r - 1] == lastWord[c - 1]:
            arr[r][c] = arr[r-1][c-1] + 1
        else:
            arr[r][c] = max(arr[r-1][c], arr[r][c-1])

result = 0
for i in range(len(arr)):
    result = max(result, max(arr[i]))
print(result)