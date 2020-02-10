import sys
sys.stdin = open('sw_2112.txt', 'r')

def isGood(t_map):
    for x in range(M):
        ck = [t_map[0][x], 1]
        flag = True
        for y in range(1, N):
            if t_map[y][x] == ck[0]:
                ck[1] += 1
            else:
                ck = [t_map[y][x], 1]
            if ck[1] >= K:
                flag = False
                break
        if flag:
            return False
    return True


def solve(idx, cnt, max_cnt, t_map):
    global result
    if result > max_cnt:
        if idx == N-1:
            if cnt == max_cnt:
                if isGood(t_map):
                    result = max_cnt
        else:
            idx += 1
            ck = sum(t_map[idx])
            save_info = t_map[idx][:]
            if ck != 0 and cnt < max_cnt:
                t_map[idx] = [0] * M
                solve(idx, cnt+1, max_cnt, t_map)
            if ck != M and cnt < max_cnt:
                t_map[idx] = [1] * M
                solve(idx, cnt+1, max_cnt, t_map)
            t_map[idx] = save_info
            solve(idx, cnt, max_cnt, t_map)

TC = int(input())
for testcase in range(1, TC+1):
    N, M, K = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    if isGood(total_map):
        print('#{} {}'.format(testcase, 0))
    else:
        result = K
        for k in range(1, K):
            solve(-1, 0, k, total_map)
            if result < K:
                break
        print('#{} {}'.format(testcase, result))