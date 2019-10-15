import sys
sys.stdin = open('b_17472.txt', 'r')


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False


def change_map(y, x, num):
    global visit
    total_map[y][x] = num
    visit.append((y, x))
    for dif in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yy = y + dif[0]
        xx = x + dif[1]
        if is_inbox(yy, xx):
            if (yy, xx) not in visit and total_map[yy][xx] == 1:
                change_map(yy, xx, num)


def find_island(y, x, dif, num, cnt):
    global link_lst
    yy = y + dif[0]
    xx = x + dif[1]
    if is_inbox(yy, xx):
        nxt = total_map[yy][xx]
        if nxt == num:
            return
        elif nxt == 0:
            find_island(yy, xx, dif, num, cnt+1)
        else:
            if cnt > 1:
                dis_map[nxt][num] = min(dis_map[nxt][num], cnt)
                dis_map[num][nxt] = dis_map[nxt][num]
                num, nxt = min(num, nxt), max(num, nxt)
                new_link = (num, nxt)
                if new_link not in link_lst:
                    link_lst.append(new_link)
                return


def is_good(lst, ck_set, cnt):
    for i in range(cnt):
        for j in range(2):
            if lst[i][j] in ck_set:
                if lst[i][1-j] not in ck_set:
                    ck_set.add(lst[i][1-j])
                    is_good(lst, ck_set, cnt)


def solve(k, bri, cnt, bri_lst):
    global result
    if k == L-1:
        if cnt == num-2:
            b_lst = list(bri_lst)
            ck_set = set(b_lst[0])
            is_good(b_lst, ck_set, cnt)
            if ck_set == ck_lst:
                result = min(result, bri)

    else:
        k += 1
        bri_lst.append(link_lst[k])
        solve(k, bri+dis_map[link_lst[k][0]][link_lst[k][1]], cnt+1, bri_lst)
        bri_lst.pop()
        solve(k, bri, cnt, bri_lst)


N, M = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
num = 1
visit = []
for y in range(N):
    for x in range(M):
        if total_map[y][x] == 1 and (y, x) not in visit:
            change_map(y, x, num)
            num += 1

dis_map = [[99 for i in range(num)] for j in range(num)]
link_lst = []
for y in range(N):
    for x in range(M):
        if total_map[y][x] != 0:
            for dif in [(0, 1), (1, 0)]:
                find_island(y, x, dif, total_map[y][x], 0)

result = 100
L = len(link_lst)
ck_lst = {i for i in range(1, num)}
solve(-1, 0, 0, [])
if result == 100:
    result = -1
print(result)