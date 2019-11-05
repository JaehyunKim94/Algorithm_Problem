num=int(input())
lst_369=[3, 6, 9]
result=''
for i in range(1, num+1):
    num_len=len(str(i))
    cnt_369=0
    next_i=i
    for j in range(num_len):
        check_i=next_i%10
        if check_i in lst_369:
            cnt_369+=1
        next_i=next_i//10
    
    if cnt_369>0:
        result+='-'*cnt_369
    else:
        result+=str(i)
    result+=' '
print(result)