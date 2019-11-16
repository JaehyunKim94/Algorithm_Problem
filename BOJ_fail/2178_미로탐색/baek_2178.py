import sys
sys.stdin = open('b_2178.txt', 'r')


def is_inbox(y, x):
    if (0 <= y < N) and (0 <= x < M):
        return True
    return False


def solve():
    que = [(0, 0)]
    cnt = 1
    visit = [[0] * M for _ in range(N)]
    visit[0][0] = 1
    while que:
        r = len(que)
        for _ in range(r):
            y, x = que.pop(0)
            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                yy = y + dy
                xx = x + dx
                if yy == N-1 and xx == M-1:
                    return cnt + 1
                if is_inbox(yy, xx) and not visit[yy][xx] and total_map[yy][xx]=='1':
                    visit[yy][xx] = 1
                    que.append((yy, xx))
        cnt += 1


N, M = map(int, input().split())
total_map = [input() for _ in range(N)]
result = solve()
print(result)