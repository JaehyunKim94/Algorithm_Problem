import sys
sys.stdin = open('d2_5177.txt', 'r')

# 실패.. 
def solve(k):
    if len(arr_sub[k]) > 0:
        sub_min = num_lst[k]
        sub_idx = k
        for sub in arr_sub[k]:
            if num_lst[sub] < sub_min:
                sub_min = num_lst[sub]
                sub_idx = sub
        num_lst[sub_idx], num_lst[k] = num_lst[k], num_lst[sub_idx]
        for sub in arr_sub[k]:
            solve(sub)


def get_ans(k):
    global result
    if k > 0:
        result += num_lst[k]
        get_ans(k//2)


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    num_lst.insert(0, -1)
    arr_sub = [[] for _ in range(N+1)]
    for ar in range(1, N+1):
        a = ar*2
        b = a + 1
        if a <= N:
            arr_sub[ar].append(a)
        if b <= N:
            arr_sub[ar].append(b)
    solve(1)
    result = 0
    get_ans(N//2)
    print(num_lst)
    print('#{} {}'.format(testcase, result))
