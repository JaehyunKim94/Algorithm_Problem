TC=10

for testcase in range(1, TC+1):
    test=int(input())
    list_a=list(map(int, input().split()))
    num1=list_a[0]
    num2=list_a[1]
    result=num1**num2
    print('#{} {}'.format(test, result))