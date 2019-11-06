import sys
sys.stdin = open('14499.txt' ,'r')

N, M, x, y, K = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
order_lst = list(map(int, input().split()))
# 위 뒤 오른 왼 앞 아래
dice = [0] * 6
# 동 서 북 남
dir = [0] * 4