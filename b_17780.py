import sys
sys.stdin = open('b_17780.txt', 'r')

def isInbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False

def findHorse(lst, idx):
    for ii in range(len(lst)):
        if lst[ii][0] == idx:
            return ii

def changeDirec(direc):
    if direc in (0, 1):
        return 1 - direc
    else:
        return 5 - direc

def white(yy, xx, tg_horse):
    horse_map[yy][xx] += tg_horse
    for i, dd in tg_horse:
        horse_dic[i] = [yy, xx, d]

def red(yy, xx, tg_horse):
    tg_horse = tg_horse[:-1]
    horse_map[yy][xx] += tg_horse
    for i, dd in tg_horse:
        horse_dic[i] = [yy, xx, d]

def blue(yy, xx, d):
    d = changeDirec(d)
    yy = y + dydx[d][0]
    xx = x + dydx[d][1]
    return yy, xx, d

def moveHorse():
    for idx in range(K):
        y, x, d = horse_dic[idx]
        map_idx = findHorse(horse_map[y][x], idx)
        dy, dx = dydx[d]
        yy = y + dy
        xx = x + dx
        blue_cnt = 0
        if not isInbox(yy, xx):
            yy, xx, d = blue(yy, xx, d)
            blue_cnt += 1
        tg_horse = horse_map[y][x][:map_idx+1]
        horse_map[y][x] = horse_map[y][x][:map_idx]
        if total_map[yy][xx] == 0:
            white(yy, xx, tg_horse)
        elif total_map[yy][xx] == 1:
            red(yy, xx, tg_horse)
        else:
            yy, xx, d = blue(yy, xx, d)
            if blue_cnt == 0:
                moveHorse()





dydx = [(0, 1), (0, -1), (-1, 0), (1, 0)]
N, K = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
horse_map = [[list() for _ in range(N)] for __ in range(N)]
horse_dic = dict()
for kk in range(K):
    y, x, d = map(int, input().split())
    horse_dic.update({kk: [y-1, x-1, d]})
    horse_map[y-1][x-1].append([kk, d])


for __ in range(3):
    moveHorse()