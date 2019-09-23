import sys
sys.stdin = open('sw_5658.txt', 'r')

hex_dic = {'A': 10,
           'B': 11,
           'C': 12,
           'D': 13,
           'E': 14,
           'F': 15}


def hextwo(num):
    rr = len(num)
    new_num = 0
    he = 1
    for i in range(rr-1, -1, -1):
        if num[i] in hex_dic.keys():
            new_num += he * hex_dic[num[i]]
        else:
            new_num += int(num[i]) * he
        he *= 16
    return new_num


TC = int(input())
for testcase in range(1, TC+1):
    N, K = map(int, input().split())
    num = input()
    num_lst = list()
    ran = N//4
    num += num[:ran]
    que = list()
    
    for i in range(N):
        if num[i:i+ran] not in que:
            que.append(num[i:i+ran])
            new = hextwo(num[i:i+ran])
            num_lst.append(new)

    num_lst.sort(reverse=True)

    print('#{} {}'.format(testcase, num_lst[K-1]))