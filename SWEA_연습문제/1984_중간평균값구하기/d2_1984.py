TC= int(input())

for testcase in range(1, TC+1):
    list_a=list(map(int, input().split()))
    list_a=sorted(list_a)
    del_a=list_a.pop(0)
    del_a=list_a.pop(-1)
    sum_a=sum(list_a)
    result=round(sum_a/len(list_a))
    print('#{} {}'.format(testcase, result))