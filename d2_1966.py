TC=int(input())
for testcase in range(1, TC+1):
    n=int(input())
    a_list=list(map(int, input().split()))
    new_str=''
    a_list=sorted(a_list)
    print(a_list)
    for a in a_list:
        new_str += '{} '.format(str(a))
    print('#{} {}'.format(testcase, new_str))