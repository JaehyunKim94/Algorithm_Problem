from pprint import pprint
import sys
sys.stdin = open('d5_5521.txt', 'r')


def solve(k_lst, d):
    new_lst = []
    for k in k_lst:
        for i in range(1, N+1):
            if total_map[k][i] == 1:
                if visit[i] == 0:
                    visit[i] = 1
                    new_lst.append(i)
    if d < 1:
        solve(new_lst, d+1)


TC = int(input())
for testcase in range(1, TC+1):
    N, M = map(int, input().split())
    total_map = [[0 for _ in range(N+1)] for __ in range(N+1)]
    visit = [0 for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        total_map[a][b] = 1
        total_map[b][a] = 1
    solve([1], 0)

    print('#{} {}'.format(testcase, sum(visit)))