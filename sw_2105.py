import sys
sys.stdin = open('sw_2105.txt', 'r')


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def solve(p, a, b, k, di_lst):
    global starting_point
    global i
    y = p[0]
    x = p[1]
    tg = total_map[y][x]
    if tg in di_lst:
        return
    else:
        di_lst.append(tg)
        yy = y + dif[k][0]
        xx = x + dif[k][1]
        new_p = (yy, xx)
        if is_inbox(yy, xx):
            solve(new_p, a+1, b, di_lst)


dif = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    for y in range(N-2):
        for x in range(1, N-1):
            di_lst = []
            starting_point = (y, x)
            solve(starting_point, 0, 0, 0, di_lst)

