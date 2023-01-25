lst = list(map(int, input().split()))
lst.sort()
a, b, c = map(str, input())
a, b, c = ord(a) - 65, ord(b) - 65, ord(c) - 65
print(lst[a], lst[b], lst[c])
