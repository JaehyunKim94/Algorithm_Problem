import sys
sys.stdin = open('d4_5120.txt', 'r')

TC = int(input())
for testcase in  range(1, TC+1):
    N, M, K = map(int, input().split())
    total_map = [0 for _ in range(N+K)]

    num_lst = list(map(int, input().split()))
    for i in range(N):
        total_map[i] = num_lst[i]

    malen = N
    now_p = 0
    for _ in range(K):
        now_p += M
        if now_p > malen:
            now_p -= malen

        for i in range(malen, now_p, -1):
            total_map[i] = total_map[i-1]
        bn = now_p-1
        if bn < 0:
            bn = malen
        an = now_p+1
        if an > malen:
            an = 0
        total_map[now_p] = total_map[bn] + total_map[an]

        malen += 1
    print('#{} '.format(testcase), end='')

    for kk in range(10):
        malen -= 1
        if malen < 0:
            break
        print(total_map.pop(malen), end = ' ')
    print()
