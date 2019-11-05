import sys
sys.stdin = open('d4_1486.txt', 'r')


def solve(k, res):
    global result
    if k == N-1:
        if B <= res:
            result = res

    else:
        k += 1
        if res + h_lst[k] < result:
            visit[k] = 1
            solve(k, res+h_lst[k])
            visit[k] = 0
        solve(k, res)


TC = int(input())
for testcase in range(1, TC+1):
    N, B = map(int, input().split())
    h_lst = list(map(int, input().split()))
    can_lst = []
    visit = [0 for _ in range(N)]
    result = 99999999
    solve(-1, 0)
    print('#{} {}'.format(testcase, result-B))