n = int(input())
graphs = []
for idx in range(n):
    graphs.append([list(input()) for _ in range(5)])


def find(a, b):
    answer = 0
    for i in range(5):
        for j in range(7):
            if a[i][j] != b[i][j]:
                answer += 1
    return answer


result = 1000
a, b = 0, 0
for i in range(n):
    for j in range(i + 1, n):
        temp = find(graphs[i], graphs[j])
        if result > temp:
            result = temp
            a = i
            b = j


print(a + 1, b + 1)