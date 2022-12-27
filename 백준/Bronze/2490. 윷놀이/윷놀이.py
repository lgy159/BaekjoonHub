a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

def aaa(t):
    if t == 1:
        print("A")
    if t == 2:
        print("B")
    if t == 3:
        print("C")
    if t == 4:
        print("D")
    if t == 0:
        print("E")


aaa(a.count(0))
aaa(b.count(0))
aaa(c.count(0))
