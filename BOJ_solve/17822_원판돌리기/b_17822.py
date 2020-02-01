import sys
sys.stdin = open('b_17822.txt')

def isInbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True

def rotate(by, d, k):
    for y in range(N):
        if (y+1)%by == 0:
            tg_lst = total_map[y]
            if d == 0:
                go_front = tg_lst[-k:]
                go_back = tg_lst[:-k]
            else:
                go_back = tg_lst[:k]
                go_front = tg_lst[k:]
            total_map[y] = go_front + go_back

def findNear(y, x):
    for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yy = y + dy
        xx = x + dx
        if xx == -1:
            xx = M-1
        elif xx == M:
            xx = 0

        if isInbox(yy, xx) and total_map[yy][xx] == total_map[y][x]:
            same_set.add((y, x))
            same_set.add((yy, xx))


N, M, T = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
order = [list(map(int, input().split())) for _ in range(T)]
for y, d, k in order:
    rotate(y, d, k)
    same_set = set()
    for y in range(N):
        for x in range(M):
            if total_map[y][x] > 0:
                findNear(y, x)
    if len(same_set) > 0:
        for y, x in same_set:
            total_map[y][x] = 0
    else:
        cnt = 0
        num = 0
        for y in range(N):
            for x in range(M):
                if total_map[y][x] > 0:
                    cnt += 1
                    num += total_map[y][x]
        # 이거 안하니까 80에서 런타임에러.. ㅜㅠ 분모가 0이 될수는 없으니 ㅜㅠ
        if cnt > 0:
            ck = num/cnt
            for y in range(N):
                for x in range(M):
                    if 0 < total_map[y][x] < ck:
                        total_map[y][x] += 1
                    elif total_map[y][x] > ck:
                        total_map[y][x] -= 1
print(sum(sum(total_map, [])))