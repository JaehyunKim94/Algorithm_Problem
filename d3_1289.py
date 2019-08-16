def otoz(st_in):
    new_str=''
    cnt=0
    for char in st_in:
        new_str+=char+' '
    st_list=list(map(int, new_str.split()))
    st_len=len(st_list)

    for i in range(st_len):
        if st_list[i]==1:
            for j in range(i, st_len):
                if st_list[j]==1:
                    st_list[j]=0
                elif st_list[j]==0:
                    st_list[j]=1
            cnt+=1

    return cnt


TC=int(input())
for testcase in range(1, TC+1):
    st_in=input()
    result=otoz(st_in)
    print('#{} {}'.format(testcase, result))
    
