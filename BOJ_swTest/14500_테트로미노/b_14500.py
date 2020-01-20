import sys
sys.stdin = open('b_14500.txt', 'r')

def isInbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True

def solve(y, x, cnt, num, bef):
    global result
    if cnt == 4:
        result = max(result, num)
    else:
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            yy = y + dy
            xx = x + dx
            if isInbox(yy, xx) and (-dy, -dx) != bef:
                solve(yy, xx, cnt+1, num + total_map[yy][xx], (dy, dx))

def checkCross(y, x):
    r = total_map[y][x]
    res = 0
    if 0 < x < M-1:
        if 0 <= y < N-1:
            a = total_map[y][x+1] + total_map[y][x-1] + total_map[y+1][x]
            res = max(res, a + r)
        if 0 < y < N:
            a = total_map[y][x+1] + total_map[y][x-1] + total_map[y-1][x]
            res = max(res, a + r)
    if 0 < y < N-1:
        if 0 <= x < M-1:
            a = total_map[y-1][x] + total_map[y+1][x] + total_map[y][x+1]
            res = max(res, a + r)
        if 0 < x < M:
            a = total_map[y-1][x] + total_map[y+1][x] + total_map[y][x-1]
            res = max(res, a + r)
    return res

N, M = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
result = 0
for y in range(N):
    for x in range(M):
        solve(y, x, 1, total_map[y][x], (-1, -1))
        result = max(result, checkCross(y, x))
print(result)