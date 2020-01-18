import sys
sys.stdin = open('b_5427.txt', 'r')

def solve(que, fire, total_map):
    year = 0
    while que:
        year += 1
        tmp_fire = set()
        for y, x in fire:
            for dy, dx in dydx:
                yy = y + dy
                xx = x + dx
                if 0 <= yy < N and 0 <= xx < M and total_map[yy][xx] <= 0:
                    tmp_fire.add((yy, xx))
                    total_map[yy][xx] = 1
        fire = tmp_fire

        tmp_que = set()
        for y, x in que:
            if y == 0 or x == 0 or y == N-1 or x == M-1:
                return year
            for dy, dx in dydx:
                yy = y + dy
                xx = x + dx
                if 0 <= yy < N and 0 <= xx < M and total_map[yy][xx] == 0:
                    total_map[yy][xx] = -1
                    tmp_que.add((yy, xx))
        que = tmp_que
    return "IMPOSSIBLE"

TC = int(input())
for ___ in range(TC):
    M, N = map(int, input().split())
    total_map = [[0] * M for _ in range(N)]
    fire = set()
    dydx = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    year = 1
    for y in range(N):
        new_info = input()
        for x in range(M):
            if new_info[x] == '#':
                total_map[y][x] = 1
            elif new_info[x] == '*':
                total_map[y][x] = 1
                fire.add((y, x))
            elif new_info[x] == '@':
                total_map[y][x] = -1
                que = {(y, x)}
    print(solve(que, fire, total_map))

