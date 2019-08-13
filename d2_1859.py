def find_max(list_a, position_s, days):
    max_value=0
    max_index=0
    result_list=[]
    for i in range(position_s, days):
        if list_a[i] > max_value:
            max_value=list_a[i]
            max_index=i
    result_list.append(max_index)
    result_list.append(max_value)
    return result_list

TC=int(input())

for testcase in range(1, TC+1):
    days=int(input())
    list_a=list(map(int, input().split()))
    position_s=0
    position_n=0
