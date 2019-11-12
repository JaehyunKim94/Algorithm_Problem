import sys
sys.stdin = open('17779.txt', 'r')

N = int(input())
total_map = [list(map(int, input().split())) for _ in range(N)]

