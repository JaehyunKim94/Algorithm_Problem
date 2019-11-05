import sys
sys.stdin = open('b_17142.txt', 'r')


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def go_vir(lst):
    global result
    global vir_lst
    global ck
    tt = 0
    que = lst[:]
    bihwal = []
    new_ck = ck
    for vir in vir_lst:
        if vir not in lst:
            bihwal.append(vir)

    while que:
        term = len(que)
        for _ in range(term):
            s_p = que.pop(0)
            y, x = s_p[0], s_p[1]
            for dif in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                yy = y + dif[0]
                xx = x + dif[1]
                if is_inbox(yy, xx):
                    new_p = (yy, xx)
                    if new_p in bihwal:
                        bihwal.remove(new_p)
                        que.append(new_p)
                    elif total_map[yy][xx] == 0:
                        total_map[yy][xx] = 2
                        que.append(new_p)
                        new_ck -= 1

        tt += 1
        if new_ck == 0:
            result = min(result, tt)
            break

    for bin in bin_lst:
        total_map[bin[0]][bin[1]] = 0
    return


def solve(k, cc, hal_lst):
    if k == vir_cnt-1:
        if cc == M:
            go_vir(hal_lst)

    else:
        k += 1
        if cc < M:
            tg = vir_lst[k]
            hal_lst.append(tg)
            solve(k, cc+1, hal_lst)
            hal_lst.pop()
        solve(k, cc, hal_lst)


N, M = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
vir_lst = []
bin_lst = []
for y in range(N):
    for x in range(N):
        if total_map[y][x] == 2:
            vir_lst.append((y, x))
        elif total_map[y][x] == 0:
            bin_lst.append((y, x))

ck = len(bin_lst)
if ck == 0:
    print(0)

else:
    result = 999999
    vir_cnt = len(vir_lst)
    solve(-1, 0, [])
    if result == 999999:
        print(-1)
    else:
        print(result)