import sys
sys.stdin = open('d3_5189.txt', 'r')


def solve(k, res):
    global result
    if sum(visit) == N:
        res += total_map[k][0]
        if res < result:
            result = res
            return
    else:
        for i in range(N):
            if visit[i] == 0:
                visit[i] = 1
                solve(i, res+total_map[k][i])
                visit[i] = 0


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    visit = [0 for _ in range(N)]
    visit[0] = 1
    result = 999999

    solve(0, 0)
    print('#{} {}'.format(testcase, result))