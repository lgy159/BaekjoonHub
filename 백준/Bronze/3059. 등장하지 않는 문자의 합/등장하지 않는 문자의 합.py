from string import ascii_lowercase, ascii_uppercase

for _ in range(int(input())):
    s = input()
    alphabet_list = list(ascii_uppercase)
    answer = 0
    for alpha in alphabet_list:
        if not alpha in s:
            answer += ord(alpha)
    print(answer)