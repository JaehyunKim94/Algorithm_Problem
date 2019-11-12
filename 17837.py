import sys
sys.stdin = open('17837.txt' ,'r')
from pprint import pprint


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def change_dir(d):
    if d in (0, 1):
        d = 1 - d
    else:
        d = 5 - d
    return d


def check_res(t_map):
    for y in range(N):
        for x in range(N):
            if t_map[y][x] != 0 and len(t_map[y][x]) >= 4:
                return True
    return False


def go_chess(chess_info, yy, xx):
    global total_map
    global chess_map
    global horse_pos
    upchess = []
    for j in range(len(chess_info)):
        if chess_info[j] == i:
            upchess = chess_info[j:]
            total_map[y][x] = chess_info[:j]
            if len(total_map[y][x]) == 0:
                total_map[y][x] = 0
            break

    for h in upchess:
        horse_pos[h] = (yy, xx)

    if chess_map[yy][xx] == 1:
        upchess.reverse()

    if total_map[yy][xx] != 0:
        total_map[yy][xx] += upchess
    else:
        total_map[yy][xx] = upchess


N, K = map(int, input().split())
# 0: 흰색  1: 빨간색  #2: 파란색
chess_map = [list(map(int, input().split())) for _ in range(N)]
total_map = [[0] * N for _ in range(N)]
dir_dic = dict()
horse_pos = [0] * K
for kk in range(K):
    y, x, d = map(int, input().split())
    y -= 1
    x -= 1
    d -= 1
    total_map[y][x] = [kk]
    dir_dic.update({kk: d})
    horse_pos[kk] = (y, x)
result = 10000
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
for t in range(1, 1001):
    for i in range(K):
        horse = horse_pos[i]
        y, x = horse[0], horse[1]
        d = dir_dic[i]
        dy, dx = direction[d]
        chess_info = total_map[y][x]
        yy = y + dy
        xx = x + dx
        if is_inbox(yy, xx):
            if chess_map[yy][xx] == 2:
                d = change_dir(d)
                dir_dic[i] = d
                n_y, n_x = y + direction[d][0], x + direction[d][1]
                if is_inbox(n_y, n_x) and total_map[n_y][n_x] != 2:
                    go_chess(chess_info, n_y, n_x)
                elif not is_inbox(n_y, n_x) or(is_inbox(n_y, n_x) and total_map[n_y][n_x] == 2):
                    continue

            else:
                go_chess(chess_info, yy, xx)
        else:
            d = change_dir(d)
            dir_dic[i] = d
            n_y, n_x = y + direction[d][0], x + direction[d][1]
            if total_map[n_y][n_x] != 2:
                go_chess(chess_info, n_y, n_x)
    pprint(total_map)
    if check_res(total_map):
        result = t
        break

if result == 10000:
    result = -1

print(result)



