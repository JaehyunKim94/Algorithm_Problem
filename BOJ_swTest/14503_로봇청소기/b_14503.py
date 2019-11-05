import sys
sys.stdin = open('b_14503.txt', 'r')
from pprint import pprint


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False


def solve(y, x, direc):
    global result
    visit = [[0] * M for _ in range(N)]
    dif = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    d = direc
    while True:
        visit[y][x] = 1
        pprint(visit)
        cnt = 0
        for __ in range(4):
            dd = (d - 1)%4
            cnt += 1
            cy, cx = y + dif[dd][0], x + dif[dd][1]
            if is_inbox(cy, cx):
                if total_map[cy][cx] == 0 and visit[cy][cx] == 0:
                    y, x = cy, cx
                    d = dd
                    break
                else:
                    d = dd
            else:
                d = dd
        if cnt == 4:
            d = (d+1)%4
            ny = y-dif[d][0]
            nx = x-dif[d][1]
            if is_inbox(ny, nx) and total_map[ny][nx] == 1:
                break
            else:
                break
    visit = sum(visit, [])
    result = sum(visit)


N, M = map(int, input().split())
s_y, s_x, d = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
result = 0
solve(s_y, s_x, d)
print(result)
