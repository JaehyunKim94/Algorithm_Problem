import sys
sys.stdin = open('17143.txt', 'r')


def is_inbox(y, x):
    if 0 <= y < R and 0 <= x < C:
        return True
    return False


def move_shark(t_map):
    dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    new_map = [[0]*C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if t_map[y][x] != 0:
                shark = t_map[y][x]
                yy, xx = y, x
                for t in range(shark[0]):
                    n_y = yy + dir[shark[1]][0]
                    n_x = xx + dir[shark[1]][1]
                    if not is_inbox(n_y, n_x):
                        if shark[1] in (0, 1):
                            shark[1] = 1 - shark[1]
                        else:
                            shark[1] = 5 - shark[1]
                        n_y = yy + dir[shark[1]][0]
                        n_x = xx + dir[shark[1]][1]
                    yy, xx = n_y, n_x
                if new_map[yy][xx] == 0:
                    new_map[yy][xx] = shark
                else:
                    if shark[2] > new_map[yy][xx][2]:
                        new_map[yy][xx] = shark
    return new_map


R, C, M = map(int, input().split())
total_map = [[0]*C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1
    total_map[r][c] = [s, d, z]

result = 0
for x in range(C):
    # 상어잡기
    for y in range(R):
        if total_map[y][x] != 0:
            result += total_map[y][x][2]
            total_map[y][x] = 0
            break
    total_map = move_shark(total_map)
print(result)