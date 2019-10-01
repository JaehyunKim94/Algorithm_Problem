import sys
sys.stdin = open('d4_7465.txt', 'r')


def solve(k):
    visit[k] = 1
    for x in range(N):
        if rel_map[k][x] == 1 and visit[x]==0:
            solve(x)


TC = int(input())
for testcase in range(1, TC+1):
    N, M = map(int, input().split())
    cnt = 0
    g_lst = []
    rel_map = [[0] * N for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        rel_map[a-1][b-1] = 1
        rel_map[b-1][a-1] = 1

    visit = [0 for _ in range(N)]
    for y in range(N):
        if visit[y] == 0:
            cnt += 1
            solve(y)
    print('#{} {}'.format(testcase, cnt))