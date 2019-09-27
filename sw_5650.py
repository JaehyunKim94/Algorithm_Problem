import sys
sys.stdin = open('sw_5650.txt', 'r')

dif = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def finish(cnt):
    global ck
    ck = False
    cnt = cnt*2 + 1
    return cnt


def move_p(y, x, block, i):
    global ck
    global cnt
    if block in range(1, 5):
        if block == 1:
            if i == 0 or i == 3:
                cnt = finish(cnt)
                return
            elif i == 1:
                cnt += 1
                i = 3
            elif i == 2:
                cnt += 1
                i = 0
            solve(y, x, i)

        elif block == 2:
            if i == 1 or i == 3:
                cnt = finish(cnt)
                return
            elif i == 0:
                cnt += 1
                i = 3
            elif i == 2:
                cnt += 1
                i = 1
            solve(y, x, i)

        elif block == 3:
            if i == 1 or i == 2:
                cnt = finish(cnt)
                return
            elif i == 0:
                cnt += 1
                i = 2
            elif i == 3:
                cnt += 1
                i = 1
            solve(y, x, i)

        elif block == 4:
            if i == 0 or i == 2:
                cnt = finish(cnt)
                return
            elif i == 1:
                cnt += 1
                i = 2
            elif i == 3:
                cnt += 1
                i = 0
            solve(y, x, i)

    elif block in range(6, 11):
        for k in range(2):
            p = block_lst[block][k]
            if p != (y, x):
                y, x = p[0], p[1]
                solve(y, x, i)

    elif block == 11:
        ck = False
        return


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True


def solve(y, x, i):
    global cnt
    global ck
    yy = y + dif[i][0]
    xx = x + dif[i][1]

    if ck:
        if is_inbox(yy, xx):
            block = total_map[yy][xx]
            if block == 0:
                solve(yy, xx, i)
            elif block == 5:
                cnt = cnt*2 + 1
                ck = False
                return
            else:
                move_p(yy, xx, block, i)

        else:
            cnt = finish(cnt)
            ck = False
            return


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    st_lst = []
    block_lst = [[] for _ in range(12)]
    for y in range(N):
        for x in range(N):
            tg = total_map[y][x]
            if tg == -1:
                block_lst[11].append((y, x))
            else:
                block_lst[tg].append((y, x))

    result = 0
    for st in block_lst[0]:
        for i in range(4):
            ck = True
            cnt = 0
            solve(st[0], st[1], i)
            if cnt > result:
                result = cnt

    print('#{} {}'.format(testcase, result))
