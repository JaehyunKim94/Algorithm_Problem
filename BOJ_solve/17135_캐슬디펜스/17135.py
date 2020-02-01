import sys
sys.stdin = open('17135.txt', 'r')

import copy

def get_dis(ap, bp):
    return abs(ap[0] - bp[0]) + abs(ap[1] - bp[1])

def solve(la, lb, lc, enm):
    global result
    res = 0
    visit = [0] * e_cnt
    d = D
    while sum(visit) != e_cnt:
        idx_set = set()
        # 공격
        for a in la:
            if a[0] <= d and not visit[a[1]]:
                idx_set.add(a[1])
                break
        for b in lb:
            if b[0] <= d and not visit[b[1]]:
                idx_set.add(b[1])
                break
        for c in lc:
            if c[0] <= d and not visit[c[1]]:
                idx_set.add(c[1])
                break

        for idx in idx_set:
            if visit[idx] == 0:
                visit[idx] = 1
                res += 1

        for ii in range(e_cnt):
            if visit[ii] == 0:
                enm[ii][0] += 1
                new_dis = enm[ii][0]
                if new_dis >= N:
                    visit[ii] = 1
        d += 1
    result = max(result, res)

N, M, D = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]

# 적들의 위치를 리스트로 저장후, x축을 기준으로 정렬
ori_enemy = []
e_cnt = 0
for y in range(N):
    for x in range(M):
        if total_map[y][x] == 1:
            ori_enemy.append([y, x])
            e_cnt += 1
ori_enemy.sort(key=lambda el: el[1])

# 궁수의 위치에 따른 적들의 거리 리스트
dis_lst = [0] * M
for x in range(M):
    new_lst = []
    bp = (N, x)
    for i in range(e_cnt):
        e = ori_enemy[i]
        new_lst.append((get_dis(e, bp), i))
    new_lst.sort()
    dis_lst[x] = new_lst

# M개의 열에서 3개를 정해 정답 탐색
result = 0
for a in range(M-2):
    l_a = dis_lst[a][:]
    for b in range(a+1, M-1):
        l_b = dis_lst[b][:]
        for c in range(b+1, M):
            l_c = dis_lst[c][:]
            enemy = copy.deepcopy(ori_enemy)
            solve(l_a, l_b, l_c, enemy)
print(result)