import sys
sys.stdin = open('b_16236.txt', 'r')

def solve(shark_p):
    global t
    global total_map
    v = shark_p[0]
    ate = shark_p[3]
    y, x = shark_p[1], shark_p[2]
    que = [[y, x]]
    visit = [[0]*N for _ in range(N)]
    visit[y][x] = 1
    tt = 0
    while que:
        r = len(que)
        tt += 1
        eat_lst = []
        for _ in range(r):
            nxt = que.pop(0)
            for dif in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                yy = nxt[0] + dif[0]
                xx = nxt[1] + dif[1]
                if 0 <= yy < N and 0 <= xx < N:
                    if visit[yy][xx] == 0:
                        visit[yy][xx] = 1
                        if 0 < total_map[yy][xx] < v:
                            eat_lst.append([yy, xx])
                        elif total_map[yy][xx] == 0 or total_map[yy][xx] == v:
                            que.append([yy, xx])
        if len(eat_lst) > 0:
            y_min = 99
            for eat in eat_lst:
                y_min = min(y_min, eat[0])
            new_lst = []
            for eat in eat_lst:
                if eat[0] == y_min:
                    new_lst.append(eat)

            x_min = 99
            for new in new_lst:
                x_min = min(x_min, new[1])
            ate += 1

            if ate == v:
                v += 1
                ate = 0
            t += tt
            shark_p = [v, y_min, x_min, ate]

            total_map[y_min][x_min] = 0
            solve(shark_p)
            return


N = int(input())
total_map = [list(map(int, input().split())) for _ in range(N)]
fish_cnt = 0
for y in range(N):
    for x in range(N):
        if total_map[y][x] == 9:
            shark_p = [2, y, x, 0]
            total_map[y][x] = 0
        elif total_map[y][x] > 0:
            fish_cnt += 1
t = 0
solve(shark_p)
print(t)