import sys
sys.stdin = open('b_17406.txt', 'r')

import copy

def getResult(t_map):
    res = 999999
    for y in range(N):
        res = min(sum(t_map[y]), res)
    return res

def isInbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True

def isTarget(y, x, r, c, s):
    if r-s <= y <= r+s and c-s <= x <= c+s:
        return True

def getVisit(r, c, s):
    tmp = [[0] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if not isTarget(y, x, r, c, s):
                tmp[y][x] = 1
    return tmp

def solve(t_map):
    global result
    if sum(command_visit) == K:
        result = min(result, getResult(t_map))
    else:
        for idx in range(K):
            if command_visit[idx] == 0:
                r, c, s = rotate_info[idx]
                tmp_map = rotate(t_map, r-1, c-1, s)
                command_visit[idx] = 1
                solve(tmp_map)
                command_visit[idx] = 0

def rotate(t_map, r, c, s):
    dydx = [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]
    tmp_map = copy.deepcopy(t_map)
    visit = getVisit(r, c, s)
    for ii in range(s, 0, -1):
        idx = 0
        sy, sx = r-ii, c-ii
        s_num = tmp_map[sy][sx]
        ny, nx = sy + 1, sx
        while idx < 4:
            tmp_map[sy][sx] = tmp_map[ny][nx]
            visit[sy][sx] = 1
            sy, sx = ny, nx
            ay, ax = ny + dydx[idx][0], nx + dydx[idx][1]
            if not isInbox(ay, ax) or visit[ay][ax] == 1:
                idx += 1
                ay, ax = ny + dydx[idx][0], nx + dydx[idx][1]
            ny, nx = ay, ax
        tmp_map[r-ii][c-ii+1] = s_num
        visit[r-ii][c-ii+1] = 1
    return tmp_map

N, M, K = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
rotate_info = [list(map(int, input().split())) for _ in range(K)]
command_visit = [0] * K
result = 999999
solve(total_map)
print(result)