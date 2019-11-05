def is_inbox(y, x):
    if 0 <= y < 10 and 0 <= x < 10:
        return True


def update_dic(y, x, b):
    if (y, x) not in bat_dic.keys():
        bat_dic.update({(y, x): {b}})
    else:
        bat_dic[(y, x)].add(b)


mov = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]


def p_move(p, s):
    new_p = (p[0] + mov[s][0], p[1] + mov[s][1])
    return new_p


def get_area(y, x, r, b):
    update_dic(y, x, b)
    if r > 0:
        for dif in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            yy = y + dif[0]
            xx = x + dif[1]
            if is_inbox(yy, xx):
                get_area(yy, xx, r - 1, b)


def charge_bat(ap, bp):
    global result
    ra, rb = 0, 0
    arr_a = []
    arr_b = []
    if ap in bat_dic.keys():
        arr_a = [(p_lst[kk], kk) for kk in bat_dic[ap]]
        arr_a.sort(key=lambda el: el[0], reverse=True)
        ra = len(arr_a)
    if bp in bat_dic.keys():
        arr_b = [(p_lst[kk], kk) for kk in bat_dic[bp]]
        arr_b.sort(key=lambda el: el[0], reverse=True)
        rb = len(arr_b)

    if ra > 0 and rb > 0:
        visit = [0] * (A + 1)
        res = 0
        for ii in range(ra):
            new_num = arr_a[ii][0]
            visit[arr_a[ii][1]] = 1
            for jj in range(rb):
                if visit[arr_b[jj][1]] == 0:
                    new_num += arr_b[jj][0]
                    if new_num > res:
                        res = new_num
                    new_num -= arr_b[jj][0]
                else:
                    if new_num > res:
                        res = new_num
            visit[arr_a[ii][1]] = 0
        result += res

    else:
        if ra > 0:
            result += arr_a[0][0]
        if rb > 0:
            result += arr_b[0][0]


TC = int(input())
for testcase in range(1, TC + 1):
    M, A = map(int, input().split())
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))

    bat_dic = dict()
    num = 1
    p_lst = [0 for _ in range(A + 1)]
    for _ in range(A):
        new_lst = list(map(int, input().split()))
        x = new_lst[0] - 1  # x좌표
        y = new_lst[1] - 1  # y좌표
        r = new_lst[2]  # 범위
        p_lst[num] = new_lst[3]  # 충전량
        get_area(y, x, r, num)
        num += 1

    ck_lst = bat_dic.keys()
    ap = (0, 0)
    bp = (9, 9)
    result = 0
    for i in range(M + 1):
        if ap in ck_lst or bp in ck_lst:
            charge_bat(ap, bp)
        if i < M:
            ap = p_move(ap, a_lst[i])
            bp = p_move(bp, b_lst[i])

    print('#{} {}'.format(testcase, result))