import sys
sys.stdin = open('d4_4366.txt', 'r')


def change_num(num, k):
    result = 0
    ran = len(num)
    j = ran-1
    for i in range(ran):
        result += int(num[i]) * k ** (j-i)
    return result


TC = int(input())
for testcase in range(1, TC+1):
    num1 = input()
    num2 = input()

    a_lst = []
    for i in range(len(num1)):
        a_case = ''
        if num1[i] == '1':
            a_case = num1[:i] + '0' + num1[i+1:]
        else:
            a_case = num1[:i] + '1' + num1[i+1:]
        a_lst.append(change_num(a_case, 2))

    b_lst = []
    ck_lst = ['0', '1', '2']
    for i in range(len(num2)):
        b_case = ''
        if num2[i] == '0':
            for k in ('1', '2'):
                b_case = num2[:i] + k + num2[i+1:]
                b_lst.append(change_num(b_case, 3))
        if num2[i] == '1':
            for k in ('0', '2'):
                b_case = num2[:i] + k + num2[i + 1:]
                b_lst.append(change_num(b_case, 3))
        if num2[i] == '2':
            for k in ('0', '1'):
                b_case = num2[:i] + k + num2[i + 1:]
                b_lst.append(change_num(b_case, 3))

    for a in a_lst:
        if a in b_lst:
            print('#{} {}'.format(testcase, a))
            break