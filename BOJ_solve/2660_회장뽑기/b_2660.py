import sys
sys.stdin = open('b_2660.txt', 'r')

def get_distance(y, x):
    que = [y]
    visit = [0] * N
    visit[y] = 1
    distance = 0
    while que:
        distance += 1
        for _ in range(len(que)):
            nxt = que.pop(0)
            for idx in range(N):
                if point_map[nxt][idx] == 1 and visit[idx] == 0:
                    visit[idx] = 1
                    if idx == x:
                        return distance
                    else:
                        que.append(idx)


N = int(input())
point_map = [[0]*N for _ in range(N)]
relation = []
while True:
    new_info = input()
    if new_info == '-1 -1':
        break
    else:
        a, b = map(int, new_info.split())
        a -= 1
        b -= 1
        point_map[a][b] = 1
        point_map[b][a] = 1

for y in range(N):
    for x in range(N):
        if y != x and point_map[y][x] == 0:
            dis = get_distance(y, x)
            point_map[y][x] = dis
            point_map[x][y] = dis

point_lst = [0] * N
for y in range(N):
    point_lst[y] = max(point_map[y])

res_point = min(point_lst)
res_cnt = 0
res_lst = []

for idx in range(N):
    if point_lst[idx] == res_point:
        res_lst.append(idx+1)
        res_cnt += 1

print(res_point, res_cnt)
for res in res_lst:
    print(res, end=' ')