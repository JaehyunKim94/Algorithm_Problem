import sys
sys.stdin = open('b_17144.txt')

def isInbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True

def diffuse(y, x, nxt_map):
    diff = total_map[y][x] // 5
    for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yy = y + dy
        xx = x + dx
        if isInbox(yy, xx) and total_map[yy][xx] != -1:
            nxt_map[yy][xx] += diff
            nxt_map[y][x] -= diff
    return nxt_map

def circulate(t_map):
    end_point = [0, N-1]
    for idx in range(2):
        cy = cleaner[idx]
        ep = end_point[idx]
        if idx == 0:
            for y in range(cy-1, ep, -1):
                t_map[y][0] = t_map[y-1][0]
            for x in range(M-1):
                t_map[ep][x] = t_map[ep][x+1]
            for y in range(ep, cy):
                t_map[y][M-1] = t_map[y+1][M-1]
            for x in range(M-1, 0, -1):
                t_map[cy][x] = t_map[cy][x-1]
        else:
            for y in range(cy+1, ep):
                t_map[y][0] = t_map[y+1][0]
            for x in range(M-1):
                t_map[ep][x] = t_map[ep][x+1]
            for y in range(ep, cy, -1):
                t_map[y][M-1] = t_map[y-1][M-1]
            for x in range(M-1, 0, -1):
                t_map[cy][x] = t_map[cy][x-1]
        t_map[cy][1] = 0
    return t_map

def solve(t_map):
    nxt_map = [[0] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            nxt_map[y][x] += t_map[y][x]
            if t_map[y][x] > 0:
                nxt_map = diffuse(y, x, nxt_map)
    nxt_map = circulate(nxt_map)
    return nxt_map

N, M, T = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
cleaner = list()
for y in range(N):
    for x in range(M):
        if total_map[y][x] == -1:
            cleaner.append(y)
cleaner.sort()
for __ in range(T):
    total_map = solve(total_map)

result = sum(sum(total_map, [])) + 2
print(result)