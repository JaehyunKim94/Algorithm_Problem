TC=int(input())

for testcase in range(1, TC+1):
    list_a=list(map(int, input().split()))
    ex_min=list_a[0]
    ex_max=list_a[1]
    ex_now=list_a[2]

    result=-1
    if ex_now<ex_min:
        result=ex_min-ex_now
    elif ex_now>=ex_min and ex_now<=ex_max:
        result=0
    
    print('#{} {}'.format(testcase, result))