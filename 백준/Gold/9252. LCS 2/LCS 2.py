firstWord = input()
lastWord = input()

arr = [[0 for _ in range(len(lastWord) + 1)] for _ in range(len(firstWord) + 1)]
word_arr = [["" for _ in range(len(lastWord) + 1)] for _ in range(len(firstWord) + 1)]

for r in range(1, len(firstWord) + 1):
    for c in range(1, len(lastWord) + 1):
        if firstWord[r - 1] == lastWord[c - 1]:
            arr[r][c] = arr[r - 1][c - 1] + 1
            word_arr[r][c] = word_arr[r - 1][c - 1] + firstWord[r - 1]
        else:
            arr[r][c] = max(arr[r - 1][c], arr[r][c - 1])
            if arr[r - 1][c] > arr[r][c - 1]:
                word_arr[r][c] = word_arr[r - 1][c]
            else:
                word_arr[r][c] = word_arr[r][c - 1]


result = 0
res_str = ""
for i in range(len(firstWord) + 1):
    for j in range(len(lastWord) + 1):
        if arr[i][j] > result:
            result = arr[i][j]
            res_str = word_arr[i][j]
print(result)
print(res_str)
