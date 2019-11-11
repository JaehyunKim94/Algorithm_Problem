import sys
sys.stdin = open('17140.txt', 'r')


def r_cal(t_map, r_len, c_len):
    new_map = [0] * r_len
    m_len = 0
    for y in range(r_len):
        tg_lst = t_map[y]
        num = tg_lst[0]
        cnt = 1
        idx = 0
        new_lst = []
        while idx < c_len-1:
            idx += 1
            if tg_lst[idx] == num:
                cnt += 1
            else:
                new_lst.append((cnt, num))
                cnt = 1
                num = tg_lst[idx]
        new_lst.append((cnt, num))
        new_lst.sort()
        new_map[y] = new_lst
        n_len = len(new_lst) * 2
        m_len = max(m_len, n_len)
    for y in range(r_len):
        new_lst = [0] * m_len
        ii = 0
        tg_lst = new_map[y]
        for tg in tg_lst:
            new_lst[ii] = tg[1]
            new_lst[ii+1] = tg[0]
            ii += 2
        new_map[y] = new_lst
    return new_map


def c_cal(t_map, r_len, c_len):
    new_map = [0] * c_len
    m_len = 0
    for x in range(c_len):
        idx = 0
        num = t_map[idx][x]
        cnt = 1
        new_lst = []
        while idx < r_len-1:
            idx += 1
            if t_map[idx][x] == num:
                cnt += 1
            else:
                new_lst.append((cnt, num))
                cnt = 1
                num = t_map[idx][x]
        new_lst.append((cnt, num))
        new_lst.sort()
        new_map[x] = new_lst
    for new in new_map:
        n_len = len(new) * 2
        m_len = max(m_len, n_len)
    for x in range(c_len):
        new_lst = [0] * m_len
        tg_lst = new_map[x]
        ii = 0
        for tg in tg_lst:
            new_lst[ii] = tg[1]
            new_lst[ii+1] = tg[0]
            ii += 2
        new_map[x] = new_lst
    y_map = list(map(list, zip(*new_map)))
    return y_map


def solve():
    global total_map
    r_len = len(total_map)
    c_len = len(total_map[0])
    if r_len >= c_len:
        total_map = r_cal(total_map, r_len, c_len)
    else:
        total_map = c_cal(total_map, r_len, c_len)


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
        if ck_res and total_map[r][c] == k:
            break
    if t == 100:
        t = -1
    print(t)