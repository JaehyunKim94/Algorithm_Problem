import sys
sys.stdin = open('2573.txt', 'r')


def isInBox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False


def findIce():
    for y in range(N):
        for x in range(M):
            if total_map[y][x] > 0:
                return y, x

def countIce():
    cnt = 0
    for y in range(N):
        for x in range(M):
            if total_map[y][x] > 0:
                cnt += 1
    return cnt

def checkIce(y, x):
    y, x = findIce()
    que = [(y, x)]
    visit = [[0] * M for _ in range(N)]
    visit[y][x] = 1
    while que:
        y, x = que.pop()
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            yy = y + dy
            xx = x + dx
            if isInBox(yy, xx) and total_map[yy][xx] > 0 and not visit[yy][xx]:
                visit[yy][xx] = 1
                que.append((yy, xx))
    if sum(visit) == countIce():
        return True
    return False

def checkWater(y, x):
    cnt = 0
    for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yy = y + dy
        xx = x + dx
        if isInBox(yy, xx) and total_map[yy][xx] == 0:
            cnt += 1
    return cnt

N, M = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
year = 0
while checkIce(findIce()):
    melting = []
    year += 1
    for y in range(N):
        for x in range(M):
            if total_map[y][x] > 0:
                melting.append((y, x, checkWater(y, x)))
    for ice in melting:
        tmp_water = total_map[ice[0]][ice[1]] - ice[2]
        total_map[ice[0]][ice[1]] = max(0, tmp_water)

print(year)