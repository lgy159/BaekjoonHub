def change(s, start, end):
    if start == 0:
        temp = []
        for idx in range(end, start -1, -1):
            temp.append(s[idx])
        for idx in range(end + 1, 20):
            temp.append(s[idx])
        return temp
    else:
        return s[:start] + s[end:start - 1:-1] + s[end + 1:]


answer = [i + 1 for i in range(20)]

for _ in range(10):
    start, end = map(int, input().split())
    answer = change(answer, start - 1, end - 1)

print(*answer)
