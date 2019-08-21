TC=int(input())
for testcase in range(1, TC+1):
    NM=list(map(int, input().split()))
    n, m = NM[0], NM[1]
    result=[0, 0]
    for i in range(n):
        score=0
        ans=list(map(int, input().split()))
        for ans_1 in ans:
            if ans_1==1:
                score+=1
        if score > result[1]:
            result[1]=score
            result[0]=1
        elif score == result[1]:
            result[0]+=1

    print('#{} {}'.format(testcase, ' '.join(result)))