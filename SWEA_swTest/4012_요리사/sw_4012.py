import sys
sys.stdin = open('sw_4012.txt', 'r')


def get_syn(n, n_lst):
    new_plus = 0
    for x in range(N):
        if x in n_lst:
            new_plus += total_map[n][x]
    return new_plus


def get_com(k):
    global result
    if k == N-1:
        if sum(visit) == N // 2:
            res_a = 0
            res_b = 0
            for i in range(N//2):
                res_a += get_syn(a_lst[i], a_lst)
                res_b += get_syn(b_lst[i], b_lst)
            m_res = abs(res_a - res_b)
            if m_res < result:
                result = m_res

    else:
        k += 1
        if sum(visit) <= N // 2:
            a_lst.append(k)
            visit[k] = 1
            get_com(k)
            a_lst.pop()
            visit[k] = 0
        b_lst.append(k)
        get_com(k)
        b_lst.pop()


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    visit = [0 for _ in range(N)]
    result = 9999999
    a_lst = []
    b_lst = []
    get_com(-1)
    print('#{} {}'.format(testcase, result))