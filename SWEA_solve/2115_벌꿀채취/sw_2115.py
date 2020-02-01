import sys
sys.stdin = open('sw_2115.txt', 'r')


def get_com(lst, com, k):
    if k == M-1:
        if len(com) != 0:
            com_lst.append(com)
            return
    else:
        k += 1
        new_com = com[:]
        new_com.append(lst[k])
        get_com(lst, new_com, k)
        get_com(lst, com, k)


def get_money(com):
    new_money = 0
    for i in range(len(com)):
        new_money += com[i]**2
    return new_money


def get_best(com_lst):
    mx_money = 0
    for i in range(len(com_lst)):
        tg = com_lst[i]
        new_money = 0
        if sum(tg) > C:
            continue
        else:
            for j in range(len(tg)):
                new_money += tg[j]**2

        if new_money > mx_money:
            mx_money = new_money
    return mx_money


def solve(a_lst, b_lst):
    global result
    global com_lst
    get_com(a_lst, [], -1)
    a_money = get_best(com_lst)
    com_lst = []
    get_com(b_lst, [], -1)
    b_money = get_best(com_lst)
    res = a_money + b_money
    if res > result:
        result = res


TC = int(input())
for testcase in range(1, TC+1):
    N, M, C = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    sp_lst = []
    ran = 0
    for y in range(N):
        for x in range(0, N-M+1):
            sp_lst.append((y, x))
            ran += 1

    result = 0
    for i in range(ran-1):
        a = sp_lst[i]
        for j in range(i+1, ran):
            b = sp_lst[j]
            if a[0] == b[0] and a[1] + M > b[1]:
                continue
            else:
                com_lst = []
                a_lst = total_map[a[0]][a[1]:a[1]+M]
                b_lst = total_map[b[0]][b[1]:b[1]+M]
                a_lst.sort(reverse=True)
                b_lst.sort(reverse=True)
                solve(a_lst, b_lst)
    print('#{} {}'.format(testcase, result))
