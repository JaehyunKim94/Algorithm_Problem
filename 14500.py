import sys
sys.stdin = open('14500.txt', 'r')


import copy


def get_tri(y, x):
    dif = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for i in range(4):
        aa = total_map[y][x]
        for j in range(4):
            yy = y + dif[j][0]
            xx = x + dif[j][1]
            if 0 <= yy < N and 0 <= xx < M:
                if i != j:
                    aa += total_map[yy][xx]
            else:
                break
        result = max(result, aa)


res_lst = []
N, M = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
result = 0
for y in range(N):
    for x in range(M):
        get_tri(y, x)
for res in res_lst:
    rr = 0
    for i in range(4):
        rr += total_map[res[i][0]][res[i][1]]
    result = max(rr, result)
print(result)