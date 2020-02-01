import sys
sys.stdin = open('b_2667.txt', 'r')

def is_inbox(y, x):
    if 0<=y<N and 0<=x<N:
        return True
    return False

def is_good(y, x):
    if visit[y][x] == 0 and total_map[y][x] == '1':
        return True
    return False

def find_danji(y, x):
    global res
    for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yy = y + dy
        xx = x + dx
        if is_inbox(yy, xx) and is_good(yy, xx):
            visit[yy][xx] = 1
            res += 1
            find_danji(yy, xx)


N = int(input())
total_map = list(input() for _ in range(N))
visit = [[0]*N for _ in range(N)]
cnt = 0
res_lst = []
for y in range(N):
    for x in range(N):
        if is_good(y, x):
            cnt += 1
            res = 1
            visit[y][x] = 1
            find_danji(y, x)
            res_lst.append(res)

print(cnt)
res_lst.sort()
for res in res_lst:
    print(res)