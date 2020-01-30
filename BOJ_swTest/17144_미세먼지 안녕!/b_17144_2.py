import sys
sys.stdin = open('b_17144.txt')

import copy

def isInbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True

def diffuse(y, x):
    global nxt_map
    diff = total_map[y][x] // 5
    for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yy = y + dy
        xx = x + dx
        if isInbox(yy, xx) and total_map[yy][xx] != -1:
            nxt_map[yy][xx] += diff
            nxt_map[y][x] -= diff

def circulate():
    global total_map

N, M, T = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
cleaner = list()
for y in range(N):
    for x in range(M):
        if total_map[y][x] == -1:
            cleaner.append((y, x))
for __ in range(T):
    nxt_map = copy.deepcopy(total_map)
    for y in range(N):
        for x in range(M):
            if total_map[y][x] > 0:
                diffuse(y, x)
    total_map = nxt_map

