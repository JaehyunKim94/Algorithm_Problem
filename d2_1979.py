def cnt_k(tg_list, n, k):
    
    len_k=0
    cnt=0
    for tg in tg_list:
        check_1=0
        for j in range(n):
            if j==0:
                check_1=tg[0]
                if check_1==1:
                    len_k=1

            else:
                if check_1==1 and tg[j]==1:
                    len_k+=1

                elif check_1==1 and tg[j]==0:
                    if len_k==k:
                        cnt+=1
                    len_k=0

                elif check_1==0 and tg[j]==1:
                    len_k=1
                
                check_1=tg[j]

                if j==n-1:
                    if len_k==k:
                        cnt+=1
    return cnt

TC = int(input())
for testcase in range(1, TC+1):
    list_a=list(map(int, input().split()))
    n=list_a[0]
    k=list_a[1]

    x_list=list()
    y_list=[[0]*n for i in range(n)]

    cnt=0

    # x_list=퍼즐 모양
    for i in range(n):
        list_b=list(map(int, input().split()))
        x_list.append(list_b)

    # x,y 대칭 후 y_list에 저장
    for i in range(n):
        for j in range(n):
            y_list[j][i]=x_list[i][j]
    
    result_1=cnt_k(x_list, n, k)
    result_2=cnt_k(y_list, n, k)
    result=result_1+result_2

    print('#{} {}'.format(testcase, result))
