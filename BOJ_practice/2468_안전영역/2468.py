import sys
sys.stdin = open('2468.txt', 'r')
from pprint import pprint

def spread(y, x):
    global visit
    que = [(y, x)]
    while que:
        y, x = que.pop()
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            yy = y + dy
            xx = x + dx
            if 0 <= yy < N and 0 <= xx < N and visit[yy][xx] == 0 and total_map[yy][xx] > 0:
                visit[yy][xx] = 1
                que.append((yy, xx))


def check():
    global visit
    global cnt
    for y in range(N):
        for x in range(N):
            if visit[y][x] == 0 and total_map[y][x] > 0:
                cnt += 1
                visit[y][x] = 1
                spread(y, x)


N = int(input())
total_map = [0] * N
max_h = 0
min_h = 101
for i in range(N):
    new_info = list(map(int, input().split()))
    max_h = max(max(new_info), max_h)
    min_h = min(min(new_info), min_h)
    total_map[i] = new_info
result = 1
for t in range(1, max_h+1):
    for y in range(N):
        for x in range(N):
            if total_map[y][x] > 0:
                total_map[y][x] -= 1
    if t < min_h:
        continue
    else:
        visit = [[0] * N for _ in range(N)]
        cnt = 0
        check()
        result = max(cnt, result)
print(result)