n, k = map(int, input().split())

l = [i for i in range(n, n * k + 1, n)]
for i in range(len(l)):
    l[i] = int(str(l[i])[::-1])
print(max(l))