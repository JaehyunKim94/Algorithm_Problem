import sys
sys.stdin = open('d5_1242.txt', 'r')

ck_lst = ['3211', '2221', '2122', '1411', '1132', '1231', '1114', '1312', '1213', '3112']
ck_dic = {ck_lst[i]: i for i in range(10)}


def get_hex(k):
    if k == 4:
        new_hexa = ''
        for i in range(1, 5):
            new_hexa += str(visit[i])
        hex_lst.append(new_hexa)
        return

    else:
        k += 1
        visit[k] = 0
        get_hex(k)
        visit[k] = 1
        get_hex(k)


def cnt_sli(new, x):
    global k
    tg = new[x-k+1:x+1]
    div = k//7
    st = tg[0]
    cnt = 0
    new_st = ''
    if st == '0':
        for i in range(k):
            if tg[i] == st:
                cnt += 1
            else:
                st = tg[i]
                new_st += str(cnt//div)
                cnt = 1
        new_st += str(cnt//div)
        if new_st in ck_lst:
            return
        else:
            k += 7
            cnt_sli(new, x)
    else:
        k+=7
        cnt_sli(new, x)


def solve(target_num, k):
    anum = []
    for i in range(0, k*8, k):
        tgn = target_num[i:i+k]
        st = '0'
        cnt = 0
        kcc = ''
        div = k//7
        for j in range(k):
            if tgn[j] == st:
                cnt += 1
            else:
                kcc += str(cnt//div)
                st = tgn[j]
                cnt = 1
        kcc += str(cnt//div)
        anum.append(ck_dic[kcc])

    num1 = sum(anum[::2]) * 3
    num2 = sum(anum[1:7:2])
    num3 = anum[7]
    if (num1 + num2 + num3) % 10 == 0:
        if anum not in lst_res:
            lst_res.append(anum)
            result.append(sum(anum))


visit = [0 for _ in range(5)]
hex_lst = []
get_hex(0)
ori_lst = ['' for _ in range(16)]
for i in range(10):
    ori_lst[i] = str(i)
ap_lst = ['A', 'B', 'C', 'D', 'E', 'F']
for i in range(6):
    ori_lst[10+i] = ap_lst[i]

hex_dic = {ori_lst[i]: hex_lst[i] for i in range(16)}

TC = int(input())
for testcase in range(1, TC+1):
    total_set = set()
    new_map = []
    N, M = map(int, input().split())
    new_n = 0
    for _ in range(N):
        new_in = input()
        if new_in not in total_set:
            total_set.add(new_in)
            new_n += 1
            new_st = ''
            for kk in range(M):
                new_st += hex_dic[new_in[kk]]
            if new_st not in new_map:
                new_map.append(new_st)

    result = []
    lst_res = []
    for new in new_map:
        x = M*4
        while x >= 0:
            x -= 1
            if new[x] == '1':
                k = 7
                cnt_sli(new, x)
                target_num = new[x-(k*8)+1:x+1]
                solve(target_num, k)
                x -= (k*8)-1

    print('#{} {}'.format(testcase, sum(result)))