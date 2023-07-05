o = input()

zero = o.split('0')
one = o.split('1')

az = ao = 0
for data in zero:
    if data:
        az += 1
for data in one:
    if data:
        ao += 1

print(min(az, ao))
