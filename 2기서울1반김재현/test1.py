def tg_ud(cnt):
    rr = cnt//div
    lc = rr * div
    rc = (rr+1) * div
    if cnt-lc <= rc - cnt:
        return rr
    else:
        return rr+1


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def solve(y, x, dif):
    yy = y + dif[0]
    xx = x + dif[1]
    if is_inbox(yy, xx):
        cnt_lst.append(total_map[yy][xx])
        solve(yy, xx, dif)


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    div = N*2-1
    cost = 999999
    height = 100

    for y in range(N):
        for x in range(N):
            cnt_lst = [total_map[y][x]]
            for dif in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                solve(y, x, dif)
            dari_tg = tg_ud(sum(cnt_lst))

            cnt = 0
            for i in range(div):
                    cnt += abs(dari_tg - cnt_lst[i])

            if cnt == cost and dari_tg < height:
                height = dari_tg
            if cnt < cost:
                cost = cnt
                height = dari_tg


    print('#{} {} {}'.format(testcase, cost, height))