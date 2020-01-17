import sys
sys.stdin = open('b_5427.txt','r')

import collections

def isInbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False

def isFinish(y, x):
    if y == 0 or x == 0 or y == N-1 or x == M-1:
        return True
    return False

TC = int(input())
for testcase in range(TC):
    M, N = map(int, input().split())
    total_map = [[0] * M for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    fire = set()
    fire_visit = [[0] * M for _ in range(N)]
    que = collections.deque()
    cnt = 0
    for y in range(N):
        new_info = input()
        for x in range(M):
            if new_info[x] == '#':
                total_map[y][x] = 1
            elif new_info[x] == '*':
                total_map[y][x] = 1
                fire_visit[y][x] = 1
                fire.add((y, x))
            elif new_info[x] == '@':
                que.append((y, x))
                visit[y][x] = 1
                cnt += 1
    result = 'IMPOSSIBLE'
    sg = False
    year = 0
    dydx = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while que:
        # 다음
        year += 1
        tmp_cnt = 0
        tmp_fire = set()

        # 다음 불 맵 구하기
        for y, x in fire:
            for dy, dx in dydx:
                yy = y + dy
                xx = x + dx
                if isInbox(yy, xx) and total_map[yy][xx] == 0 and fire_visit[yy][xx] == 0:
                    fire_visit[yy][xx] = 1
                    tmp_fire.add((yy, xx))

        # 갈 수 있는 곳 구하기
        for kk in range(cnt):
            y, x = que.popleft()
            for dy, dx in dydx:
                yy = y + dy
                xx = x + dx
                if isInbox(yy, xx) and total_map[yy][xx] == 0 and not visit[yy][xx] and not fire_visit[yy][xx]:
                    if isFinish(yy, xx):
                        result = year+1
                        sg = True
                        break
                    visit[yy][xx] = 1
                    que.append((yy, xx))
                    tmp_cnt += 1

        for y, x in tmp_fire:
            total_map[y][x] = 1
        fire = tmp_fire
        cnt = tmp_cnt

    print(result)