import sys
sys.stdin = open('sw_5656.txt', 'r')


import copy


def is_inbox(y, x):
    if 0 <= y < H and 0 <= x < W:
        return True
    return False


# 맨 위 블럭 찾기
def find_top(k, new_map):    # k: 찾는 횟수
    for y in range(H):
        for x in range(W):
            if (not is_inbox(y - 1, x)) or new_map[y - 1][x] == 0:
                num = new_map[y][x]
                if num != 0:
                    k += 1
                    total_map = copy.deepcopy(new_map)
                    bomb(y, x)
                    nxt_map = move_map(total_map)
                    if k < N:
                        find_top(k, nxt_map)
                    k -= 1


# 터트리기
def bomb(y, x):
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
                    total_map[yy][xx] = 0
    return total_map


# 밑으로 당기기
def move_map(total_map):
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
    return total_map


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
    cnt = 0
    total_map = copy.deepcopy(ori_map)

    bomb(3, 0)
    for y in range(H):
        print(total_map[y])
    print()
    move_map(total_map)
    for y in range(H):
        print(total_map[y])
    print()
