import sys
sys.stdin = open('b_14888.txt', 'r')


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
    if k == N - 1:
        result_max = max(result_max, num)
        result_min = min(result_min, num)
        return
    else:
        k += 1
        tg_num = num_lst[k]
        for i in range(4):
            if cal_lst[i] > 0:
                cal_lst[i] -= 1
                solve(k, my_cal(num, i, tg_num))
                cal_lst[i] += 1


N = int(input())
num_lst = list(map(int, input().split()))
cal_lst = list(map(int, input().split()))
result_max = -1000000001
result_min = 1000000001
solve(0, num_lst[0])
print(result_max)
print(result_min)