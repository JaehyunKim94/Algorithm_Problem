import sys
sys.stdin = open('sw_5653.txt', 'r')

import copy

# -2: 빈 공간    -1: 죽은 세포

def h_sepo(kk):
    global h_lst
    for y in range(K-kk, K+N+kk):
        for x in range(K-kk, K+M+kk):
            if total_map[y][x] == 0:
                h_lst.add((y, x, ori_map[y][x]))
                total_map[y][x] -= 1
            elif 0 < total_map[y][x]:
                total_map[y][x] -= 1


def bunsik(y, x, kk):
    for dif in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yy = y + dif[y]
        xx = x + dif[x]
        if total_map[yy][xx] == -2:
            total_map[yy][xx] = ori_map[y][x] + kk
            ori_map[yy][xx] = ori_map[y][x]


TC = int(input())
for testcase in range(1, TC+1):
    N, M, K = map(int, input().split())

    H = N + (2*K)
    W = M + (2*K)
    ori_map = [[-2] * W for _ in range(H)]
    cnt = 0

    for y in range(K, K+N):
        new_info = list(map(int, input().split()))
        for i in range(M):
            if new_info[i] != 0:
                cnt += 1
            elif new_info[i] == 0:
                new_info[i] = -2
            ori_map[y][K+i] = new_info[i]
    
    total_map = copy.deepcopy(ori_map)
    h_lst = set()
    for kk in range(K):
        h_sepo(kk)

    