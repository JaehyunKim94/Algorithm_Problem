import sys
sys.stdin = open('b_2302.txt', 'r')

# def get_res(num):
#     global res_lst
#     if num == 0:
#         return 1
#     elif num == 1:
#         return 1
#     else:
#         return res_lst[num-1] + res_lst[num-2]

N = int(input())
M = int(input())
holding = [int(input()) for _ in range(M)]

res_lst = [1 for i in range(41)]
for idx in range(2, 41):
    res_lst[idx] = res_lst[idx-1] + res_lst[idx-2]

sp = 0
result = 1
for ep in holding:
    length = ep - sp - 1
    result *= res_lst[length]
    sp = ep
last = N - sp
result *= res_lst[last]
print(result)