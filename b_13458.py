import sys
sys.stdin = open('b_13458.txt', 'r')

N = int(input())
people_lst = list(map(int, input().split()))
M, S = map(int, input().split())
result = N
for people in people_lst:
    people -= M
    if people < 0:
        people = 0
    s_num = people // S
    if people%S != 0:
        s_num += 1
    result += s_num
print(result)
