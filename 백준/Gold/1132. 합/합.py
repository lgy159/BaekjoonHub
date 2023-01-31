n = int(input())
dict = {}
notZero = []  # 0이 되면 안되는 알파벳들
for _ in range(n):
    s = input()
    if not s[0] in notZero:
        notZero.append(s[0])
    i = 1
    for idx in range(len(s) - 1, -1, -1):
        if not s[idx] in dict:
            dict[s[idx]] = i  # dict에 없는 알파벳이면 추가
        else:
            dict[s[idx]] += i  # 해당 자리수의 값만큼 추가
        i *= 10
# 가장 큰 값을 가진 알파벳에 9를 넣는 방식
dict = sorted(dict.items(), key=lambda x: x[1])  # value값 정렬
dict.reverse()
if len(dict) == 10:
    for idx in range(len(dict) - 1, -1, -1):
        if dict[idx][0] in notZero:
            continue
        else:
            # 역순으로 탐색을 시작하여 0이면 안되는 알파벳은 continue로 생략하고 0으로 만들 부분을 맨 마지막으로 빼주기
            dict.append((dict[idx][0], dict[idx][1]))
            dict.remove((dict[idx][0], dict[idx][1]))
            break
result = 0
for idx in range(len(dict)):
    result += dict[idx][1] * (9 - idx)
print(result)
