n = int(input())
s = input()
a = s.count("A")
b = s.count("B")

if a == b:
    print("Tie")
elif a > b:
    print("A")
else:
    print("B")