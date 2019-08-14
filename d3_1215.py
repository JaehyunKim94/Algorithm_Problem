def is_palom(new_str):
    rev_str=''
    rev_str=''.join(reversed(new_str))
    if new_str==rev_str:
        return True
    else:
        return False
 
def make_nin(new_list):
    list_nin=list()
    new_len=len(new_list)
    for y in range(new_len):
        new_str=''
        for x in range(new_len):
            new_str+=new_list[x][y]
        list_nin.append(new_str)
    return list_nin
 
def pal_cnt(new_list, pal_dict, n):
    for st_li in new_list:
        for x in range(9-n):
            app_str=''
            for i in range(n):
                app_str+=st_li[x+i]
            if is_palom(app_str):
                if app_str not in pal_dict.keys():
                    pal_dict.update({app_str:1})
                else:
                    pal_dict[app_str] +=1
    return pal_dict
 
TC=10
for testcase in range(1, TC+1):
    n=int(input())
    new_list=list()
    pal_dict=dict()
    for k in range(8):
        in_str=input()
        new_list.append(in_str)
 
    pal_dict=pal_cnt(new_list, pal_dict, n)
    new_list=make_nin(new_list)
    pal_dict=pal_cnt(new_list, pal_dict, n)
 
    result=0
    for v in pal_dict.values():
        result+=v
     
    print('#{} {}'.format(testcase, result))