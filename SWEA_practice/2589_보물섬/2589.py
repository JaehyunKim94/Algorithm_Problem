import sys
sys.stdin = open('2589.txt', 'r')

def solve(y, x):
    global result
    que = [(y, x)]
    visit = [[0] * M for _ in range(N)]
    visit[y][x] = 1
    d = 0
    while que:
        r = len(que)
        d += 1
        for i in range(r):
            y, x = que.pop(0)
            for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                yy = y + dy
                xx = x + dx
                if 0 <= yy < N and 0 <= xx < M and visit[yy][xx] == 0 and total_map[yy][xx] == 'L':
                    visit[yy][xx] = 1
                    que.append((yy, xx))

    result = max(d-1, result)

N, M = map(int, input().split())
total_map = [input() for _ in range(N)]
result = -1
for y in range(N):
    for x in range(M):
        if total_map[y][x] == 'L':
            solve(y, x)
print(result)