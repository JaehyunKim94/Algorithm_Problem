import sys
sys.stdin = open('d3_6190.txt', 'r')

TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    result = -1
    for i in range(N-1):
        for j in range(i+1, N):
            cal = num_lst[i]*num_lst[j]
            ck = True
            while ck:
                a = cal%10
                cal = cal//10
                if a < cal%10:
                    ck = False
                    break
                if cal < 10:
                    break
            if ck:
                if num_lst[i] * num_lst[j] > result:
                    result = num_lst[i] * num_lst[j]

    print('#{} {}'.format(testcase, result))