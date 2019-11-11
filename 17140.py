import sys
sys.stdin = open('17140.txt', 'r')
from pprint import pprint


def r_cal(t_map):
    r_len = len(t_map)
    new_map = [0] * r_len
    m_len = 0
    for y in range(r_len):
        cnt_dict = dict()
        tg_lst = t_map[y]
        for tg in tg_lst:
            if tg!=0:
                if tg not in cnt_dict.keys():
                    cnt_dict.update({tg:1})
                else:
                    cnt_dict[tg] += 1
        n_len = len(cnt_dict)
        new_lst = [0] * n_len
        ii = 0
        for k, v in cnt_dict.items():
            new_lst[ii] = [v, k]
            ii += 1
        new_lst.sort()
        new_map[y] = new_lst
        m_len = max(m_len, n_len*2)
    for y in range(r_len):
        new_lst = [0] * m_len
        tg_lst = new_map[y]
        ii = 0
        for tg in tg_lst:
            new_lst[ii] = tg[1]
            new_lst[ii+1] = tg[0]
            ii += 2
            if ii == 100: break
        if ii == 100:
            new_lst = new_lst[:100]
        new_map[y] = new_lst
    return new_map


def solve():
    global total_map
    if len(total_map) >= len(total_map[0]):
        total_map = r_cal(total_map)
    else:
        total_map = list(map(list, zip(*total_map)))
        total_map = r_cal(total_map)
        total_map = list(map(list, zip(*total_map)))


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
            if r <= len(total_map)-1 and c <= len(total_map[0])-1:
                ck_res = True
        if ck_res and total_map[r][c] == k:
            break
    if t == 100:
        t = -1
    print(t)