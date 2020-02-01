import sys
sys.stdin = open('17135.txt', 'r')

import itertools, copy

def isInbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True

def find_target(y, x, t_map):
    visit = [[0]*M for _ in range(N)]
    que = set()
    que.add((y, x))
    for dis in range(D):
        nxt_que = set()
        for ay, ax in que:
            for dy, dx in [(0, -1), (-1, 0), (0, 1)]:
                yy = ay + dy
                xx = ax + dx
                if isInbox(yy, xx) and visit[yy][xx] == 0:
                    if t_map[yy][xx] == 1:
                        return (yy, xx)
                    visit[yy][xx] = 1
                    nxt_que.add((yy, xx))
        que = nxt_que

def goDown(t_map):
    new_map = [[0] * M for _ in range(N)]
    for y in range(N-1):
        new_map[y+1] = t_map[y][:]
    return new_map

def solve(archer_lst, t_map):
    cnt = 0
    for _ in range(N):
        tg_set = set()
        for archer in archer_lst:
            tg = find_target(N, archer, t_map)
            if tg:
                tg_set.add(tg)
        if tg_set:
            for y, x in tg_set:
                t_map[y][x] = 0
                cnt += 1
        t_map = goDown(t_map)
    return cnt

N, M, D = map(int, input().split())
enemy = list()
e_cnt = 0
total_map = [list(map(int, input().split())) for _ in range(N)]
lst = [i for i in range(M)]
result = 0
for archer_lst in itertools.combinations(lst, 3):
    t_map = copy.deepcopy(total_map)
    res = solve(archer_lst, t_map)
    result = max(result, res)
print(result)