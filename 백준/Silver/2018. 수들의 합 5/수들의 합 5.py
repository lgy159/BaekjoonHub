n = int(input())

left, right = 1, 1
count = 0
num = 1
while left < n and right < n:
    if num < n:
        right += 1
        num += right
    elif num == n:
        count += 1
        right += 1
        num += right
    else:
        num -= left
        left += 1

print(count + 1)