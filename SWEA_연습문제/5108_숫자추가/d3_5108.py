import sys
sys.stdin = open('d3_5108.txt', 'r')

TC = int(input())
for testcase in range(1, TC+1):
    N, M, L = map(int, input().split())
    num_lst = list(map(int, input().split()))
    for _ in range(M):
        pk, num = map(int, input().split())
        num_lst.insert(pk, num)
    print('#{} {}'.format(testcase, num_lst[L]))