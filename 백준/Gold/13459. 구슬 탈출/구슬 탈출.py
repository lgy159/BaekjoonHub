import sys
from collections import deque

row, col = map(int, input().split())
graph = [list(map(str, input())) for _ in range(row)]


def move_up(x, y, color):
    while 1:
        if graph[x - 1][y] == 'O':
            if color == 0:
                x, y = -2, -2
            else:
                x, y = -1, -1
            break
        elif graph[x - 1][y] != '#':
            x, y = x - 1, y
        else:
            break
    return x, y


def move_down(x, y, color):
    while 1:
        if graph[x + 1][y] == 'O':
            if color == 0:
                x, y = -2, -2
            else:
                x, y = -1, -1
            break
        elif graph[x + 1][y] != '#':
            x, y = x + 1, y
        else:
            break
    return x, y


def move_left(x, y, color):
    while 1:
        if graph[x][y - 1] == 'O':
            if color == 0:
                x, y = -2, -2
            else:
                x, y = -1, -1
            break
        elif graph[x][y - 1] != '#':
            x, y = x, y - 1
        else:
            break
    return x, y


def move_right(x, y, color):
    while 1:
        if graph[x][y + 1] == 'O':
            if color == 0:
                x, y = -2, -2
            else:
                x, y = -1, -1
            break
        if graph[x][y + 1] != '#':
            x, y = x, y + 1
        else:
            break
    return x, y


def solve(type, rx, ry, bx, by):
    if type == 0:  # up
        if rx > bx:
            rx, ry = move_up(rx, ry, 0)
            bx, by = move_up(bx, by, 1)
            if rx == bx and ry == by:
                rx += 1
        else:
            bx, by = move_up(bx, by, 1)
            rx, ry = move_up(rx, ry, 0)
            if rx == bx and ry == by:
                bx += 1
    elif type == 1:  # down
        if rx > bx:
            bx, by = move_down(bx, by, 1)
            rx, ry = move_down(rx, ry, 0)
            if rx == bx and ry == by:
                bx -= 1
        else:
            rx, ry = move_down(rx, ry, 0)
            bx, by = move_down(bx, by, 1)
            if rx == bx and ry == by:
                rx -= 1
    elif type == 2:  # left
        if ry > by:
            rx, ry = move_left(rx, ry, 0)
            bx, by = move_left(bx, by, 1)
            if rx == bx and ry == by:
                ry += 1
        else:
            bx, by = move_left(bx, by, 1)
            rx, ry = move_left(rx, ry, 0)
            if rx == bx and ry == by:
                by += 1
    elif type == 3:  # right
        if ry > by:
            bx, by = move_right(bx, by, 1)
            rx, ry = move_right(rx, ry, 0)
            if rx == bx and ry == by:
                by -= 1
        else:
            rx, ry = move_right(rx, ry, 0)
            bx, by = move_right(bx, by, 1)
            if rx == bx and ry == by:
                ry -= 1

    return rx, ry, bx, by


q = deque()
rx = ry = bx = by = 0
ox, oy = 0, 0
for r in range(row):
    for c in range(col):
        if graph[r][c] == 'B':
            bx, by = r, c
        if graph[r][c] == 'R':
            rx, ry = r, c
        if graph[r][c] == 'O':
            ox, oy = r, c
q.append((rx, ry, bx, by, -1, 0))
visited = [[[[False for _ in range(col)] for _ in range(row)] for _ in range(col)] for _ in range(row)]
visited[rx][ry][bx][by] = True
while q:
    rx, ry, bx, by, order, cnt = q.popleft()
    #print(rx, ry, bx, by, cnt)
    for dir in range(4):
        new_rx, new_ry, new_bx, new_by = solve(dir, rx, ry, bx, by)
        if dir == order:
            continue
        if new_rx == -2 and new_ry == -2 and new_bx == -1 and new_by == -1:
            continue
        if (not (new_rx == -2 and new_ry == -2)) and new_bx == -1 and new_by == -1:
            continue
        if cnt >= 10:
            continue
        if new_rx == -2 and new_ry == -2:
            if cnt + 1 <= 10:
                print(1)
            else:
                print(0)
            sys.exit(0)

        if not visited[new_rx][new_ry][new_bx][new_by]:
            q.append((new_rx, new_ry, new_bx, new_by, dir, cnt + 1))
            visited[new_rx][new_ry][new_bx][new_by] = True
print(0)