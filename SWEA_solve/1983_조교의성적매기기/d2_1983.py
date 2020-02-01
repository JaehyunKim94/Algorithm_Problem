def get_score(student_list, n):
    same_score=n//10
    list_score=['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    score_dict=dict()
    # v 기준으로 정렬
    student_list = sorted(student_list, reverse=True)

    ch=0
    for j in range(0, n, same_score):
        for m in range(same_score):
            score_dict.update({student_list[j+m]:list_score[ch]})
        ch+=1

    return score_dict

TC=int(input())
for testcase in range(1, TC+1):
    obj=list(map(int, input().split()))
    n, k = obj[0], obj[1]
    student_list=list()
    student_dict=dict()

    for i in range(1, n+1):
        st_score=list(map(int, input().split()))
        ave = (0.35*st_score[0]) + (0.45*st_score[1]) + (0.2*st_score[2])
        student_list.append(ave)
        student_dict.update({i:ave})
    
    score_abc=get_score(student_list, n)

    for k1, v1 in student_dict.items():
        for k2, v2 in score_abc.items():
            if v1==k2:
                student_dict[k1]=v2
    
    print('#{} {}'.format(testcase, student_dict[k]))
    

    
    
