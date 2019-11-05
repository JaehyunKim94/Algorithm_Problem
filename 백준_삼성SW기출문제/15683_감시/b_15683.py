import sys
sys.stdin = open('b_15683.txt', 'r')


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False


def five_on(y, x):
    global cnt
    for dif in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ay = y + dif[0]
        ax = x + dif[1]
        while is_inbox(ay, ax):
            if total_map[ay][ax] == 6:
                break
            elif total_map[ay][ax] == 0:
                total_map[ay][ax] = 8
                cnt -= 1
            ay += dif[0]
            ax += dif[1]


def rem_area(p, dd, rem_lst):
    y = p[0]
    x = p[1]
    dif = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dj in dd:
        diff = dif[dj]
        ay = y + diff[0]
        ax = x + diff[1]
        while is_inbox(ay, ax):
            if total_map[ay][ax] == 6:
                break
            elif total_map[ay][ax] == 0:
                if (ay, ax) not in rem_lst:
                    rem_lst.append((ay, ax))
            ay += diff[0]
            ax += diff[1]


def solve(k, cnt):
    global result
    if k == cam_cnt-1:
        if cnt < result:
            result = cnt
        return

    k += 1
    p = cam_lst[k]
    d = go_lst[total_map[p[0]][p[1]]]

    for dd in d:
        rem_lst = []
        rem_area(p, dd, rem_lst)
        cnt_bbaegi = len(rem_lst)
        for rem_p in rem_lst:
            total_map[rem_p[0]][rem_p[1]] = 8
        solve(k, cnt-cnt_bbaegi)
        for rem_p in rem_lst:
            total_map[rem_p[0]][rem_p[1]] = 0


go_lst = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [0, 3], [1, 2], [1, 3]], [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]]]
N, M = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
cam_lst = []
fiv_lst = []
cnt = 0
cam_cnt = 0
for y in range(N):
    for x in range(M):
        if 0 < total_map[y][x] < 5:
            cam_lst.append((y, x, total_map[y][x]))
            cam_cnt += 1
        elif total_map[y][x] == 5:
            fiv_lst.append((y, x))
        elif total_map[y][x] == 0:
            cnt += 1
result = cnt

if len(fiv_lst) > 0:
    for cam in fiv_lst:
        five_on(cam[0], cam[1])

visit = [0 for _ in range(cam_cnt)]
solve(-1, cnt)
print(result)
