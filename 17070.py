import sys
sys.stdin = open('17070.txt', 'r')
import time

def solve():
    pass


st = time.time()
N = int(input())
total_map = [list(map(int, input().split())) for _ in range(N)]
cnt_map = [[0] * M for _ in range(N)]
print(solve())

print(time.time() - st)