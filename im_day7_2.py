import sys
sys.stdin = open('im_day7_2.txt', 'r')


TC = int(input())
for testcase in range(1, TC+1):
    N, M = map(int, input().split())
    total_map = [0 for _ in range(N*M)]
    ck = 0
    for _ in range(M):
        new_lst = list(map(int, input().split()))
        pk = ck
        if _ == 0:
            for i in range(N):
                total_map[i] = new_lst[i]
        else:
            com_num = new_lst[0]
            for i in range(ck):
                if total_map[i] > com_num:
                    pk = i
                    break

            for i in range(ck+N-1, pk+N-1, -1):
                total_map[i] = total_map[i-N]

            for j in range(N):
                total_map[pk+j] = new_lst[j]

        ck += N

    print('#{} '.format(testcase), end='')
    for i in range(-1, -11, -1):
        print('{}'.format(total_map[i]), end=' ')
    print()
