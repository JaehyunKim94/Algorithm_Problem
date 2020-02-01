import sys
sys.stdin = open('2636.txt', 'r')
from pprint import pprint


def is_inbobx(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False


def make_air():
    global total_map
    que = [(0, 0)]
    while que:
        y, x = que.pop()
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            yy = y + dy
            xx = x + dx
            if is_inbobx(yy, xx) and total_map[yy][xx] == 0:
                total_map[yy][xx] = -1
                que.append((yy, xx))


def near_air(y, x):
    for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yy = y + dy
        xx = x + dx
        if is_inbobx(yy, xx) and total_map[yy][xx] == -1:
            return True
    return False


def hole_air():
    global total_map
    que = [(0, 0)]
    visit = [[0]*M for _ in range(N)]
    visit[0][0] = 1
    while que:
        y, x = que.pop()
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            yy = y + dy
            xx = x + dx
            if is_inbobx(yy, xx) and visit[yy][xx] == 0 and total_map[yy][xx] <= 0:
                visit[yy][xx] = 1
                que.append((yy, xx))
                if total_map[yy][xx] == 0:
                    total_map[yy][xx] = -1


def melt():
    global melting_info
    new_map = [[0] * M for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(M):
            if total_map[y][x] == -1:
                new_map[y][x] = -1
            elif total_map[y][x] == 1 and near_air(y, x):
                new_map[y][x] = -1
            else:
                new_map[y][x] = total_map[y][x]
                if total_map[y][x] == 1:
                    cnt += 1
    melting_info.append(cnt)
    return new_map


N, M = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
melting_info = [0]
make_air()
time = 0
first_cnt = 0
for y in range(N):
    for x in range(M):
        if total_map[y][x] > 0:
            first_cnt+= 1
melting_info[0] = first_cnt
while True:
    time += 1
    total_map = melt()
    hole_air()
    if melting_info[time] == 0:
        break
print(time)
print(melting_info[time-1])