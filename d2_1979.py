import sys
sys.stdin = open('1979.txt', 'r')

dy = [1, 0]
dx = [0, 1]


def is_wall(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False

def find_tg(y, x, i):
    visit[y][x] = 1
    yy = y + dy[i]
    xx = x + dx[i]
    if is_wall(yy, xx) and total_map[yy][xx] == 1:
        find_tg(yy, xx, i)
    return

TC = int(input())
for testcase in range(1, TC+1):
    N, K = map(int, input().split())
    total_map = []
    for _ in range(N):
        new_lst = list(map(int, input().split()))
        total_map.append(new_lst)

    res_lst = []
    for i in range(2):
        visit = [[0 for _ in range(N)] for __ in range(N)]
        new_lst = []
        for y in range(N):
            for x in range(N):
                if total_map[y][x] == 1 and visit[y][x] == 0:
                    find_tg(y, x, i)
                    if is_wall(y+dy[i], x+dx[i]) and total_map[y+dy[i]][x+dx[i]] == 1:
                        new_lst.append([y, x])
        res_lst.append(new_lst)

    result = 0
    for i in range(2):
        res = res_lst[i]
        for j in range(len(res)):
            y = res[j][0]
            x = res[j][1]
            cnt = 1
            while True:
                x += dx[i]
                y += dy[i]
                if not is_wall(y, x):
                    break
                if total_map[y][x] == 0:
                    break
                cnt += 1

            if cnt == K:
                result += 1

    print('#{} {}'.format(testcase, result))