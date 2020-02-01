TC=int(input())

for testcase in range(1, TC+1):
    ob_list=list(map(int, input().split()))
    n, m=ob_list[0], ob_list[1]

    fly_list=list()
    for i in range(n):
        new_info=list(map(int, input().split()))
        fly_list.append(new_info)

    sum_bef=0
    sum_now=0
    for y in range(0, n-m+1):
        for x in range(0, n-m+1):
            for j in range(m):
                for i in range(m):
                    sum_now+=fly_list[x+i][y+j]

            if sum_now>sum_bef:
                sum_bef=sum_now
            sum_now=0
    print('#{} {}'.format(testcase, sum_bef))


