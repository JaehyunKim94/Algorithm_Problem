import sys
sys.stdin = open('d3_5208.txt', 'r')


def solve(k, cnt, bat):
    global result
    k += 1
    for kk in range(k, k+bat):
        if kk > N-1:
            if cnt < result:
                result = cnt
                break
        elif cnt < result - 1:
            solve(kk, cnt + 1, new_lst[kk])


TC = int(input())
for testcase in range(1, TC+1):
    new_lst = list(map(int, input().split()))
    N = new_lst[0]
    result = 99999
    solve(1, 0, new_lst[1])
    print('#{} {}'.format(testcase, result))