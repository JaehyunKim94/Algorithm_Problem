import sys
sys.stdin = open('b_2629.txt', 'r')


    def fillCheckMap(cnt, left_num, right_num):
        global com_set
        global sinkerDic
        res = abs(left_num - right_num)
        com_set.add(res)

        if cnt == N:
            return
        else:
            cnt += 1
            for k in sinkerDic.keys():
                if sinkerDic[k] > 0:
                    for l, r in [(left_num, right_num), (left_num+k, right_num), (left_num, right_num+k)]:
                        sinkerDic[k] -= 1
                        fillCheckMap(cnt, l, r)
                        sinkerDic[k] += 1


    N = int(input())
    sinkerDic = dict()
    sinker = list(map(int, input().split()))
    M = int(input())
    check = list(map(int, input().split()))
    com_set = set()
    for sin in sinker:
        if sin in sinkerDic.keys():
            sinkerDic[sin] += 1
        else:
            sinkerDic[sin] = 1
    fillCheckMap(0, 0, 0)
    res_lst = ['N']*M
    for idx in range(M):
        if check[idx] in com_set:
            res_lst[idx] = 'Y'

    print(' '.join(res_lst))