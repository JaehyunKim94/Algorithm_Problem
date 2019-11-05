TC=int(input())
for testcase in range(1, TC+1):
    n=int(input())
    v=0
    d=0
    for i in range(n):
        list_a=list(map(int, input().split()))
        if len(list_a)==1:
            c=list_a[0]
            d+=v

        else:
            c=list_a[0]
            a=list_a[1]

            if c==1:
                v+=a
                d+=v
            elif c==2:
                v-=a
                if v<0:
                    v=0
                d+=v

    print('#{} {}'.format(testcase, d))