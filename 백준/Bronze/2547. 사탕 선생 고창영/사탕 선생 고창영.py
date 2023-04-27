for _ in range(int(input())):
    t = input()
    n = int(input())
    temp = 0
    for _ in range(n):
        temp += int(input())
    if temp % n == 0:
        print("YES")
    else:
        print("NO")


