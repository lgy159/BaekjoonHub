answer = 0
for i in range(1, int(input()) + 1):
    answer += str(i).count('3')
    answer += str(i).count('6')
    answer += str(i).count('9')

print(answer)