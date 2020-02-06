import sys
sys.stdin = open('5648.txt', 'r')

def solve():
    global atom_dict
    dydx = [(0.5, 0), (-0.5, 0), (0, -0.5), (0, 0.5)]
    res = 0
    while atom_dict:
        nxt_dict = dict()
        col_set = set()
        pos_set = set()
        for k, v in atom_dict.items():
            y, x = k[0], k[1]
            d, e = atom_info[v]
            dy, dx = dydx[d]
            yy = y + dy
            xx = x + dx
            if abs(yy) <= 1000 and abs(xx) <= 1000:
                if (yy, xx) in nxt_dict.keys():
                    a = nxt_dict.get((yy, xx))
                    col_set.add(a)
                    col_set.add(v)
                    pos_set.add((yy, xx))
                else:
                    nxt_dict.update({(yy, xx): v})
        for idx in col_set:
            res += atom_info[idx][1]
        for pos in pos_set:
            nxt_dict.pop(pos)
        atom_dict = nxt_dict
    return res

TC = int(input())
for testcase in range(1, TC+1):
    atom_cnt = int(input())
    atom_dict = dict()
    atom_info = [0] * atom_cnt
    for i in range(atom_cnt):
        x, y, d, e = map(int, input().split())
        atom_dict[(y, x)] = i
        atom_info[i] = (d, e)
    result = solve()
    print('#{} {}'.format(testcase, result))