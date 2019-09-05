import sys
sys.stdin = open('d3_4615.txt', 'r')

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, 1, -1, 1, -1]

def is_wall(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False

def oth(x, y, p, i):
    px = x + dx[i]
    py = y + dy[i]
    if is_wall(py, px) and total_map[py][px] != 0:
        if total_map[py][px] != p:
            tg_lst.append([py, px])
            oth(px, py, p, i)
        else:
            if len(tg_lst) != 0:
                for tg in tg_lst:
                    total_map[tg[0]][tg[1]] = p
    return

TC = int(input())
for testcase in range(1, TC+1):
    N, M = map(int, input().split())
    total_map = [[0 for _ in range(N)] for __ in range(N)]

    base = N//2
    for i in range(2):
        total_map[base-1+i][base-1+i] = 2
        total_map[base-i][base-1+i] = 1

    for _ in range(M):
        x, y, p = map(int, input().split())
        x -= 1
        y -= 1
        for i in range(8):
            tg_lst = []
            total_map[y][x] = p
            oth(x, y, p, i)

    a_cnt = 0
    b_cnt = 0

    for y in range(N):
        for x in range(N):
            if total_map[y][x] == 2:
                b_cnt += 1
            if total_map[y][x] == 1:
                a_cnt += 1

    print('#{} {} {}'.format(testcase, a_cnt, b_cnt))