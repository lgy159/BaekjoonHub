n = int(input())
students = [input() for _ in range(n)]

k = 1
while 1:
    temp = set()
    for data in students:
        temp.add(data[len(data) - k:len(data)])
    if len(temp) == n or k == len(students[0]):
        break
    k += 1
print(k)
