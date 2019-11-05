import sys
sys.stdin = open('sw_2112.txt', 'r')

def ck_map(t_map):
    ck_cnt = 0
    for y in range(W):
        new_sum = sum(t_map[y][0:K])
        if new_sum in (0, K):
            ck_cnt += 1
            continue
        else:
            p = ck_cnt
            for x in range(K, D):
                new_sum += t_map[y][x] - t_map[y][x-K]
                if new_sum in (0, K):
                    ck_cnt += 1
                    break
            if p == ck_cnt:
                return False
    return True


def solve(t_map, k, cnt):
    global result
    if k == D-1:
        if ck_map(t_map):
            if cnt < result:
                result = cnt
        return

    else:
        k += 1
        solve(t_map, k, cnt)
        if cnt < result-1:
            s_lst = [0 for _ in range(W)]
            for y in range(W):
                s_lst[y] = t_map[y][k]
                t_map[y][k] = 0
            solve(t_map, k, cnt+1)
            for y in range(W):
                t_map[y][k] = 1
            solve(t_map, k, cnt+1)
            for y in range(W):
                t_map[y][k] = s_lst[y]


TC = int(input())
for testcase in range(1, TC+1):
    D, W, K = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(D)]
    ver_map = list(map(list, zip(*total_map[:])))
    if ck_map(ver_map):
        result = 0
    else:
        result = K
        solve(ver_map, -1, 0)
    print('#{} {}'.format(testcase, result))
