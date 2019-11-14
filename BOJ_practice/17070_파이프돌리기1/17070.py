import sys
sys.stdin = open('17070.txt', 'r')

def get_pos(n):
    lst = []
    for i in range(n+1):
        a = i
        b = n - i + 1
        if a < N and b < N:
            lst.append((a, b))
    return lst

def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False

N = int(input())
block = [list(map(int, input().split())) for _ in range(N)]
cnt_map = [[[0]*3 for __ in range(N)] for _ in range(N)]
cnt_map[0][1][0] += 1
pos_lst = [get_pos(i) for i in range(1, 2*(N-1))]

for pos in pos_lst:
    for y, x in pos:
        if not block[y][x]:
            tg = cnt_map[y][x]
            ay, ax = y-1, x-1
            if is_inbox(ay, ax) and not block[ay][ax] and not block[ay][x] and not block[y][ax]:
                tg[1] += sum(cnt_map[ay][ax])
            if ax > 0:
                tg[0] += cnt_map[y][ax][0] + cnt_map[y][ax][1]
            if ay > 0:
                tg[2] += cnt_map[ay][x][2] + cnt_map[ay][x][1]
            cnt_map[y][x] = tg

print(sum(cnt_map[N-1][N-1]))