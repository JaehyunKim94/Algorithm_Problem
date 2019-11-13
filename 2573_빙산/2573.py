import sys
sys.stdin = open('2573.txt', 'r')

from pprint import pprint
# 13


def check_map(p, t_map):
    global visit
    que = [p]
    while que:
        y, x = que.pop(0)
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            yy = y + dy
            xx = x + dx
            if visit[yy][xx] == 0 and t_map[yy][xx] > 0:
                visit[yy][xx] = 1
                que.append((yy, xx))

    for y in range(N):
        for x in range(M):
            if t_map[y][x] > 0 and visit[y][x] == 0:
                return True
    return False


def find_sp(t_map):
    for y in range(N):
        for x in range(M):
            if t_map[y][x] != 0:
                return (y, x)


def melt(t_map):
    new_map = [[0] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if t_map[y][x] != 0:
                ice = t_map[y][x]
                for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    yy = y + dy
                    xx = x + dx
                    if t_map[yy][xx] == 0:
                        ice -= 1
                if ice < 0:
                    ice = 0
                new_map[y][x] = ice
    return new_map


N , M = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
result = 0
while True:
    total_map = melt(total_map)
    sp = find_sp(total_map)
    if sp:
        visit = [[0]*M for _ in range(N)]
        visit[sp[0]][sp[1]] = 1
        result += 1
        if check_map(sp, total_map):
            break
    else:
        result = 0
        break
print(result)