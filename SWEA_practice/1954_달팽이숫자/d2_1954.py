TC=int(input())
for testcase in range(1, TC+1):
    n=int(input())
    new_list=[[0 for j in range(n)] for i in range(n)]


    x=0
    y=0
    new_num=1
    tg_num=n
    check_pm=1

    while tg_num>0:
        if tg_num==n:
            new_list[y][x]=new_num
            for i in range(tg_num-1): 
                x+=check_pm 
                new_num+=1
                new_list[y][x]=new_num
                

        else:
            for i in range(tg_num):
                new_num+=1
                y+=check_pm
                new_list[y][x]=new_num
                
            
            check_pm=-check_pm

            for i in range(tg_num):
                new_num+=1
                x+=check_pm
                new_list[y][x]=new_num
                
        tg_num-=1
    
    print('#{}'.format(testcase))

    for result_str in new_list:
        result=''
        for new_char in result_str:
            result+=str(new_char)
            result+=' '
        print(result)