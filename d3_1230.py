def secret(origin_map, lst_cmd, cnt_cmd):
    for i in range(cnt_cmd):
        if lst_cmd[i]=='I':
            cmd_tg=int(lst_cmd[i+1])            # index
            cmd_len=int(lst_cmd[i+2])           # 문자의 개수
            for j in range(i+3, i+3+cmd_len):            # 문자의 개수만큼       
                new_num=lst_cmd[j]          # 추가할 문자를
                origin_map.insert(cmd_tg, new_num)    # 삽입한다
                cmd_tg+=1
                

        elif lst_cmd[i]=='D':
            cmd_tg=int(lst_cmd[i+1])            # index
            cmd_len=int(lst_cmd[i+2])           # 삭제 개수
            for j in range(cmd_len):            # 개수만큼
                del_num=origin_map.pop(cmd_tg)  # 해당 위치 data 삭제


        elif lst_cmd[i]=='A':
            cmd_len=int(lst_cmd[i+1])           # 추가 개수
            for j in range(cmd_len):            # 추가 횟수만큼
                new_num=lst_cmd[i+j+2]          # 추가할 문자를
                origin_map.append(new_num)      # 끝에 추가.
        
        
    return origin_map


TC=10
for testcase in range(1, TC+1):
    a=int(input())
    origin_map=list(input().split())
    num_cmd=int(input())
    lst_cmd=list(input().split())
    cnt_cmd=len(lst_cmd)
    result=secret(origin_map, lst_cmd, cnt_cmd)
    print('#{} {}'.format(testcase, " ".join(origin_map[0:10])))