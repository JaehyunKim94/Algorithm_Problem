import sys
sys.stdin = open('d2_5174.txt', 'r')


def find_sub(k):
    global cnt
    cnt += 1
    for i in range(0, 2 * E, 2):
        if node_lst[i] == k:
            find_sub(node_lst[i+1])


TC = int(input())
for testcase in range(1, TC+1):
    E, N = map(int, input().split())
    node_lst = list(map(int, input().split()))
    cnt = 0
    find_sub(N)
    print('#{} {}'.format(testcase, cnt))
