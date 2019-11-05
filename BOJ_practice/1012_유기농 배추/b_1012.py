import sys
sys.stdin = open('b_1012.txt', 'r')


def dfs(y, x):
    visit[y][x] = 1
    for dif in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ay = y + dif[0]
        ax = x + dif[1]
        if is_inbox(ay, ax):
            if total_map[ay][ax] == 1 and visit[ay][ax] == 0:
                dfs(ay, ax)


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False


def bfs(y, x):
    que = [(y, x)]
    while que:
        t = que.pop(0)
        visit[t[0]][t[1]] = 1
        for dif in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ay = t[0] + dif[0]
            ax = t[1] + dif[1]
            if is_inbox(ay, ax):
                if total_map[ay][ax] == 1:
                    if (visit[ay][ax] == 0) and ((ay, ax) not in que):
                        que.append((ay, ax))


TC = int(input())
for testcase in range(TC):
    M, N, K = map(int, input().split())
    total_map = [[0]*M for _ in range(N)]

    for _ in range(K):
        xx, yy = map(int, input().split())
        total_map[yy][xx] = 1

    cnt = 0
    visit = [[0]*M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if total_map[y][x] == 1:
                if visit[y][x] == 0:
                    cnt += 1
                    bfs(y, x)
    print(cnt)