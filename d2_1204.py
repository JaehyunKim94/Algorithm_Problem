TC=int(input())

for testcase in range(TC):
    intest=int(input())
    score_list=list(map(int, input().split()))

    score_dict=dict()
    for score in score_list:
        if score not in score_dict.keys():
            score_dict.update({score:1})
        else:
            score_dict[score]+=1
    
    result_v=0
    result_k=0

    for k, v in score_dict.items():
        if v>result_v:
            result_v=v
            result_k=k
    print('#{} {}'.format(intest, result_k))