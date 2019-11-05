import sys
sys.stdin = open('d2_5186.txt', 'r')

def is_pos(n):
    dif = 1
    result = ''
    for _ in range(12):
        dif = dif/2
        if n >= dif:
            n -= dif
            result += '1'
        else:
            result += '0'
        if n == 0:
            return result

    return 'overflow'


TC = int(input())
for testcase in range(1, TC+1):
    n = float(input())
    print('#{} {}'.format(testcase, is_pos(n)))
