a, b, c = 1, 0, 0
order = input()

for o in order:
    if o == 'A':
        a, b = b, a
    if o == 'B':
        b, c = c, b
    if o == 'C':
        a, c = c, a

print([a, b, c].index(1) + 1)