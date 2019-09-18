import sys
sys.stdin = open('d3_1240.txt', 'r')

ck_lst = ['3211', '2221', '2122', '1411', '1132', '1231', '1114', '1312', '1213', '3112']


def change_num(num_lst):
    res = []
    for num in num_lst:
        s_p = '0'
        cnt = 1
        cnt_num = ''
        for i in range(1, 7):
            if num[i] == s_p:
                cnt += 1
            else:
                cnt_num += str(cnt)
                s_p = num[i]
                cnt = 1
        cnt_num += str(cnt)
        res.append(cnt_num)

    for k in range(8):
        for i in range(10):
            if res[k] == ck_lst[i]:
                res[k] = i
                break

    ck = 3 * sum(res[::2]) + sum(res[1:7:2]) + res[7]
    if ck%10 == 0:
        return sum(res)
    return 0


def find_tg():
    for y in range(N):
        for x in range(M-1, -1, -1):
            if total_map[y][x] == '1':
                return total_map[y][x-55:x+1]


def solve():
    tg = find_tg()
    num_lst = []
    for i in range(0, 56, 7):
        num_lst.append(tg[i:i+7])
    return change_num(num_lst)


TC = int(input())
for testcase in range(1, TC+1):
    N, M = map(int, input().split())
    total_map = [input() for _ in range(N)]
    result = solve()
    print('#{} {}'.format(testcase, result))