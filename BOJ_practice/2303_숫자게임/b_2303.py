import sys
sys.stdin = open('b_2303.txt', 'r')

def get_number(lst):
    ret = -1
    for i in range(3):
        a = lst[i]
        for j in range(i+1, 4):
            b = lst[j]
            for k in range(j+1, 5):
                c = lst[k]
                ck = a + b + c
                if ck%10 > ret:
                    ret = ck%10
    return ret

N = int(input())
num_set = [list(map(int, input().split())) for _ in range(N)]
res_first = -1
res_idx = -1
for idx in range(N):
    num_lst = num_set[idx]
    res = get_number(num_lst)
    if res >= res_first:
        res_first = res
        res_idx = idx + 1
print(res_idx)