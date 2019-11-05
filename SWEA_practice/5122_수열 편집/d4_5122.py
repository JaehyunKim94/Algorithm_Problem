import sys
sys.stdin = open('d4_5122.txt', 'r')


def rara():
    tg_num = int(new_lst[1])
    if new_lst[0] == 'D':
        for i in range(tg_num, N+M-1, 1):
            num_lst[i] = num_lst[i+1]
    if new_lst[0] == 'I':
        for i in range(N+M-2, tg_num-1, -1):
            num_lst[i+1] = num_lst[i]
        num_lst[tg_num] = int(new_lst[2])
    if new_lst[0] == 'C':
        num_lst[tg_num] = int(new_lst[2])


TC = int(input())
for testcase in range(1, TC+1):
    N, M, L = map(int, input().split())
    num_lst = [0 for _ in range(N+M)]
    num_lst[:N] = map(int, input().split())
    for __ in range(M):
        new_lst = input().split()
        rara()
    if num_lst[L] == 0:
        result = -1
    else:
        result = num_lst[L]
    print('#{} {}'.format(testcase, result))