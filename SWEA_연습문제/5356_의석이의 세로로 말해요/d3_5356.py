import sys
sys.stdin = open('d3_5356.txt', 'r')

TC = int(input())
for testcase in range(1, TC+1):
    tot_map = []
    ma_len = 0
    for _ in range(5):
        new_lst = input()
        if len(new_lst) > ma_len:
            ma_len = len(new_lst)
        tot_map.append(new_lst)

    new_txt = ''
    for i in range(ma_len):
        for j in range(5):
            if i in range(len(tot_map[j])):
                new_txt += tot_map[j][i]
    print('#{} {}'.format(testcase, new_txt))