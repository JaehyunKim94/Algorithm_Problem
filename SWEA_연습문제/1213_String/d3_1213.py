TC=10
for testcase in range(1, TC+1):
    test=input()
    st_check=str(input())
    st_in=str(input())
    cnt=0
    in_len = len(st_in)
    ch_len = len(st_check)
    for i in range(in_len-ch_len+1):
        cnt_k=0
        if st_in[i]==st_check[0]:
            for j in range(ch_len):
                if st_in[i+j]==st_check[j]:
                    cnt_k+=1
            if cnt_k==ch_len:
                cnt+=1
    print('#{} {}'.format(testcase, cnt))