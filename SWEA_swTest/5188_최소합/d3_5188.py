import sys
sys.stdin = open('d3_5188.txt', 'r')


def is_inbox(y, x):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


def solve(y, x, res):
    global result
    if y == N-1 and x == N-1:
        if res < result:
            result = res
            return
    else:
        for dif in [(0, 1), (1, 0)]:
            yy = y + dif[0]
            xx = x + dif[1]
            if is_inbox(yy, xx):
                if res + total_map[yy][xx] < result:
                    solve(yy, xx, res+total_map[yy][xx])



TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    result = 30 * N
    solve(0, 0, total_map[0][0])
    print('#{} {}'.format(testcase, result))