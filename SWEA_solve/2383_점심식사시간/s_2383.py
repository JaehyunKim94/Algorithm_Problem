import sys
sys.stdin = open('sw_2383.txt', 'r')

def getDistance(ay, ax, by, bx):
    res = abs(ay-by) + abs(ax-bx)
    return res

def goDown(s_num, lst):
    if lst:
        stair_time = stair_info[s_num][2]
        stair = [0]*3
        bye = 0
        tg_lst = lst[:]
        lst_cnt = len(tg_lst)
        time = 0
        while bye < lst_cnt:
            time += 1
            for j in range(lst_cnt):
                if tg_lst[j] > 0:
                    tg_lst[j] -= 1
                    if tg_lst[j] == 0:
                        tg_lst[j] = -1
                elif tg_lst[j] == -1:
                    tg_lst[j] = 0
                elif tg_lst[j] == 0:
                    for ii in range(3):
                        if stair[ii] == 0:
                            stair[ii] = stair_time
                            tg_lst[j] = -2
                            break
            for i in range(3):
                if stair[i] > 0:
                    stair[i] -= 1
                    if stair[i] == 0:
                        bye += 1
        return time
    else:
        return 0
def solve(idx, a_lst, b_lst):
    global result
    if idx == person_cnt-1:
        a_time = goDown(0, a_lst)
        b_time = goDown(1, b_lst)
        res = max(a_time, b_time)
        result = min(res, result)
    else:
        idx += 1
        dis = person_distance[idx]
        a_lst.append(dis[0])
        solve(idx, a_lst, b_lst)
        a_lst.pop()
        b_lst.append(dis[1])
        solve(idx, a_lst, b_lst)
        b_lst.pop()

TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    person_position = []
    stair_info = []
    for y in range(N):
        new_info = list(map(int, input().split()))
        for x in range(N):
            if new_info[x] == 1:
                person_position.append((y, x))
            elif new_info[x] > 1:
                stair_info.append((y, x, new_info[x]))
    person_cnt = len(person_position)
    person_distance = [[0, 0] for _ in range(person_cnt)]
    result = 999999
    for idx in range(person_cnt):
        py, px = person_position[idx]
        for i in range(2):
            sy, sx = stair_info[i][0], stair_info[i][1]
            person_distance[idx][i] = getDistance(py, px, sy, sx)

    solve(-1, [], [])
    print('#{} {}'.format(testcase, result))