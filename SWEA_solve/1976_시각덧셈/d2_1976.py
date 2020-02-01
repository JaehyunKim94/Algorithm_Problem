TC = int(input())

for testcase in range(1, TC+1):
    list_a=list(map(int, input().split()))

    result_h=list_a[0] + list_a[2]
    result_m=list_a[1] + list_a[3]

    if result_m>=60:
        result_m-=60
        result_h+=1
    if result_h>12:
        result_h-=12

    print('#{} {} {}'.format(testcase, result_h, result_m))