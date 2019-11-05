import sys
sys.stdin = open('14501.txt', 'r')


def solve(k, now_money):
    global result
    if k > n:
        return
    elif k == n:
        result = max(result, now_money)
    else:
        result = max(result, now_money)
        solve(k + money_lst[k][0], now_money + money_lst[k][1])
        solve(k+1, now_money)


result = 0
n = int(input())
money_lst = [0]*n
for i in range(n):
    money_lst[i] = list(map(int, input().split()))
solve(0, 0)
print(result)