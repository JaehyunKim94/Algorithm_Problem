import sys
sys.stdin = open('d3_5203.txt', 'r')


def win_ck(di, win):
    global ck
    for k, v in di.items():
        if k < 8:
            if di[k] > 0 and di[k+1] > 0 and di[k+2] > 0:
                ck = win
                return
        if v > 2:
            ck = win
            return


TC = int(input())
for testcase in range(1, TC+1):
    total_map = list(map(int, input().split()))
    a_dic = {i: 0 for i in range(10)}
    b_dic = {i: 0 for i in range(10)}
    ck = 0
    for i in range(12):
        if i & 1:
            b_dic[total_map[i]] += 1
            win_ck(b_dic, 2)
        else:
            a_dic[total_map[i]] += 1
            win_ck(a_dic, 1)

        if ck != 0:
            break
    print('#{} {}'.format(testcase, ck))