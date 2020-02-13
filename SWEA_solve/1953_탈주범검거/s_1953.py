import sys
sys.stdin = open('sw_1953.txt', 'r')

def isInbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True

def solve(sy, sx, t):
    visit = [[0]*M for _ in range(N)]
    visit[sy][sx] = 1
    cnt = 1
    que = {(sy, sx, total_map[sy][sx])}
    for _ in range(t):
        nxt_que = set()
        for y, x, num in que:
            for d in possible_direction[num]:
                dy, dx = dydx[d]
                yy = y + dy
                xx = x + dx
                if isInbox(yy, xx) and not visit[yy][xx] and total_map[yy][xx] > 0:
                    nxt_block = total_map[yy][xx]
                    if possible_pipe[d][nxt_block]:
                        visit[yy][xx] = 1
                        nxt_que.add((yy, xx, nxt_block))
                        cnt += 1
        que = nxt_que
    return cnt

dydx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

possible_pipe = [
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 1]
]

possible_direction = [
    [],
    [0, 1, 2, 3],
    [0, 1],
    [2, 3],
    [0, 3],
    [1, 3],
    [1, 2],
    [0, 2]
]

TC = int(input())
for testcase in range(1, TC+1):
    N, M, R, C, T = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    result = solve(R, C, T-1)
    print('#{} {}'.format(testcase, result))