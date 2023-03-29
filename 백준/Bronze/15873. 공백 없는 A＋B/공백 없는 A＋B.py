import sys

s = input()

a = 0
if '10' in s:
    a = 10
    s = s.replace('10', '')
else:
    print(int(s[0]) + int(s[1]))
    sys.exit(0)
if len(s) == 0:
    print(20)
else:
    print(a + int(s))