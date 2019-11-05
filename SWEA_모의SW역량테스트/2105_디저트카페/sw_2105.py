import sys
sys.stdin = open('sw_2105.txt', 'r')


def is_good(x):
    if 1 <= x < N-1:
        return True
    return False


def get_end(x, L, x_lst):
    if L%2 == 1:
        x_lst.append(x)
        L -= 1
        for i in range(1, L//2+1):
            ax = x - (2*i)
            bx = x + (2*i)
            if is_good(ax):
                x_lst.append(ax)
            if is_good(bx):
                x_lst.append(bx)
    else:
        for ax in range(x-L+1, x+L, 2):
            if is_good(ax):
                x_lst.append(ax)
    return x_lst


def solve(ay, ax, by):
    L = by - ay - 1
    x_lst = get_end(ax, L, list())
    for tx in x_lst:
        d_lst = [0, 0]
        if ax == tx:
            aa = (L+1)//2
            bb = aa
        # else:
        # 포기...
        d_lst[0] = aa
        d_lst[1] = bb
        print(ay, ax, by, tx, d_lst)


dif = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    for ay in range(0, N-2):
        for by in range(ay+2, N):
            for ax in range(1, N-1):
                solve(ay, ax, by)
    print('#{} {}'.format(testcase, result))
