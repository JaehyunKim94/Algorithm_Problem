import sys
sys.stdin = open('d4_1862.txt', 'r')


def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True


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
    idx = 0
    result = (pos_lst[0], 1)
    new_p = (pos_lst[0], 1)
    while idx < num:
        if pos_lst[idx] + 1 == pos_lst[idx+1]:


    print(testcase, pos_lst)