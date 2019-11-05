import sys
sys.stdin = open('sw_4013.txt', 'r')


def get_point(mag_lst):
    global score
    for po in range(4):
        if mag_lst[po][0] == 1:
            score += 2**po


def get_rot_lst(tg, rot):
    if visit[tg] == 0:
        visit[tg] = 1
        r_lst.append((tg, rot))
        kk = tg-1
        if -1 < kk < 4:
            if mag_lst[tg][6] != mag_lst[kk][2]:
                get_rot_lst(kk, -rot)
        kk = tg+1
        if -1 < kk < 4:
            if mag_lst[tg][2] != mag_lst[kk][6]:
                get_rot_lst(kk, -rot)


def rot_mag(tg, rot):
    global mag_lst
    if rot == -1:
        new_lst = mag_lst[tg][1:]
        new_lst.append(mag_lst[tg][0])
        mag_lst[tg] = new_lst
    elif rot == 1:
        new_lst = mag_lst[tg][:7]
        new_lst.insert(0, mag_lst[tg][7])
        mag_lst[tg] = new_lst
    mag_lst[tg] = new_lst


TC = int(input())
for testcase in range(1, TC+1):
    K = int(input())
    mag_lst = [list(map(int, input().split())) for _ in range(4)]
    score = 0
    for i in range(K):
        tg, rot = map(int, input().split())
        tg -= 1
        visit = [0] * 4
        r_lst = []
        get_rot_lst(tg, rot)
        for r in r_lst:
            rot_mag(r[0], r[1])
    get_point(mag_lst)
    print('#{} {}'.format(testcase, score))
