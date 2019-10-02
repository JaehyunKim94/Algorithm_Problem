import sys
sys.stdin = open('d4_1861.txt', 'r')


def is_next(ap, bp):
    rr = abs(ap[0] - bp[0]) + abs(ap[1] - bp[1])
    if rr == 1:
        return True


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    num_dic = dict()
    for y in range(N):
        for x in range(N):
            num_dic.update({total_map[y][x]: (y, x)})

    pos_lst = []
    num = 0
    for k in num_dic.keys():
        if k+1 in num_dic.keys():
            if is_next(num_dic[k], num_dic[k+1]):
                pos_lst.append(k)
                num += 1
    pos_lst.sort()      # 제출 할 때 sort 안하니까 안되더라는
    idx = 0
    result = [0, 0]
    while idx < num:
        if idx == 0:
            new_p = [pos_lst[0], 1]
        else:
            if new_p[0] + new_p[1] == pos_lst[idx]:
                new_p[1] += 1
            else:
                if new_p[1] > result[1]:
                    result = new_p
                new_p = [pos_lst[idx], 1]
        idx += 1

    if new_p[1] > result[1]:
        result = new_p

    print('#{} {} {}'.format(testcase, result[0], result[1] + 1))