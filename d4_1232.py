import sys
sys.stdin = open('d4_1232.txt', 'r')


def my_cal(num1, cal, num2):
    num1 = int(num1)
    num2 = int(num2)
    if cal == '+':
        return num1+num2
    elif cal == '-':
        return num1-num2
    elif cal == '*':
        return num1*num2
    elif cal == '/':
        return num1/num2


def find_nxt(p):
    if len(tree_lst[int(p)]) == 2:
        return tree_lst[int(p)][1]
    else:
        l = find_nxt(tree_lst[int(p)][2])
        r = find_nxt(tree_lst[int(p)][3])
        res = my_cal(l, tree_lst[int(p)][1], r)
        return res


TC = 10
for testcase in range(1, TC+1):
    N = int(input())
    tree_lst = [list(input().split()) for _ in range(N)]
    tree_lst.insert(0, [])
    result = find_nxt('1')
    result = int(result)
    print('#{} {}'.format(testcase, result))