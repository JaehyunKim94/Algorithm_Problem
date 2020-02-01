import sys
sys.stdin = open('d3_5178.txt', 'r')


def solve(k):
    if node_lst[k] == '':
        idx_b = (2*k)
        if node_lst[idx_b] == '':
            node_lst[idx_b] = solve(idx_b)

        idx_a = (2 * k) + 1
        if idx_a > N:
            return node_lst[idx_b]
        if node_lst[idx_a] == '':
            node_lst[idx_a] = solve(idx_a)
        node_lst[k] = node_lst[idx_a] + node_lst[idx_b]
    return node_lst[k]


TC = int(input())
for testcase in range(1, TC+1):
    N, M, L = map(int, input().split())
    node_lst = ['' for i in range(N+1)]
    for _ in range(M):
        idx, num = map(int, input().split())
        node_lst[idx] = num
    solve(1)
    print('#{} {}'.format(testcase, node_lst[L]))