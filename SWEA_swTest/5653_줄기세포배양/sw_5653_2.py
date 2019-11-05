import sys
sys.stdin = open('sw_5653.txt', 'r')


def ck_map(lst):
    for y in range(H):
        print(lst[y])


def sepo(kk):
    global cnt
    bu_lst = set()
    for y in range(K-kk, K+N+kk):
        for x in range(K-kk, K+M+kk):
            if ori_map[y][x] != 0:
                if ori_map[y][x][1] > 0:
                    if ori_map[y][x][1] == e_map[y][x]:
                        bunsik(y, x, bu_lst)
                    ori_map[y][x][1] -= 1
                    if ori_map[y][x][1] == 0:
                        cnt -= 1

                elif ori_map[y][x][0] > 0 and (y, x) not in bu_lst:
                    ori_map[y][x][0] -= 1
                    if ori_map[y][x][0] == 0:
                        ori_map[y][x][1] = e_map[y][x]


def bunsik(y, x, bu_lst):
    global cnt
    for dif in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yy = y + dif[0]
        xx = x + dif[1]
        if (yy, xx) in bu_lst:
            if e_map[y][x] > e_map[yy][xx]:
                e_map[yy][xx] = e_map[y][x]
                ori_map[yy][xx][0] = e_map[y][x]

        if ori_map[yy][xx] == 0:
            ori_map[yy][xx] = [e_map[y][x], 0]
            e_map[yy][xx] = e_map[y][x]
            bu_lst.add((yy, xx))
            cnt += 1


TC = int(input())
for testcase in range(1, TC+1):
    N, M, K = map(int, input().split())

    H = N + (2*K)
    W = M + (2*K)
    ori_map = [[0] * W for _ in range(H)]
    e_map = [[0] * W for _ in range(H)]
    cnt = 0
    for y in range(K, K+N):
        new_info = list(map(int, input().split()))
        for i in range(M):
            if new_info[i] != 0:
                ori_map[y][K + i] = [new_info[i], 0]
                cnt += 1
            e_map[y][K+i] = new_info[i]

    for kk in range(K):
        sepo(kk)

    print('#{} {}'.format(testcase, cnt))