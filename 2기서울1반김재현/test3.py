import sys
sys.stdin = open('test3.txt', 'r')
import time

def get_dis(r_p, m_p):
    dis = abs(r_p[0] - m_p[0]) + abs(r_p[1] - m_p[1])
    return dis*2


def solve(k, mg, fl):
    global result
    if k == ran-1:
        if mg > result:
            result = mg
        return
    else:
        k += 1
        if fl + mineral[k][1] <= C:
            solve(k, mg+mineral[k][0], fl+mineral[k][1])
        solve(k, mg, fl)


TC = int(input())
for testcase in range(1, TC+1):
    st = time.time()
    N, M, C = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    mineral = []
    robot = 0
    ran = 0
    for y in range(N):
        for x in range(M):
            if total_map[y][x] == 1:
                robot = (y, x)
            elif total_map[y][x] != 0:
                mineral.append((y, x, total_map[y][x]))
                ran += 1

    result = 0
    for i in range(ran):
        distance = get_dis(robot, mineral[i])
        mineral[i] = (mineral[i][2], distance)
    solve(-1, 0, 0)
    print('#{} {}'.format(testcase, result))
    print(time.time() - st)
