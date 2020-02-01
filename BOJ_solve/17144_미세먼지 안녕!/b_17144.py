import sys
sys.stdin = open('b_17144.txt', 'r')


def is_inbox(y, x):
    if 0 <= y < R and 0 <= x < C:
        return True
    return False


def power_on():
    sun = clean[0][0]
    for y in range(sun-1, 0, -1):
        total_map[y][0] = total_map[y-1][0]
    for x in range(0, C-1):
        total_map[0][x] = total_map[0][x+1]
    for y in range(sun):
        total_map[y][C-1] = total_map[y+1][C-1]
    for x in range(C-1, 1, -1):
        total_map[sun][x] = total_map[sun][x-1]
    total_map[sun][1] = 0

    for y in range(sun+2, R-1):
        total_map[y][0] = total_map[y+1][0]
    for x in range(0, C-1):
        total_map[R-1][x] = total_map[R-1][x+1]
    for y in range(R-1, sun+1, -1):
        total_map[y][C-1] = total_map[y-1][C-1]
    for x in range(C-1, 1, -1):
        total_map[sun+1][x] = total_map[sun+1][x-1]
    total_map[sun+1][1] = 0


def munji(y, x, mun_dic):
    p = total_map[y][x] // 5
    cnt = 0
    for dif in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        yy = y + dif[0]
        xx = x + dif[1]
        if is_inbox(yy, xx):
            if total_map[yy][xx] > -1:
                cnt += 1
                if (yy, xx) not in mun_dic.keys():
                    mun_dic.update({(yy, xx): p})
                else:
                    mun_dic[(yy, xx)] += p
    total_map[y][x] -= p*cnt


def solve():
    mun_dic = dict()
    for y in range(R):
        for x in range(C):
            if total_map[y][x] > 0:
                munji(y, x, mun_dic)
    for k, v in mun_dic.items():
        total_map[k[0]][k[1]] += v
    power_on()
    for i in range(2):
        total_map[clean[i][0]][0] = -1


R, C, T = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(R)]
for y in range(R):
    if total_map[y][0] == -1:
        clean = [(y, 0), (y+1, 0)]
        break

for _ in range(T):
    solve()
res_lst = sum(total_map, [])
print(sum(res_lst) + 2)