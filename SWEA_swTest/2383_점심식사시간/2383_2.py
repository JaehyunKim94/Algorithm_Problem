import sys
sys.stdin = open('sw_2383.txt', 'r')


def get_dis(ay, ax, by, bx):
    return abs(ay-by) + abs(ax - bx)


def simul(tlst, s_idx):
    lst = tlst[:]
    r = len(lst)
    st = stair[s_idx][2]
    visit = [0] * r
    s_que = [0] * 3
    time = 0
    while sum(visit) != r:
        time += 1
        for i in range(3):
            if s_que[i] > 0:
                s_que[i] -= 1

        for i in range(r):
            if not visit[i]:
                if lst[i] > 0:
                    lst[i] -= 1
                else:
                    for j in range(3):
                        if s_que[j] == 0:
                            visit[i] = 1
                            s_que[j] = st
                            break
    time += st
    return time


def solve(k, a_lst, b_lst):
    global result
    if k == p_cnt - 1:
        at = simul(a_lst, 0)
        bt = simul(b_lst, 1)
        res = max(at, bt)
        result = min(res, result)
    else:
        k += 1
        solve(k, a_lst + [dis_lst[0][k]], b_lst)
        solve(k, a_lst, b_lst + [dis_lst[1][k]])


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [0]*N
    person = []
    stair = []
    p_cnt = 0
    result = 9999
    for y in range(N):
        new_info = list(map(int, input().split()))
        for x in range(N):
            if new_info[x] == 1:
                p_cnt += 1
                person.append((y, x))
            if new_info[x] > 1:
                stair.append((y, x, new_info[x]))
        total_map[y] = new_info
    dis_lst = []
    for i in range(2):
        new_dis = [get_dis(stair[i][0], stair[i][1], p[0], p[1]) for p in person]
        dis_lst.append(new_dis)
    solve(-1, [], [])
    print('#{} {}'.format(testcase, result))