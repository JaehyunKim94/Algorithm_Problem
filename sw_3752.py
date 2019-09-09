import sys
from itertools import *

sys.stdin = open('s_3752.txt', 'r')


def solve(k, my_sum):
    global cnt
    if k == N:
        if my_sum not in res_lst:
            res_lst.append(my_sum)
            cnt += 1
        return
    else:
        visit[k] = 1
        solve(k+1, my_sum + num_lst[k])
        visit[k] = 0
        solve(k+1, my_sum)


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    res_lst = [0]
    cnt = 1
    for i in range(1, N+1):
        new_lst = list(combinations(num_lst, i))
        for new in new_lst:
            new_sum = sum(new)
            if new_sum not in res_lst:
                cnt += 1
                res_lst.append(new_sum)

    # visit = [0] * N
    # res_lst = []
    # cnt = 0
    # solve(0, 0)
    print('#{} {}'.format(testcase, cnt))