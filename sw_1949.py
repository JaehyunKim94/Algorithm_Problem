import sys
sys.stdin = open('sw_1949.txt', 'r')


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def solve(y, x, down, cnt):
    global visit
    global result
    cnt += 1
    if cnt > result:
        result = cnt
    height = total_map[y][x]
    for dif in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        yy = y + dif[0]
        xx = x + dif[1]
        if is_inbox(yy, xx) and (yy, xx) not in visit:
            n_height = total_map[yy][xx]
            if n_height < height:
                visit.append((yy, xx))
                solve(yy, xx, down, cnt)
                visit.remove((yy, xx))
            else:
                if down > 0:
                    if n_height-height < down:
                        s_height = total_map[yy][xx]
                        total_map[yy][xx] = height-1
                        visit.append((yy, xx))
                        solve(yy, xx, 0, cnt)
                        visit.remove((yy, xx))
                        total_map[yy][xx] = s_height


TC = int(input())
for testcase in range(1, TC+1):
    N, K = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    ck_map = sum(total_map, [])
    highest = max(ck_map)
    result = 0
    for y in range(N):
        for x in range(N):
            if total_map[y][x] == highest:
                visit = [(y, x)]
                solve(y, x, K, 0)
    print('#{} {}'.format(testcase, result))