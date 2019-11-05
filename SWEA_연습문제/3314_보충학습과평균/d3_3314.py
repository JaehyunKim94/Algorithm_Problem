TC=int(input())
for testcase in range(1, TC+1):
    list_a=list(map(int, input().split()))

    my_sum=0
    for a in list_a:
        if a<40:
            a=40
        my_sum+=a
    result=int(my_sum/5)

    print('#{} {}'.format(testcase, result))