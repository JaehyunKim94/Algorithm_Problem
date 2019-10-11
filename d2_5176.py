import sys
sys.stdin = open('d2_5176.txt', 'r')


def solve(k):
    global num
    




TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    node_lst = [0 for i in range(N+1)]
    num = 1
    solve(1)