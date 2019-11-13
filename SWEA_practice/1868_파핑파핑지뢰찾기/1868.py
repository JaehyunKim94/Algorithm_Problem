import sys
sys.stdin = open('1868.txt', 'r')
from pprint import pprint


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def count_mine(y, x):
    global ori_map
    cnt = 0
    for dy, dx in [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, -1), (-1, 0), (-1, 1)]:
        yy = y + dy
        xx = x + dx
        if is_inbox(yy, xx):
            if ori_map[yy][xx] == '*':
                cnt += 1
    return cnt


def spread(y, x):
    global visit
    global num_map
    que = [(y, x)]
    while que:
        ay, ax = que.pop()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, -1), (-1, 0), (-1, 1)]:
            yy = ay + dy
            xx = ax + dx
            if is_inbox(yy, xx) and not visit[yy][xx]:
                visit[yy][xx] = 1
                if num_map[yy][xx] == 0:
                    que.append((yy, xx))


def zero_next(y, x):
    global num_map
    for dy, dx in [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, -1), (-1, 0), (-1, 1)]:
        yy = y + dy
        xx = x + dx
        if is_inbox(yy, xx) and num_map[yy][xx] == 0:
            return True
    return False


def solve():
    global num_map
    global visit
    time = 0
    for y in range(N):
        for x in range(N):
            if visit[y][x] == 0:
                if num_map[y][x] == 0:
                    visit[y][x] = 1
                    spread(y, x)
                    time += 1
                else:
                    if not zero_next(y, x):
                        time += 1
    return time

def ori_to_num():
    global ori_map
    global visit
    new_map = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if ori_map[y][x] == '*':
                new_map[y][x] = 9
                visit[y][x] = 1
            else:
                new_map[y][x] = count_mine(y, x)
    return new_map


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    visit = [[0]*N for _ in range(N)]
    ori_map = [input() for _ in range(N)]
    num_map = ori_to_num()
    print('#{} {}'.format(testcase, solve()))
