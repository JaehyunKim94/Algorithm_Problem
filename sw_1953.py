import sys
sys.stdin = open('sw_1953.txt', 'r')

def solve(y, x, k):



dif = [(-1, 0), (1, 0), (0, -1), (0, 1)]
TC = int(input())
for testcase in range(1, TC+1):
    N, M, R, C, L = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0 for _ in range(M)] for __ in range(N)]
    solve(R, C, 0)