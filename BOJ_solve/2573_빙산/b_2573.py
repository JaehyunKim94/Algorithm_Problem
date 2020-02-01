def isInbox(ay, ax):
    if 0 <= ay < N and 0 <= ax < M:
        return True
    return False

def countWater(ay, ax):
    cnt = 0
    for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yy = ay + dy
        xx = ax + dx
        if isInbox(yy, xx) and total_map[yy][xx] == 0:
            cnt += 1
    return cnt

def findIce(ck_map):
    for ay in range(N):
        for ax in range(M):
            if ck_map[ay][ax] > 0:
                return ay, ax

def checkMap():
    check_map = [[0] * M for _ in range(N)]
    start_ice = findIce(total_map)
    if start_ice:
        que = [start_ice]
    else:
        return False

    while que:
        y, x = que.pop()
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            yy = y + dy
            xx = x + dx
            if isInbox(yy, xx) and total_map[yy][xx] > 0 and not check_map[yy][xx]:
                que.append((yy, xx))
                check_map[yy][xx] = total_map[yy][xx]
    if check_map != total_map:
        return True
    return False

N, M = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
zero_map = [[0] * M for _ in range(N)]
year = 0
result = 0

while total_map != zero_map:
    year += 1
    melting = []
    for y in range(N):
        for x in range(M):
            if total_map[y][x] > 0:
                nxt_ice = total_map[y][x] - countWater(y, x)
                if nxt_ice > 0:
                    total_map[y][x] = nxt_ice
                else:
                    melting.append((y, x))
    for ice in melting:
        total_map[ice[0]][ice[1]] = 0
    if checkMap():
        result = year
        break

print(result)