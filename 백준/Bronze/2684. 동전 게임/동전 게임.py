rule = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']
for _ in range(int(input())):
    answer = [0] * 8
    s = input()
    for idx in range(38):
        temp = s[idx:idx + 3]
        answer[rule.index(temp)] += 1

    print(*answer)