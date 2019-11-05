TC=int(input())
for testcase in range(1, TC+1):
    n=int(input())
    lst_num=list(map(int, input().split()))
    up_max=0
    down_max=0
    calc_down=0
    calc_up=0

    for i in range(1, n):
        j=i-1   
        if lst_num[i] > lst_num[j]:
            calc_up=lst_num[i]-lst_num[j]
        elif lst_num[i] < lst_num[j]:
            calc_down=lst_num[j]-lst_num[i]

        if calc_down>down_max:
            down_max=calc_down
        if calc_up>up_max:
            up_max=calc_up
    print('#{} {} {}'.format(testcase, up_max, down_max))