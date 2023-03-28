a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

t = [a, b, c, d]
t.sort()
t.reverse()
t.pop()

print(sum(t) + max(e, f))