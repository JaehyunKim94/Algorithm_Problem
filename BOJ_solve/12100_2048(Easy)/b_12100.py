from pprint import pprint
import sys
sys.stdin = open('b_12100.txt', 'r')

import copy


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def find_max(res_map):
    rr = sum(res_map, [])
    return max(rr)


def move_map(t_map, i):
    dif = (1, -1)
    d = dif[i % 2]
    ran = [(0, N-1, 1), (N-1, 0, -1)]
    r = ran[i % 2]
    idx_lst = [(0, N, 1), (N-1, -1, -1)]
    idx = idx_lst[i % 2]
    c_map = copy.deepcopy(t_map)

    if i in (0, 1):
        for x in range(N):
            for y in range(r[0], r[1], r[2]):
                if c_map[y][x] > 0:
                    n_y = y + d
                    while is_inbox(n_y, x):
                        if c_map[n_y][x] != 0:
                            if c_map[n_y][x] == c_map[y][x]:
                                c_map[y][x] *= 2
                                c_map[n_y][x] = 0
                            break
                        n_y += d
            new_lst = [0] * N
            start = idx[0]
            for y in range(idx[0], idx[1], idx[2]):
                if c_map[y][x] > 0:
                    new_lst[start] = c_map[y][x]
                    start += idx[2]
            for y in range(idx[0], idx[1], idx[2]):
                c_map[y][x] = new_lst[y]

    elif i in (2, 3):
        for y in range(N):
            for x in range(r[0], r[1], r[2]):
                if c_map[y][x] > 0:
                    n_x = x + d
                    while is_inbox(y, n_x):
                        if c_map[y][n_x] > 0:
                            if c_map[y][n_x] == c_map[y][x]:
                                c_map[y][x] *= 2
                                c_map[y][n_x] = 0
                            break
                        n_x += d
            new_lst = [0] * N
            start = idx[0]
            for x in range(idx[0], idx[1], idx[2]):
                if c_map[y][x] > 0:
                    new_lst[start] = c_map[y][x]
                    start += idx[2]
            c_map[y] = new_lst

    return c_map


def solve(t_map, k):
    global result
    if k == 0:
        res = find_max(t_map)
        result = max(result, res)

    else:
        k -= 1
        for i in range(4):
            new_map = move_map(t_map, i)
            solve(new_map, k)


N = int(input())
result = 0
origin_map = [list(map(int, input().split())) for _ in range(N)]
solve(origin_map, 5)
print(result)