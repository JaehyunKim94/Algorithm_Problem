import sys
sys.stdin = open('sw_2112.txt', 'r')


def check_map(t_map):
    ck = 0
    if K == 1:
        return True
    for x in range(W):
        cnt = 1
        num = t_map[0][x]
        for y in range(1, D):
            if total_map[y][x] == num:
                cnt += 1
                if cnt == K:
                    ck += 1
                    break
            else:
                cnt = 1
                num = total_map[y][x]
        if x + 1 != ck:
            return False
    return True


def solve(k, t_map, cnt):
    global result

    if k == D-1:
        if check_map(t_map):
            result = min(cnt, result)
        return
    else:
        k += 1
        solve(k, t_map, cnt)
        if cnt < result-1:
            save_lst = t_map[k][:]
            t_map[k] = [0 for _ in range(W)]
            solve(k, t_map, cnt+1)
            t_map[k] = [1 for _ in range(W)]
            solve(k, t_map, cnt+1)
            t_map[k] = save_lst


TC = int(input())
for testcase in range(1, TC+1):
    D, W, K = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(D)]
    result = K
    solve(-1, total_map, 0)
    print('#{} {}'.format(testcase, result))