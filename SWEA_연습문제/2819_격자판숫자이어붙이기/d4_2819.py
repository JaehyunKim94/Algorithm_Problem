import sys
sys.stdin = open('s_2819.txt', 'r')


def is_inbox(y, x):
    if 0 <= y < 4 and 0 <= x < 4:
        return True
    return False


def solve(y, x, lst, k):
    global cnt
    lst += total_map[y][x]
    k += 1

    if k == 7:
        if lst not in res_lst:
            res_lst.append(lst)
            cnt += 1
            return

    else:
        for dif in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ay = y + dif[0]
            ax = x + dif[1]
            if is_inbox(ay, ax):
                solve(ay, ax, lst, k)
                lst = lst[:k]

TC = int(input())
for testcase in range(1, TC+1):
    total_map = [input().split() for _ in range(4)]
    res_lst = []
    cnt = 0
    for y in range(4):
        for x in range(4):
            lst = ''
            solve(y, x, lst, 0)
    print('#{} {}'.format(testcase, cnt))