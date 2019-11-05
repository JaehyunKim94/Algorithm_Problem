import sys
sys.stdin = open('d4_3752.txt', 'r')


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    new_lst = list(map(int, input().split()))
    cnt = 1
    score_ck = [0 for _ in range(N*100)]
    score_lst = [0]
    for i in range(N):
        for j in range(cnt):
            ans = new_lst[i] + score_lst[j]
            if score_ck[ans] == 0:
                score_ck[ans] = 1
                score_lst.append(ans)
                cnt += 1

    print('#{} {}'.format(testcase, cnt))
