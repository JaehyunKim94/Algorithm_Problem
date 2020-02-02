import sys
sys.stdin = open('b_12100.txt', 'r')

def left(t_map):
    tmp_map = [[0] * N for _ in range(N)]
    for y in range(N):
        idx = 0
        for x in range(N):
            if t_map[y][x] != 0:
                tmp_map[y][idx] = t_map[y][x]
                idx += 1
    for y in range(N):
        for x in range(N-1):
            if tmp_map[y][x] == tmp_map[y][x+1]:
                tmp_map[y][x] *= 2
                tmp_map[y][x+1] = 0
    for y in range(N):
        idx = 0
        new_info = [0] * N
        for x in range(N):
            if tmp_map[y][x] != 0:
                new_info[idx] = tmp_map[y][x]
                idx += 1
        tmp_map[y] = new_info
    return tmp_map

def right(t_map):
    tt_map = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            tt_map[y][x] = t_map[y][N-1-x]
    tt_map = left(tt_map)
    tmp_map = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            tmp_map[y][x] = tt_map[y][N-1-x]
    return tmp_map

def up(t_map):
    tmp_map = [[0] * N for _ in range(N)]
    for x in range(N):
        idx = 0
        for y in range(N):
            if t_map[y][x] != 0:
                tmp_map[idx][x] = t_map[y][x]
                idx += 1
    for x in range(N):
        for y in range(N-1):
            if tmp_map[y][x] == tmp_map[y+1][x]:
                tmp_map[y][x] *= 2
                tmp_map[y+1][x] = 0
    res_map = [[0]*N for _ in range(N)]
    for x in range(N):
        idx = 0
        for y in range(N):
            if tmp_map[y][x] != 0:
                res_map[idx][x] = tmp_map[y][x]
                idx += 1
    return res_map

def down(t_map):
    tmp_map = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            tmp_map[y][x] = t_map[N-1-y][x]
    tmp_map = up(tmp_map)
    res_map = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            res_map[y][x] = tmp_map[N-1-y][x]
    return res_map


def solve(t_map, depth):
    global result
    if depth == 5:
        res = max(sum(t_map, []))
        result = max(res, result)
    else:
        depth += 1
        solve(left(t_map), depth)
        solve(right(t_map), depth)
        solve(up(t_map), depth)
        solve(down(t_map), depth)


N = int(input())
total_map = [list(map(int, input().split())) for _ in range(N)]
result = 0
solve(total_map, 0)
print(result)