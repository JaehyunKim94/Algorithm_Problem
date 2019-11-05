import sys
sys.stdin = open('sw_1953.txt', 'r')


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False


def solve(que, k):
    global cnt
    rr = len(que)
    if k < L:
        for i in range(rr):
            now = que.pop(0)
            y = now[0]
            x = now[1]
            cnt += 1
            now_num = total_map[y][x]
            way = slct_way[now_num]
            for d in way:
                yy = y + dif[d][0]
                xx = x + dif[d][1]
                if is_inbox(yy, xx):
                    nxt = total_map[yy][xx]
                    if nxt in nxt_pos[d] and visit[yy][xx] == 0:
                        nxt_p = (yy, xx)
                        que.append(nxt_p)
                        visit[yy][xx] = 1

        solve(que, k+1)


slct_way = [(), (0, 1, 2, 3), (0, 1), (2, 3), (0, 3), (1, 3), (1, 2), (0, 2)]
nxt_pos = [(1, 2, 5, 6), (1, 2, 4, 7), (1, 3, 4, 5), (1, 3, 6, 7)]
dif = [(-1, 0), (1, 0), (0, -1), (0, 1)]
TC = int(input())
for testcase in range(1, TC+1):
    N, M, R, C, L = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0 for _ in range(M)] for __ in range(N)]
    cnt = 0
    que = [(R, C)]
    visit[R][C] = 1
    solve(que, 0)
    print('#{} {}'.format(testcase, cnt))