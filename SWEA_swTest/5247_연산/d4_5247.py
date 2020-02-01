import sys
sys.stdin = open('d4_5247.txt', 'r')
import collections

def solve(lst):
    global result
    global visit
    cnt = 1
    while lst:
        new_lst = []
        for num in lst:
            for new in (num*2, num+1, num-10, num-1):
                if new == M:
                    result = cnt
                    return
                if 0 < new < 1000001:
                    if visit[new] == 0:
                        visit[new] = 1
                        new_lst.append(new)
        lst = new_lst
        cnt += 1

TC = int(input())
for testcase in range(1, TC+1):
    result = 1000000
    N, M = map(int, input().split())
    visit = [0] * 10000001
    visit[N] = 1
    solve([N])
    print('#{} {}'.format(testcase, result))