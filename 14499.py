import sys
sys.stdin = open('14499.txt' ,'r')

N, M, x, y, K = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
order_lst = list(map(int, input().split()))
