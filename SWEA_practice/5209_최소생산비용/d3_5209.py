import sys
sys.stdin = open('d3_5209.txt', 'r')


def solve(k, v):
    global result
    if k == N-1:
        result = v

    else:
        k += 1
        for i in range(N):
            if visit[i] == 0:
                nxt = v + total_map[k][i]
                if nxt < result:
                    visit[i] = 1
                    solve(k, nxt)
                    visit[i] = 0

TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    result = 99999999
    solve(-1, 0)
    print('#{} {}'.format(testcase, result))