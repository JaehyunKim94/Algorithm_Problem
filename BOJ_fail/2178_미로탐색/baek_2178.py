import sys
sys.stdin = open('b_2178.txt', 'r')


def is_inbox(y, x):
    if (0 <= y < N) and (0 <= x < M):
        return True
    return False


def bfs(que, k):
    global cnt
    cnt += 1
    kk = 0
    for _ in range(k):
        t = que.pop(0)
        for dif in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ay = t[0] + dif[0]
            ax = t[1] + dif[1]
            if is_inbox(ay, ax):
                if ay == N-1 and ax == M-1:
                    cnt += 1
                    return
                if total_map[ay][ax] == '1':
                    if visit[ay][ax] == 0:
                        visit[ay][ax] = 1
                        que.append((ay, ax))
                        kk += 1
    print(que)
    if que:
        bfs(que, kk)
    return


N, M = map(int, input().split())
visit = [[0]*M for _ in range(N)]
total_map = [input() for _ in range(N)]
que = [(0, 0)]
visit[0][0] = 1
cnt = 0
bfs(que, 1)
print(cnt)