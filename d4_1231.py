import sys
sys.stdin = open('d4_1231.txt', 'r')


def find_sp(p):
    global sp
    for i in range(N):
        if tree_lst[i][0] == p:
            if len(tree_lst[i]) > 2:
                find_sp(tree_lst[i][2])
            else:
                sp = p
            break


def solve(p):
    global result
    if visit[int(p)] == 0:
        result += tree_lst[int(p)-1][1]
        visit[int(p)] = 1
        if len(tree_lst[int(p) - 1]) == 4:
            find_sp(tree_lst[int(p) - 1][3])
            solve(sp)
        for i in range(N):
            if len(tree_lst[i]) > 2:
                if tree_lst[i][2] == p:
                    solve(tree_lst[i][0])


TC = 10
for testcase in range(1, TC+1):
    N = int(input())
    tree_lst = [list(input().split()) for _ in range(N)]
    sp = '1'
    result = ''
    visit = [0 for _ in range(N+1)]
    while sum(visit) != N:
        find_sp(sp)
        solve(sp)
    print('#{} {}'.format(testcase, result))