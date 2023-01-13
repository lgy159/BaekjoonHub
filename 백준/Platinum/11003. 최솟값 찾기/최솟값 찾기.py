from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))
num_list = list(map(int, input().split(' ')))
q = deque()
for idx in range(n):
    while q and q[-1][0] > num_list[idx]:  # num_list[idx]보다 큰거는 전부 pop
        q.pop()
    while q and q[0][1] < idx - k + 1:  # left_idx가 증가함에 따라 윈도우 슬라이딩처럼 해당 부분 popleft
        q.popleft()
    q.append((num_list[idx], idx))
    print(q[0][0], end=' ')
