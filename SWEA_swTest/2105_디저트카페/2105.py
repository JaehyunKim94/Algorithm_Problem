import sys
sys.stdin = open('2105.txt' ,'r')


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def back_check(y, x, des_lst, cnt_lst):
    global result
    dd_lst = des_lst[:]
    for _ in range(cnt_lst[0]):
        y -= 1
        x -= 1
        if not is_inbox(y, x) or total_map[y][x] in dd_lst:
            return
        else:
            dd_lst.append(total_map[y][x])
    for _ in range(cnt_lst[1]-1):
        y -= 1
        x += 1
        if not is_inbox(y, x) or total_map[y][x] in dd_lst:
            return
        else:
            dd_lst.append(total_map[y][x])
    result = max(result, len(dd_lst))


def solve(y, x, idx, des_lst, cnt_lst):
    dif = [(1, 1), (1, -1)]
    dy, dx = dif[idx]
    yy = y + dy
    xx = x + dx
    if is_inbox(yy, xx):
        if total_map[yy][xx] in des_lst:
            return
        des_lst.append(total_map[yy][xx])
        cnt_lst[idx] += 1
        if idx == 1:
            back_check(yy, xx, des_lst, cnt_lst)
            solve(yy, xx, idx, des_lst, cnt_lst)
        if idx == 0:
            solve(yy, xx, idx, des_lst, cnt_lst)
            solve(yy, xx, idx+1, des_lst, cnt_lst)
        cnt_lst[idx] -= 1
        des_lst.pop()


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    for y in range(N-2):
        for x in range(1, N-1):
            solve(y, x, 0, [total_map[y][x]], [0, 0])
    print('#{} {}'.format(testcase, result))