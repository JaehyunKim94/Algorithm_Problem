import sys
sys.stdin = open('sw_2105.txt', 'r')

TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    print(total_map)