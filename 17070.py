def solve():
    dif = [(0, 1), (1, 1), (1, 0)]
    que = [(0, 1, 0)]
    cnt = 0
    while que:
        y, x, d = que.pop()
        if y == N-1 and x == N-1:
            cnt += 1
            continue
        ac, bc = False, False
        for i in (0, 2, 1):
            dy, dx = dif[i]
            yy = y + dy
            xx = x + dx
            if yy < N and xx < N and total_map[yy][xx] == 0:
                if i == 0:
                    ac = True
                    if d in (0, 1):
                        que.append((yy, xx, i))
                elif i == 2:
                    bc = True
                    if d in (1, 2):
                        que.append((yy, xx, i))
                elif i == 1 and ac and bc:
                    que.append((yy, xx, 1))
    return cnt

N = int(input())
total_map = [list(map(int, input().split())) for _ in range(N)]
print(solve())