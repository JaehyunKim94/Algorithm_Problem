import sys
sys.stdin = open('17140.txt', 'r')


def r_cal(t_map):
    r_len = len(t_map)
    m_len = 0
    for y in range(r_len):
        tg_lst = t_map[y]
        tg_dict = dict()
        for tg in tg_lst:
            if tg != 0:
                if tg not in tg_dict.keys():
                    tg_dict.update({tg: 1})
                else:
                    tg_dict[tg] += 1

        new_lst = []
        for k, v in tg_dict.items():
            new_lst.append((v, k))
        new_lst.sort()
        t_map[y] = new_lst
        n_len = len(new_lst)
        m_len = max(n_len, m_len)
    for y in range(r_len):
        t_lst = t_map[y]
        idx = 0
        new_lst = [0] * (2*m_len)
        for t in t_lst:
            new_lst[idx] = t[1]
            new_lst[idx+1] = t[0]
            idx += 2
            if idx == 100:
                break
        if len(new_lst)> 100:
            new_lst = new_lst[:100]
        t_map[y] = new_lst
    return t_map


def solve(t_map):
    global result
    r_len = len(t_map)
    c_len = len(t_map[0])
    if r_len >= c_len:
        t_map = r_cal(t_map)
    else:
        t_map = list(map(list, zip(*t_map)))
        t_map = r_cal(t_map)
        t_map = list(map(list, zip(*t_map)))
    return t_map


r, c, k = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(3)]
r -= 1
c -= 1
result = 1000
if r < 3 and c < 3 and total_map[r][c] == k:
    print(0)
else:
    for t in range(1, 101):
        total_map = solve(total_map)
        if r < len(total_map) and c < len(total_map[0]) and total_map[r][c] == k:
            result = t
            break
    if result == 1000:
        result = -1
    print(result)