import string

tmp = string.digits + string.ascii_lowercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


while 1:
    t = list(map(str, input().split()))
    if t[0] == '0':
        break
    b, p, m = t
    b = int(b)
    np, nm = int(p, b), int(m, b)
    r = np % nm
    print(convert(r, b))
