TC=int(input())
for testcase in range(1, TC+1):
    n=input()
    result=('1/'+n+' ')*int(n)
    print('#{} {}'.format(testcase, result))