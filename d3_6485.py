TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [0 for i in range(5001)]
    for __ in range(N):
        new_lst = list(map(int, input().split()))
        for i in range(new_lst[0], new_lst[1]+1):
            total_map[i] += 1

    P = int(input())
    print('#{}'.format(testcase), end=' ')
    for j in range(P):
        print(total_map[int(input())], end=' ')

    print()