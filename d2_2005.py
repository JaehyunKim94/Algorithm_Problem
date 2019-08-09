def my_pascal(pascal_list):
    new_pascal=list()
    new_list=list()

    if len(pascal_list)==0:
        pascal_list.append(int(1))
        return pascal_list
    else:
        new_list=pascal_list
        new_list.append(int(0))
        new_list.insert(0, int(0))
        
        for k in range(len(new_list)-1):
            new_k=new_list[k]+new_list[k+1]
            new_pascal.append(new_k)
        return new_pascal

TC=int(input())

for testcase in range(1, TC+1):
    n=int(input())

    pascal_list=[]
    print('#{}'.format(testcase))
    for i in range(n):
        pascal_str=''
        pascal_list=my_pascal(pascal_list)
        for j in pascal_list:
            pascal_str += '{} '.format(j)
        print(pascal_str)