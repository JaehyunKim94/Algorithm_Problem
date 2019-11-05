import sys
sys.stdin = open('d5_1247.txt', 'r')


def get_dis(ax, ay, bx, by):
    ans = abs(ax - bx) + abs(ay - by)
    return ans


def solve(k, mid):
    global result
    if sum(visit) == N+2:
        las = mid + total_map[k][1]
        if result > las:
            result = las

    else:
        for i in range(N+2):
            if visit[i] == 0:
                if mid + total_map[k][i] < result:
                    visit[i] = 1
                    solve(i, mid + total_map[k][i])
                    visit[i] = 0


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    ran = N+2
    new_lst = list(map(int, input().split()))
    total_map = [[0 for _ in range(ran)] for __ in range(ran)]
    result = 999999

    for y in range(ran):
        for x in range(ran):
            ax = new_lst[2*y]
            ay = new_lst[2*y+1]
            bx = new_lst[2*x]
            by = new_lst[2*x+1]
            total_map[y][x] = get_dis(ax, ay, bx, by)

    visit = [0 for _ in range(N+2)]
    visit[1] = 1    # 집
    visit[0] = 1    # 회사
    solve(0, 0)
    print('#{} {}'.format(testcase, result))





    # p_lst = [0 for _ in range(N)]
    # k = 0
    # comp = (new_lst[0], new_lst[1])
    # home = (new_lst[2], new_lst[3])
    # for i in range(4, 2*(N+2), 2):
    #     p_lst[k] = (new_lst[i], new_lst[i+1])
    #     k += 1
