import sys
sys.stdin = open('sw_5656.txt', 'r')

TC = int(input())
for testcase in range(1, TC+1):
    N, W, H = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(H)]
