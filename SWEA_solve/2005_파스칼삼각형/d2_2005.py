import sys
sys.stdin = open('2005.txt', 'r')

def solve(N):
    ans_lst = [[1] * i for i in range(1, N+1)]
    for i in range(N):
        ans = ans_lst[i]
        if len(ans) > 2:
            for j in range(1, len(ans)-1):
                ans[j] = ans_lst[i-1][j-1] + ans_lst[i-1][j]
    return ans_lst

TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    res = solve(N)

    print('#{}'.format(testcase), end=' ')
    print()
    for a in res:
        for i in range(len(a)):
            print('{}'.format(a[i]), end=' ')
        print()