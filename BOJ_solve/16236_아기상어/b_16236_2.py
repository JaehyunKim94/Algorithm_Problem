import sys
sys.stdin = open('b_16236.txt', 'r')

def isInbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False

def findEat(sy, sx, sm):
    pos_lst = {(sy, sx)}
    visit = [[0] * N for _ in range(N)]
    visit[sy][sx] = 1
    eat_set = set()
    time = 0
    while pos_lst:
        new_pos = set()
        time += 1
        for ay, ax in pos_lst:
            for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                yy = ay + dy
                xx = ax + dx
                if isInbox(yy, xx) and not visit[yy][xx]:
                    visit[yy][xx] = 1
                    if 0 < total_map[yy][xx] < sm:
                        eat_set.add((yy, xx))
                    elif total_map[yy][xx] > sm:
                        continue
                    else:
                        new_pos.add((yy, xx))

        if eat_set:
            eat_set = sorted(list(eat_set))
            ey, ex = eat_set[0][0], eat_set[0][1]
            return ey, ex, time
        pos_lst = new_pos

def solve(sy, sx):
    ny, nx = sy, sx
    nm = 2
    res = 0
    ate = 0
    while True:
        eat = findEat(ny, nx, nm)
        if eat:
            ny, nx = eat[0], eat[1]
            total_map[ny][nx] = 0
            res += eat[2]
            ate += 1
            if ate == nm:
                nm += 1
                ate = 0
        else:
            return res

N = int(input())
total_map = [[] for _ in range(N)]
sy, sx = 0, 0
for y in range(N):
    new_info = list(map(int, input().split()))
    for x in range(N):
        if new_info[x] == 9:
            sy, sx = y, x
            new_info[x] = 0
    total_map[y] = new_info

print(solve(sy, sx))