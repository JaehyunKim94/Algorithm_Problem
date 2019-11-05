import sys
sys.stdin = open('d3_5202.txt', 'r')


def solve(t, cnt):
    global result
    if t[1] > ck or t[1] == 24:
        if cnt > result:
            result = cnt
            return
    else:
        for i in range(N):
            if ton_lst[i][0] >= t[1]:
                solve(ton_lst[i], cnt+1)


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    ton_lst = [list(map(int, input().split())) for _ in range(N)]
    ton_lst.sort(key=lambda element: element[1])
    ck = max(ton_lst, key=lambda element: element[0])[0]
    result = 0
    for j in range(N):
        solve(ton_lst[j], 1)
    print('#{} {}'.format(testcase, result))