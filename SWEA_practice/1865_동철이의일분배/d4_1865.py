import sys
sys.stdin = open('d4_1865.txt', 'r')


def solve(dep, res):
    dep += 1
    global result

    if dep == N:
        if res > result:
            result = res

    else:
        for x in range(N):
            if visit[x] == 0:
                if res * total_map[dep][x] / 100 > result:
                    visit[x] = 1
                    solve(dep, res * total_map[dep][x] / 100)
                    visit[x] = 0


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    num_lst = [i for i in range(N)]
    visit = [0 for _ in range(N)]
    solve(-1, 1)
    print('#{}'.format(testcase), end=' ')
    print('%.6f' %round(result * 100, 6))
