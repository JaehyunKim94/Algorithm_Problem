import sys
sys.stdin = open('d2_5185.txt', 'r')


def get_hex(k):
    if k == 4:
        new_str = ''
        for i in range(1, 5):
            new_str += str(visit[i])
        two_lst.append(new_str)
        return
    else:
        k += 1
        visit[k] = 0
        get_hex(k)
        visit[k] = 1
        get_hex(k)


visit = [0 for _ in range(5)]
two_lst = []
get_hex(0)
hex_lst = ['' for _ in range(16)]
al_lst = ['A', 'B', 'C', 'D', 'E', 'F']
for i in range(16):
    if i < 10:
        hex_lst[i] = str(i)
    else:
        hex_lst[i] = al_lst[i-10]

hex_dic = {hex_lst[i]: two_lst[i] for i in range(16)}

def hextwo(st):
    new_str = ''
    for s in st:
        new_str += hex_dic[s]
    return new_str



TC = int(input())
for testcase in range(1, TC+1):
    n, st = input().split()
    result = hextwo(st)
    print('#{} {}'.format(testcase, result))
