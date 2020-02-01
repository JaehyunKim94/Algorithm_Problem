import sys
sys.stdin = open('sw_2117.txt', 'r')


def get_cost(n):
    res = n**2 + (n-1)**2
    return res


def get_dis(a, b):
    dis = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return dis


def solve(p):
    global result
    dis_lst = [get_dis(p, home_lst[i]) for i in range(h_cnt)]
    my_lst = [0 for _ in range(2*N)]
    for j in range(2*N):
        for dis in dis_lst:
            if j >= dis:
                my_lst[j] += 1
    for j in range(2*N):
        if my_lst[j] * M < cost_lst[j+1]:
            my_lst[j] = 0
    if max(my_lst) > result:
        result = max(my_lst)


cost_lst = [get_cost(i) for i in range(41)]
cost_lst[0] = 0

TC = int(input())
for testcase in range(1, TC+1):
    N, M = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    home_lst = []
    h_cnt = 0
    l = N * 2
    for y in range(N):
        for x in range(N):
            if total_map[y][x] == 1:
                home_lst.append((y, x))
                h_cnt += 1
    result = 0

    for y in range(l):
        for x in range(l):
            p = (y, x)
            solve(p)
    print('#{} {}'.format(testcase, result))