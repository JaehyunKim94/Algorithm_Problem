import sys
sys.stdin = open('s_5650.txt', 'r')

def isInbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True

def getScore(s):
    return s*2 + 1

def solve(y, x, d):
    sy, sx = y, x
    que = (y, x, d)
    score = 0
    while que:
        ay, ax, ad = que
        dy, dx = dydx[ad]
        yy = ay + dy
        xx = ax + dx
        if isInbox(yy, xx):
            if yy == sy and sx == xx:
                return score
            elif total_map[yy][xx] == -1:
                return score
            elif total_map[yy][xx] == 5:
                return getScore(score)
            elif total_map[yy][xx] in range(6, 11):
                hole_num = total_map[yy][xx]
                hole_lst = block_set[hole_num]
                for hy, hx in hole_lst:
                    if hy == yy and hx == xx:
                        continue
                    else:
                        que = (hy, hx, ad)
                        break
            elif total_map[yy][xx] == 0:
                que = (yy, xx, ad)
            else:
                if total_map[yy][xx] == 1:
                    if ad in (0, 3):
                        return getScore(score)
                    else:
                        score += 1
                        if ad == 1:
                            que = (yy, xx, 3)
                        else:
                            que = (yy, xx, 0)

                elif total_map[yy][xx] == 2:
                    if ad in (1, 3):
                        return getScore(score)
                    else:
                        score += 1
                        if ad == 0:
                            que = (yy, xx, 3)
                        else:
                            que = (yy, xx, 1)

                elif total_map[yy][xx] == 3:
                    if ad in (1, 2):
                        return getScore(score)
                    else:
                        score += 1
                        if ad == 0:
                            que = (yy, xx, 2)
                        else:
                            que = (yy, xx, 1)

                elif total_map[yy][xx] == 4:
                    if ad in (0, 2):
                        return getScore(score)
                    else:
                        score += 1
                        if ad == 1:
                            que = (yy, xx, 2)
                        else:
                            que = (yy, xx, 0)
        else:
            return getScore(score)

dydx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    block_set = [set() for _ in range(12)]
    result = 0
    for y in range(N):
        for x in range(N):
            num = total_map[y][x]
            block_set[num].add((y, x))
    for n in range(1, 12):
        for y, x in block_set[n]:
            for idx in range(4):
                dy, dx = dydx[idx]
                yy = y + dy
                xx = x + dx
                if isInbox(yy, xx) and total_map[yy][xx] == 0:
                    if idx in (0, 1):
                        res = solve(yy, xx, 1-idx)
                    else:
                        res = solve(yy, xx, 5-idx)
                    result = max(result, res)

    # for y, x in block_set[0]:
    #     sy, sx = y, x
    #     for idx in range(4):
    #         solve(y, x, idx, 0)
    print('#{} {}'.format(testcase, result))