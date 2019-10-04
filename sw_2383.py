import sys

sys.stdin = open('sw_2383.txt', 'r')


def get_dis(p, s):
    dis = abs(p[0] - s[0]) + abs(p[1] - s[1])
    return dis


def get_time(lst, t):
    ran = len(lst)
    visit = [0 for _ in range(ran)]
    que = [0 for _ in range(3)]
    time = 0
    while sum(visit) != ran:
        # 계단까지 걸어가기
        for kk in range(ran):
            if lst[kk] > 0:
                lst[kk] -= 1

        # 계단 내려가기
        for kk in range(3):
            if que[kk] > 0:
                que[kk] -= 1

        # 입구 도착한 사람 계단 들어가기
        for kk in range(ran):
            if lst[kk] == 0 and visit[kk] == 0:
                for jj in range(3):
                    if que[jj] == 0:
                        visit[kk] = 1
                        que[jj] = t
                        break

        time += 1

    res = time + max(que)
    return res


def solve(k):
    global result
    if k == p_cnt - 1:
        a_lst = []
        b_lst = []
        for ii in range(p_cnt):
            dis = get_dis(p_lst[ii], s_lst[ptos[ii]])
            if ptos[ii] == 0:
                a_lst.append(dis)
            elif ptos[ii] == 1:
                b_lst.append(dis)
        a_lst.sort()        # 1번 계단으로 가는 사람 리스트
        b_lst.sort()        # 2번 계단으로 가는 사람 리스트
        at = s_lst[0][2]    # 1번 계단의 높이
        bt = s_lst[1][2]    # 2번 계단의 높이
        res_a = get_time(a_lst, at)
        res_b = get_time(b_lst, bt)
        if max(res_a, res_b) < result:
            result = max(res_a, res_b)

    else:
        k += 1
        solve(k)
        ptos[k] = 1
        solve(k)
        ptos[k] = 0


TC = int(input())
for testcase in range(1, TC + 1):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    p_lst = []
    p_cnt = 0
    s_lst = []
    for y in range(N):
        for x in range(N):
            if total_map[y][x] == 1:
                p_lst.append((y, x))
                p_cnt += 1
            elif total_map[y][x] > 1:
                s_lst.append((y, x, total_map[y][x]))

    result = 99999999
    ptos = [0 for _ in range(p_cnt)]    # 사람마다의 목적지
    solve(-1)
    print('#{} {}'.format(testcase, result + 1))
