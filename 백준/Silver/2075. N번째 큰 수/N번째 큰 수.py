import heapq
import sys

input = sys.stdin.readline
n = int(input().rstrip())
heap = []
graph = []
for _ in range(n):
    temp = list(map(int, input().rstrip().split()))
    if not heap:
        for data in temp:
            heapq.heappush(heap, data)

    for data in temp:
        if heap[0] < data:
            heapq.heappush(heap, data)
            heapq.heappop(heap)

print(heap[0])
