import sys
sys.stdin = open('1767.txt', 'r')


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def solve(core_idx, ccnt, dis):
    global total_map
    global result
    if core_idx == core_cnt-1:
        result.add((ccnt, dis))
        return
    else:
        core_idx += 1
        dif = [(0,1), (1, 0), (0, -1), (-1, 0)]
        y, x = core[core_idx]
        for i in range(4):
            ck = True
            dy, dx = dif[i]
            yy, xx = y + dy, x + dx
            change_lst = []
            pp = 0

            while is_inbox(yy, xx):
                if total_map[yy][xx] == 0:
                    total_map[yy][xx] = 3
                    change_lst.append((yy, xx))
                    pp += 1
                else:
                    ck = False
                    break
                yy += dy
                xx += dx

            if ck:
                result.add((ccnt, dis+pp))
                solve(core_idx, ccnt+1, dis+pp)
            for change in change_lst:
                total_map[change[0]][change[1]] = 0
        solve(core_idx, ccnt, dis)


def get_ans(lst):
    core_max = lst[-1][0]
    ret = lst[-1][1]
    for rr in lst:
        if rr[0] == core_max:
            ret = min(ret, rr[1])
    return ret


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [0] * N
    core = []
    core_cnt = 0
    result = set()
    res = 0
    for y in range(N):
        new_info = list(map(int, input().split()))
        total_map[y] = new_info
        for x in range(N):
            if new_info[x] == 1:
                if y in (0, N-1) or x in (0, N-1):
                    res += 1
                else:
                    core.append((y, x))
                    core_cnt += 1
    result.add((res, res))
    solve(-1, res, 0)
    res_lst = sorted(list(result))
    ans = get_ans(res_lst)
    print('#{} {}'.format(testcase, ans))