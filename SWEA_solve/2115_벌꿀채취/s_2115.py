import sys
sys.stdin = open('sw_2115.txt', 'r')

import itertools

def getMoney(lst):
    res = 0
    for num in lst:
        res += num*num
    return res

TC = int(input())
for testcase in range(1, TC+1):
    N, M, C = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    com_lst = []
    for y in range(N):
        for x in range(N-M+1):
            tg = total_map[y][x:x+M]
            if sum(tg) <= C:
                money = getMoney(tg)
                com_lst.append((y, x, money))
            else:
                money = 0
                for num in range(1, M):
                    for lst in itertools.combinations(tg, num):
                        if sum(lst) <= C:
                            new_money = getMoney(list(lst))
                            money = max(new_money, money)
                            com_lst.append((y, x, money))
    result = 0
    len_com = len(com_lst)
    for i in range(len_com-1):
        for j in range(i+1, len_com):
            if com_lst[i][0] == com_lst[j][0]:
                if com_lst[i][1]+M <= com_lst[j][1]:
                    res = com_lst[i][2] + com_lst[j][2]
                    result = max(res, result)
            else:
                res = com_lst[i][2] + com_lst[j][2]
                result = max(res, result)
    print('#{} {}'.format(testcase, result))