import sys
sys.stdin = open('15686.txt', 'r')


def solve(k):
    if k == chicken:
        if sum(visit) == M:
            mak_lst = []
            for i in range(1, chicken+1):
                if visit[i] == 1:
                    mak_lst.append(chi_lst[i-1])
            bubun_lst.append(mak_lst)
        return
    else:
        k += 1
        visit[k] = 1
        solve(k)
        visit[k] = 0
        solve(k)

def my_cal(ay, ax, by, bx):
    return abs(ay-by) + abs(ax-bx)



def get_dist():
    res_lst = []
    for home in home_lst:
        dis = []
        for nene in bubun:
            d = my_cal(home[0], home[1], nene[0], nene[1])
            dis.append(d)
        res_lst.append(min(dis))
    return sum(res_lst)


N, M = map(int, input().split())
total_map = []
for i in range(N):
    new_lst = list(map(int, input().split()))
    total_map.append(new_lst)

chi_lst = []
home_lst = []
for y in range(N):
    for x in range(N):
        if total_map[y][x] == 2:
            chi_lst.append([y, x])
        if total_map[y][x] == 1:
            home_lst.append([y, x])


bubun_lst = []
chicken = len(chi_lst)
visit = [0] * (chicken + 1)
solve(0)

res_lst = []
for bubun in bubun_lst:
    res_lst.append(get_dist())
print(min(res_lst))

