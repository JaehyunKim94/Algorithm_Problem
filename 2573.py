import sys
sys.stdin = open('2573.txt', 'r')
from pprint import pprint


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False


def find_tg():
    for y in range(N):
        for x in range(M):
            if total_map[y][x] != 0:
                return (y, x)


def check_map(y, x):
    cnt = 0
    que = [(y, x)]
    visit = [[0] * M for _ in range(N)]
    visit[y][x] = 1
    while que:
        cnt += 1
        y, x = que.pop(0)
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            yy = y + dy
            xx = x + dx
            if is_inbox(yy, xx) and total_map[yy][xx] != 0 and visit[yy][xx] == 0:
                visit[yy][xx] = 1
                que.append((yy, xx))
    return cnt


def melt(y, x):
    minus = 0
    for dif in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
        yy = y + dif[0]
        xx = x + dif[1]
        if is_inbox(yy, xx) and total_map[yy][xx] == 0:
            minus += 1
    new = total_map[y][x] - minus
    if new < 0:
        new = 0
    new_info = (y, x, new)
    change_lst.append(new_info)


N, M = map(int, input().split())
total_map = [0] * N
ice = 0
m_height = 0
for i in range(N):
    new_info = list(map(int, input().split()))
    n_height = 0
    for new in new_info:
        if new != 0:
            ice += 1
        n_height = max(n_height, new)
    m_height = max(n_height, m_height)
    total_map[i] = new_info


time = 0
while time < m_height:
    change_lst = []
    for y in range(N):
        for x in range(M):
            if total_map[y][x] != 0:
                melt(y, x)
    for change in change_lst:
        y, x, v = change
        if v == 0:
            ice -= 1
        total_map[y][x] = v
    time += 1
    tg = find_tg()
    ck_cnt = check_map(tg[0], tg[1])
    if ck_cnt != ice:
        break

if time == m_height:
    time = 0

print(time)