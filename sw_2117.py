import sys
sys.stdin = open('sw_2117.txt', 'r')


def get_cost(n):
    res = n**2 + (n-1)**2
    return res


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def solve(y, x, i):
    global cnt
    if (y, x) in home_lst:
        if (y, x) not in que:
            que.append((y, x))
            cnt += 1

    if i > 0:
        for d in dif:
            yy = y + d[0]
            xx = x + d[1]
            if is_inbox(yy, xx):
                solve(yy, xx, i-1)



dif = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cost_lst = [get_cost(i) for i in range(21)]
TC = int(input())
for testcase in range(1, TC+1):
    N, M = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    home_lst = []
    h_cnt = 0
    for y in range(N):
        for x in range(N):
            if total_map[y][x] == 1:
                home_lst.append((y, x))
                h_cnt += 1
    result = 0
    if h_cnt*M > cost_lst[N]:
        result = h_cnt
    else:
        for cost in cost_lst:
            if h_cnt*M < cost:
                m_in = cost_lst.index(cost)
                break


        print('#{} {}'.format(testcase, m_in))
