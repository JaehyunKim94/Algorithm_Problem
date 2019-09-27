def get_dist(r_p, s_p):
    dist = abs(r_p[0] - s_p[0]) + abs(r_p[1] - s_p[1])
    return dist


def perm(k, dis):
    global result
    if dis > result:
        return

    if k == 5:
        if dis < result:
            result = dis

    else:
        k += 1
        for i in range(6):
            if visit[i] == 0:
                visit[i] = 1
                perm(k, dis + get_dist(robot[k], snack[i]))
                visit[i] = 0


TC = int(input())
for testcase in range(TC):
    tc = input()
    total_map = [list(map(int, input().split())) for _ in range(10)]
    robot = []
    snack = []
    for y in range(10):
        for x in range(10):
            if total_map[y][x] == 9:
                robot.append((y, x))
            elif total_map[y][x] != 0:
                snack.append((y, x))
    result = 999999
    visit = [0] * 6
    perm(-1, 0)
    print('#{} {}'.format(tc, result))