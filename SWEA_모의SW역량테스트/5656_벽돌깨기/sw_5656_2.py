import sys
sys.stdin = open('sw_5656.txt', 'r')


import copy

def is_inbox(y, x):
    if 0 <= y < H and 0 <= x < W:
        return True
    return False


def find_top(k, cnt, new_map):
    global rem_cnt
    global result
    global total_map

    for y in range(H):
        for x in range(W):
            if (not is_inbox(y - 1, x)) or new_map[y - 1][x] == 0:
                num = new_map[y][x]
                if num != 0:
                    k += 1
                    rem_cnt = 0
                    total_map = copy.deepcopy(new_map)
                    bomb(y, x)
                    move_map()
                    aa = rem_cnt
                    cnt += rem_cnt
                    if cnt > result:
                        result = cnt
                    if k < N:
                        find_top(k, cnt, total_map)
                    cnt -= aa
                    k -= 1


def bomb(y, x):
    global rem_cnt
    global total_map
    rem_cnt += 1
    ran = total_map[y][x] - 1
    total_map[y][x] = 0
    for dif in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yy = y
        xx = x
        for ___ in range(ran):
            yy += dif[0]
            xx += dif[1]
            if is_inbox(yy, xx):
                if total_map[yy][xx] > 0:
                    bomb(yy, xx)

    
def move_map():
    global total_map
    for x in range(W):
        new_y = []
        ccnt = 0
        for y in range(H):
            if total_map[y][x] != 0:
                new_y.append(total_map[y][x])
                ccnt += 1
        for y in range(H-ccnt):
            total_map[y][x] = 0

        kk = 0
        for y in range(H-ccnt, H):
            total_map[y][x] = new_y[kk]
            kk += 1


TC = int(input())
for testcase in range(1, TC+1):
    N, W, H = map(int, input().split())
    ori_map = [list(map(int, input().split())) for _ in range(H)]

    cnt_ori = 0
    for y in range(H):
        for x in range(W):
            if ori_map[y][x] != 0:
                cnt_ori += 1

    result = 0
    rem_cnt = 0
    total_map = []
    find_top(0, 0, ori_map)
    print('#{} {}'.format(testcase, cnt_ori - result))
