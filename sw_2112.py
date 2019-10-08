import sys
sys.stdin = open('sw_2112.txt', 'r')
import time

# 1차: 50개 중 38개 (시간 초과)
# 2차: 50개 중 40개 (시간 초과)

import copy


def is_good(t_map):
    cnt = 0
    for x in range(W):
        s_cnt = cnt
        for y in range(D-K+1):
            tg = t_map[y][x]
            ck = True
            for i in range(1, K):
                if tg != t_map[y+i][x]:
                    ck = False
                    break
            if ck:
                cnt += 1
                break
        if s_cnt == cnt:
            return False

    if cnt == W:
        return True
    else:
        return False


def get_com(k, visited):
    if k == D-1:
        tg = sum(visited)
        visit = tuple(visited)
        com_lst[tg].append(visit)

    else:
        k += 1
        get_com(k, visited)
        if sum(visited) < K-1:
            visited[k] = 1
            get_com(k, visited)
            visited[k] = 0


def solve(com, t_map, k):
    global cck
    if k == D-1:
        if is_good(t_map):
            cck = True
            return
    else:
        k += 1
        if com[k] == 1:
            a_map = copy.deepcopy(t_map)
            for x in range(W):
                a_map[k][x] = 1
            solve(com, a_map, k)
            for x in range(W):
                a_map[k][x] = 0
            solve(com, a_map, k)
        else:
            solve(com, t_map, k)


TC = int(input())
for testcase in range(1, TC+1):
    D, W, K = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(D)]
    if is_good(total_map):
        result = 0
    else:
        result = K
        cck = False
        com_lst = [[] for _ in range(K)]
        get_com(-1, [0 for _ in range(D)])
        for jj in range(1, K):
            t_com = com_lst[jj]
            for i in range(len(t_com)):
                com = t_com[i]
                solve(com, total_map, -1)
                if cck:
                    break
            if cck:
                result = sum(com)
                break

    print('#{} {}'.format(testcase, result))