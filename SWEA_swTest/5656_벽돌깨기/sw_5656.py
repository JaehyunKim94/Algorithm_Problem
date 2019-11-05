import sys
sys.stdin = open('sw_5656.txt', 'r')


def is_inbox(y, x):
    if 0 <= y < H and 0 <= x < W:
        return True
    return False


# 맨 위 블럭 찾기
def find_top(k):    # k: 찾는 횟수
    global cnt
    global result
    for y in range(H):
        for x in range(W):
            if (not is_inbox(y - 1, x)) or total_map[y - 1][x] == 0:
                num = total_map[y][x]
                if num != 0:
                    total_map[y][x] = 0
                    k += 1

                    visit = list()
                    visit.append([y, x])

                    bomb(y, x, num, visit)
                    move_map()
                    new_cnt = len(visit)
                    cnt += new_cnt

                    if cnt > result:
                        result = cnt
                    if k < N:
                        find_top(k)
                    total_map[y][x] = num
                    cnt -= new_cnt
                    k -= 1


# 터트리기
def bomb(y, x, a, visit):
    ran = a - 1
    for dif in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yy = y
        xx = x
        for ___ in range(ran):
            yy += dif[0]
            xx += dif[1]
            if is_inbox(yy, xx) and [yy, xx] not in visit:
                aa = total_map[yy][xx]
                if aa > 0:
                    visit.append([yy, xx])
                    total_map[yy][xx] = 0
                    if aa > 1:
                        bomb(yy, xx, aa, visit)
                    total_map[yy][xx] = aa


# 밑으로 당기기
def move_map():
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
    total_map = [list(map(int, input().split())) for _ in range(H)]

    cnt_ori = 0
    for y in range(H):
        for x in range(W):
            if total_map[y][x] != 0:
                cnt_ori += 1
    result = 0
    cnt = 0
    print(cnt_ori, result)
    find_top(0)
    print(cnt_ori - result)
    print()


