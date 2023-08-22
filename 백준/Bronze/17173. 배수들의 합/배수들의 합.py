n, m = map(int, input().split())

lst = list(map(int, input().split()))

answer = 0
for num in range(1, n + 1):
    for data in lst:
        if num % data == 0:
            answer += num
            break

print(answer)