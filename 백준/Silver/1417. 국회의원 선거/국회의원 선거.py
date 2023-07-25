n = int(input())
people = []
for idx in range(n):
    people.append(int(input()))


count = 0
while max(people) != people[0]:
    a = people.index(max(people))
    people[a] -= 1
    people[0] += 1
    count += 1

if people.count(people[0]) > 1:
    count += 1

print(count)