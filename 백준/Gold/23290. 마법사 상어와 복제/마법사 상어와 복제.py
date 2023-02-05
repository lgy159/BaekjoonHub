import copy
from collections import deque

fish_num, practices = map(int, input().split())
fishes = [[[] for _ in range(4)] for _ in range(4)]
copy_fishes = []
fish_smell = [[0 for _ in range(4)] for _ in range(4)]

direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
shark_dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
for _ in range(fish_num):
    row, col, d = map(int, input().split())
    fishes[row - 1][col - 1].append(d - 1)
shark_x, shark_y = map(int, input().split())
shark_x -= 1
shark_y -= 1


def move_fish():
    temp = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for d in fishes[x][y]:
                nx, ny = x + direction[d][0], y + direction[d][1]
                cnt = 0
                original = d
                while nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or (shark_x == nx and shark_y == ny) or fish_smell[nx][ny]:
                    d -= 1
                    nx, ny = x + direction[d][0], y + direction[d][1]
                    cnt += 1
                    if cnt >= 8:
                        d = original
                        nx, ny = x, y
                        break
                d = d % 8
                temp[nx][ny].append(d)
    return temp


def move_shark(shark_x, shark_y):
    q = deque()
    answer = -1
    visited = [[False for _ in range(4)] for _ in range(4)]
    history_result = ""
    q.append((shark_x, shark_y, 0, visited, ""))
    #print(shark_x, shark_y)
    while q:
        x, y, many, history, result = q.popleft()
        if len(result) >= 3:
            #print(x, y, many, result)
            if many > answer:
                answer = many
                history_result = result
            elif many == answer:
                if history_result > result:
                    history_result = result
            continue
        for idx in range(4):
            nx, ny = x + shark_dir[idx][0], y + shark_dir[idx][1]
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                continue

            if history[nx][ny]:
                q.append((nx, ny, many, copy.deepcopy(history), result + str(idx + 1)))
            else:
                history[nx][ny] = True
                q.append((nx, ny, many + len(fishes[nx][ny]), copy.deepcopy(history), result + str(idx + 1)))
                history[nx][ny] = False
    #print(history_result, shark_x, shark_y, answer)
    for order in history_result:
        nx, ny = shark_x + shark_dir[int(order) - 1][0], shark_y + shark_dir[int(order) - 1][1]
        if fishes[nx][ny]:
            fishes[nx][ny] = []
            fish_smell[nx][ny] = 2
        shark_x, shark_y = nx, ny
    return nx, ny


for _ in range(practices):
    #print("start\n")
    copy_fishes = copy.deepcopy(fishes)
    #print(1, *fishes, sep='\n')
    fishes = move_fish()
    for x in range(4):
        for y in range(4):
            if fish_smell[x][y]:
                fish_smell[x][y] -= 1
    #print(2, *fishes, sep='\n')
    shark_x, shark_y = move_shark(shark_x, shark_y)
    #print(shark_x, shark_y)
    #print(3, *fishes, sep='\n')
    for x in range(4):
        for y in range(4):
            for data in copy_fishes[x][y]:
                fishes[x][y].append(data)
    #print("sharkt", shark_x, shark_y)
    #print(4, *fishes, sep='\n')
    #print()
    #print(*fish_smell, sep='\n')
result = 0
for x in range(4):
    for y in range(4):
        result += len(fishes[x][y])
print(result)