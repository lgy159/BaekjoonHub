def twoPointer(k, s):
    left, right = 0, len(s) - 1
    cnt = 0
    m = 1e9
    while left < right:
        val = k - (s[right] + s[left])
        if m > abs(val):
            cnt = 0
            m = abs(val)
        if val > 0:
            if abs(val) == m:
                cnt += 1
            left += 1
        elif val < 0:
            if abs(val) == m:
                cnt += 1
            right -= 1
        else:
            cnt += 1
            left += 1

    print(cnt)


for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    s.sort()
    twoPointer(k, s)
