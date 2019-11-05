def encryption(list_a):
    num=1
    new_num=0
    while list_a[7]!=0:
        if num>5:
            num=1

        list_a[0]-=num
        new_num = list_a.pop(0)
        if new_num<1:
            new_num=0
        list_a.append(new_num)
        
        num+=1
    return list_a

TC=10

for testcase in range(1, TC+1):
    test=int(input())
    list_a=list(map(int, input().split()))
    result=''
    lst_result=encryption(list_a)
    for number in lst_result:
        result+=str(number)+' '

    print('#{} {}'.format(testcase,result))
