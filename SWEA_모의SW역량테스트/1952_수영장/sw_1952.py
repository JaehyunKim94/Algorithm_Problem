import sys
sys.stdin = open('sw_1952.txt', 'r')


def solve(k, cos):
    global result
    if k > 11:
        if cos < result:
            result = cos
    else:
        solve(k+1, cos+mon_cost[k])
        solve(k+3, cos+cost_lst[2])


TC = int(input())
for testcase in range(1, TC+1):
    cost_lst = list(map(int, input().split()))      # 이용권 가격
    month_lst = list(map(int, input().split()))     # 월별 이용 횟수
    mon_cost = [0 for _ in range(12)]   # 달마다의 코스트
    result = cost_lst[3]
    for i in range(12):
        mon_cost[i] = month_lst[i] * cost_lst[0]
        if mon_cost[i] > cost_lst[1]:
            mon_cost[i] = cost_lst[1]
    solve(0, 0)
    print('#{} {}'.format(testcase, result))