def find_max(list_a, position_s, days):
    max_value2=0
    max_index=0
    get_money=0
    result_list=[]
    # 현재 위치 ~ 끝 중에 최고 가격과 그 index 찾기 - 최대값의 위치 : result_list[0]
    for i in range(position_s, days):
        if list_a[i] > max_value2:
            max_value2=list_a[i]
            max_index=i
    result_list.append(max_index)
    
    # 최고 가격과 당일 가격의 차만큼 이득 발생 - 발생한 이득 : result_list[1]
    for i in range(position_s, max_index):
        get_money+=max_value2-list_a[i]
    result_list.append(get_money)
    return result_list


#실행구문
TC=int(input())

for testcase in range(1, TC+1):
    days=int(input())
    list_a=list(map(int, input().split()))
    position_s=0
    result=0
    
    while position_s!=days:
        list_b=find_max(list_a, position_s, days)
        position_s=list_b[0]+1
        result+=list_b[1]

    print('#{} {}'.format(testcase, result))