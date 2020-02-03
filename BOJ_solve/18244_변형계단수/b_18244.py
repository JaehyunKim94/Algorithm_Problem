import sys
sys.stdin = open('b_18244.txt', 'r')


N = int(input())
if N == 1:
    result = 10
else:
    N -= 1
    result = 0
    cnt_dict = [[0]*4 for _ in range(10)]
    for i in range(10):
        if i > 0:
            cnt_dict[i][2] += 1
        if i < 9:
            cnt_dict[i][1] += 1
    for k in range(N-1):
        new_dict = [[0]*4 for _ in range(10)]
        for i in range(10):
            if i < 9:
                new_dict[i+1][2] = cnt_dict[i][1] + cnt_dict[i][0]
                new_dict[i+1][3] = cnt_dict[i][2]
            if i > 0:
                new_dict[i-1][1] = cnt_dict[i][2] + cnt_dict[i][3]
                new_dict[i-1][0] = cnt_dict[i][1]
        cnt_dict = new_dict
    result = sum(sum(cnt_dict, [])) % 1000000007
print(result)