import sys
sys.stdin = open('5648.txt', 'r')


def is_inbox(x, y):
    if -1000 <= y <= 1000 and -1000 <= x <= 1000:
        return True
    return False


def solve(atom_lst):
    dif = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]
    energy = 0
    while atom_lst:
        a_dic = dict()
        d_lst = set()
        for atom in atom_lst:
            x, y, d, e = atom[0], atom[1], atom[2], atom[3]
            dx, dy = dif[d]
            x = x + dx
            y = y + dy
            if is_inbox(x, y):
                if (x, y) in a_dic.keys():
                    if (x, y) in d_lst:
                        energy += e
                    else:
                        energy += e
                        energy += a_dic[(x, y)][1]
                        d_lst.add((x, y))

                else:
                    a_dic.update({(x, y): (d, e)})

        for p in d_lst:
            a_dic.pop(p)

        new_atom = []
        for k, v in a_dic.items():
            new_el = [k[0], k[1], v[0], v[1]]
            new_atom.append(new_el)
        atom_lst = new_atom
    return energy


# x좌표, y좌표, 방향, 보유에너지
TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    atom_lst = [list(map(int, input().split())) for _ in range(N)]
    result = solve(atom_lst)
    print('#{} {}'.format(testcase, result))