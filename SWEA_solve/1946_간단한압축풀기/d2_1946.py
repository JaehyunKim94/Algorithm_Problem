TC=int(input())

for testcase in range(1, TC+1):
    n=int(input())
    new_str=''
    new_num=0
    for l in range(n):
        lst_in=input().split()
        st_in=lst_in[0]
        st_num=int(lst_in[1])
        new_str+=st_in*st_num
        new_num+=st_num
    
        result=''
    print('#{}'.format(testcase))
    for i in range(new_num):
        result+=new_str[i]
        if len(result)==10:
            print(result)
            result=''
        elif i==new_num-1:
            print(result)
