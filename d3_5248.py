import sys
sys.stdin = open('d3_5248.txt', 'r')


def solve(k):
    for i in range(1, N+1):
        if total_map[k][i] == 1:
            if visit[i] == 0:
                visit[i] = 1
                solve(i)


TC= int(input())
for testcase in range(1, TC+1):
    N, M = map(int, input().split())
    new_lst = list(map(int, input().split()))
    total_map = [[0]*(N+1) for _ in range(N+1)]
    visit = [0] * (N+1)
    result = 0
    for i in range(0, M*2, 2):
        total_map[new_lst[i]][new_lst[i+1]] = 1
        total_map[new_lst[i+1]][new_lst[i]] = 1
    for i in range(1, N+1):
        if visit[i] == 0:
            visit[i] = 1
            solve(i)
            result += 1
    print('#{} {}'.format(testcase, result))

