import sys
sys.stdin = open('1493.txt', 'r')

def my_sum(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

ran_lst = []
for j in range(0, 142):
    ran_lst.append(my_sum(j))

TC = int(input())
for testcase in range(1, TC+1):
    cal_lst = []        # 해당 숫자, 범위, 차이
    p, q = map(int, input().split())
    for i in range(1, len(ran_lst)):
        if ran_lst[i-1] < p <= ran_lst[i]:
            cal_lst.append([p, i, ran_lst[i] - p])
        if ran_lst[i-1] < q <= ran_lst[i]:
            cal_lst.append([q, i, ran_lst[i] - q])
        if len(ran_lst) == 2:
            break

    a_s = [1+cal_lst[0][2], cal_lst[0][1] - cal_lst[0][2]]  # [y, x]
    b_s = [1+cal_lst[1][2], cal_lst[1][1] - cal_lst[1][2]]  # [y, x]
    y = a_s[0] + b_s[0]
    x = a_s[1] + b_s[1]
    gap = y - 1
    tg_y = y - gap
    tg_x = x + gap
    res = my_sum(tg_x) - gap
    print('#{} {}'.format(testcase, res))