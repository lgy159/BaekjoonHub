a = int(input())
b = int(input())
c = int(input())
s = a + b + c

if a == 60 and b == 60 and c == 60:
    print("Equilateral")
elif s == 180 and (a == b or b == c or a == c):
    print("Isosceles")
elif s == 180:
    print("Scalene")
else:
    print("Error")