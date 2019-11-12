import sys
sys.stdin = open('5643.txt', 'r')
from pprint import pprint


def solve(g, f, t):
    for k in range(N):
        if g[t][k] == 1 and k != f:
            g[f][k] = 1
            if g[f][k] == 0:
                solve(g, f, k)

TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    ag = [[0] * N for _ in range(N)]
    bg = [[0] * N for _ in range(N)]
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        ag[b][a] = 1
        bg[a][b] = 1

    for i in range(N):
        for j in range(N):
            if ag[i][j] == 1:
                solve(ag, i, j)
            if bg[i][j] == 1:
                solve(bg, i, j)
    result = 0
    for i in range(N):
        if sum(ag[i]) + sum(bg[i]) == N-1:
            result += 1
    print('#{} {}'.format(testcase, result))
