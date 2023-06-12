for _ in range(int(input())):
    put = input()
    num = str(int(put) + int(put[::-1]))
    left, right = 0, len(num) - 1
    flag = 0
    while left < right:
        if num[left] != num[right]:
            flag = 1
            break
        left += 1
        right -= 1
    print("YES" if not flag else "NO")
