import sys
sys.stdin = open('17140.txt', 'r')

def rotate(t_map):
    y_len = len(t_map)
    x_len = len(t_map[0])
    new_map = [[0] * y_len for _ in range(x_len)]
    for y in range(x_len):
        for x in range(y_len):
            new_map[y][x] = t_map[x][y]
    return new_map


def go_count():
    global total_map
    ran = len(total_map)
    lim = len(total_map[0])
    new_map = [0] * ran
    max_len = 0
    for y in range(ran):
        tg = total_map[y]
        idx = 1
        num = tg[0]
        cnt = 1
        new_lst = []
        while idx < lim:
            if num == tg[idx]:
                cnt += 1
            else:
                new_lst.append((cnt, num))
                num = tg[idx]
                cnt = 1
            idx += 1
        new_lst.append((cnt, num))
        new_lst.sort()
        n_len = len(new_lst) * 2
        max_len = max(n_len, max_len)
        new_map[y] = new_lst

    for i in range(ran):
        new_in = [0] * max_len
        new_tg = new_map[i]
        ii = 0
        for tg in new_tg:
            new_in[ii] = tg[1]
            new_in[ii+1] = tg[0]
            ii += 2
        new_map[i] = new_in
    total_map = new_map


def solve():
    global total_map
    r_len = len(total_map)
    c_len = len(total_map[0])
    if r_len >= c_len:
        go_count()
    else:
        total_map = rotate(total_map)
        go_count()
        total_map = rotate(total_map)


r, c, k = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(3)]
r -= 1
c -= 1
if r < 3 and c < 3 and total_map[r][c] == k:
    print(0)
else:
    ck_res = False
    for t in range(1, 101):
        solve()
        if not ck_res:
            if r < len(total_map) and c < len(total_map[0]):
                ck_res = True
        if ck_res:
            if total_map[r][c] == k:
                break
    print(t)