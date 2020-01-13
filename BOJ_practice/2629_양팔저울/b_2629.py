import sys
sys.stdin = open('b_2629.txt', 'r')

N = int(input())
sinker = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))
res_set = {0}
idx = -1
while idx < N-1:
    idx += 1
    concat_set = set()
    for res in res_set:
        for cal in (-sinker[idx], sinker[idx]):
            new = res + cal
            concat_set.add(new)
    res_set = res_set | concat_set

yes_or_no = ['N'] * M
for idx in range(M):
    if check[idx] in res_set:
        yes_or_no[idx] = 'Y'

print(' '.join(yes_or_no))