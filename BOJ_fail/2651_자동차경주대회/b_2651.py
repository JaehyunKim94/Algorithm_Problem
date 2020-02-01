import sys
sys.stdin = open('b_2651.txt', 'r')

def solve():
    que = [(limit, 0, [])]
    idx = 0
    while idx < station_cnt:
        nxt_que = list()
        for d, t, l in que:
            d -= distance[idx]
            if d >= 0:
                if d >= distance[idx+1]:
                    nxt_que.append((d, t, l))
                new_l = l[:]
                new_l.append(idx)
                nxt_que.append((limit, t+time[idx], new_l))
        idx += 1
        que = nxt_que

    min_time = 999999
    min_lst = []
    for d, t, l in que:
        if d >= distance[station_cnt]:
            if t < min_time:
                min_time = t
                min_lst = l
    return min_time, min_lst


limit = int(input())
station_cnt = int(input())
distance = list(map(int, input().split()))
time = list(map(int, input().split()))

res_t, res_l = solve()
print(res_t)
print(len(res_l))
for r in res_l:
    print(r+1, end=' ')