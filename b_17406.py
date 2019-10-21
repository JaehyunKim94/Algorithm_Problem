import sys
from pprint import pprint
sys.stdin = open('b_17406.txt', 'r')


import copy


def is_visit(y, x, new_visit):
    if 0 <= y < N and 0 <= x < M:
        if new_visit[y][x] == 1:
            return True
    return False


def rotate(tt_map, order):
    re_map = copy.deepcopy(tt_map)
    r, c, s = order[0]-1, order[1]-1, order[2]
    for j in range(s, 0, -1):
        s_x = c - j
        s_y = r - j
        s_v = re_map[s_y][s_x]
        y, x = s_y, s_x
        line = (r-j, r+j, c-j, c+j)
        d = 0
        dif = ((1, 0), (0, 1), (-1, 0), (0, -1))
        new_visit = [[0] * M for _ in range(N)]
        while True:
            yy = y
            xx = x
            y += dif[d][0]
            x += dif[d][1]
            if y == s_y and x == s_x:
                break

            if y < line[0] or y > line[1] or x < line[2] or x > line[3] or is_visit(y, x, new_visit):
                y, x = yy, xx
                d = (d+1) % 4
                y += dif[d][0]
                x += dif[d][1]
            re_map[yy][xx] = re_map[y][x]
            new_visit[y][x] = 1
        re_map[s_y][s_x+1] = s_v

    return re_map


def solve(k, t_map):
    global result
    if k == K:
        if sum(visit) == K:
            for y in range(N):
                ck = sum(t_map[y])
                if ck < result:
                    result = ck
        return
    else:
        k += 1
        for i in range(K):
            if visit[i] == 0:
                visit[i] = 1
                new_map = rotate(t_map, order_lst[i])
                solve(k, new_map)
                visit[i] = 0


N, M, K = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
order_lst = [list(map(int, input().split())) for _ in range(K)]
visit = [0] * K
result = 9999999
solve(0, total_map)
print(result)