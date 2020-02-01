import sys
sys.stdin = open('b_2667.txt', 'r')

def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def dfs(y, x):
    global cnt
    cnt += 1
    visit[y][x] = 1
    for dif in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ay = y + dif[0]
        ax = x + dif[1]
        if is_inbox(ay, ax):
            if total_map[ay][ax] == '1' and visit[ay][ax] == 0:
                dfs(ay, ax)


N = int(input())
total_map = [input() for _ in range(N)]
visit = [[0] * N for _ in range(N)]
res_lst = []
danji = 0
for y in range(N):
    for x in range(N):
        if total_map[y][x] == '1' and visit[y][x] == 0:
            danji += 1
            cnt = 0
            dfs(y, x)
            res_lst.append(cnt)

res_lst.sort()
print(danji)
for res in res_lst:
    print(res)
