import sys
sys.stdin = open('d3_5204.txt', 'r')


def solve(s, e):
    if e-s < 2:
        return
    else



TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    solve(0, N)