def list_90(make_list,n):
    new_list=list()
    i=0
    for i in range(n):
        new_str=''
        for y in range(n):
            new_str+=make_list[-y-1][i]
        new_list.append(new_str)
    return new_list

def list_180(make_list,n):
    new_list=list()
    i=0
    for y in range(n):
        new_str=''
        for x in range(n):
            new_str+=make_list[-y-1][-x-1]
        new_list.append(new_str)
    return new_list

def list_270(make_list,n):
    new_list=list()
    i=0
    for y in range(n):
        new_str=''
        for x in range(n):
            new_str+=make_list[x][-y-1]
        new_list.append(new_str)
    return new_list

TC = int(input())

for testcase in range(1, TC+1):
    n=int(input())
    make_list=list()
    make_str=''
    for i in range(n):
        list_a=list(input().split())
        make_list.append(list_a)
    list_1=list_90(make_list,n)
    list_2=list_180(make_list, n)
    list_3=list_270(make_list, n)
    
    print('#{} '.format(testcase))
    for i in range(n):
        print('{} {} {}'.format(list_1[i], list_2[i], list_3[i]))