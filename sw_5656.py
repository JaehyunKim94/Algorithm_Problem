import sys
sys.stdin = open('sw_5656.txt', 'r')

def cnt_block(k):
    for yy in range(H):
        for xx in range(W):
            if total_map[yy][xx] != 0:
                cnt_lst[k] += 1

def solve():
    pass


TC = int(input())
for testcase in range(1, TC+1):
    N, W, H = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(H)]
    cnt_lst = [0 for _ in range(W)]
    for y in range(H):
        for x in range(W):
            if total_map[y][x] != 0:
                solve()
                cnt_block(x)
                break