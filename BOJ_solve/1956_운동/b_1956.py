import sys
sys.stdin = open('b_1956.txt', 'r')


def goRun(now_point, distance, target):
    global res, ck, visit
    for idx in range(V):
        dis = total_map[now_point][idx]
        if dis and distance + dis < res:
            if not visit[idx]:
                visit[idx] = 1
                goRun(idx, distance+dis, target)
                visit[idx] = 0
            else:
                if idx == target:
                    ck = False
                    res = min(res, distance+dis)

V, E = map(int, input().split())
total_map = [[0] * V for _ in range(V)]
for _ in range(E):
    fr, to, dis = map(int, input().split())
    total_map[fr-1][to-1] = dis

res = 99999999
ck = True
visit = [0] * V
for i in range(V):
    start_point = i
    visit[i] = 1
    goRun(start_point, 0, start_point)
    visit[i] = 0

if ck:
    res = -1
print(res)