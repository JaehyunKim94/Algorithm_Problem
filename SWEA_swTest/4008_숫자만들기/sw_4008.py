import sys
sys.stdin = open('sw_4008.txt', 'r')


def my_cal(num, i, tg_num):
    if i == 0:
        return num + tg_num
    elif i == 1:
        return num - tg_num
    elif i == 2:
        return num * tg_num
    elif i == 3:
        return int(num / tg_num)


def solve(k, num):
    global result_max
    global result_min
    if k == N-1:
        if num > result_max:
            result_max = num
        if num < result_min:
            result_min = num
    else:
        k += 1
        tg_num = num_lst[k]
        for i in range(4):
            if cal_lst[i] > 0:
                cal_lst[i] -= 1
                solve(k, my_cal(num, i, tg_num))
                cal_lst[i] += 1


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    cal_lst = list(map(int, input().split()))
    num_lst = list(map(int, input().split()))
    result_max = -100000000
    result_min = 100000000
    solve(0, num_lst[0])
    print('#{} {}'.format(testcase, result_max - result_min))