import sys
sys.stdin = open('b_16236.txt', 'r')

N = int(input())
total_map = [list(map(int, input().split())) for _ in range(N)]
fish_lst = []
for y in range(N):
    for x in range(N):
        v = total_map[y][x]
        if 0 < v < 9:
            fish_lst.append((v, y, x))
        elif total_map[y][x] == 9:
            shark_p = (2, y, x)
print(shark_p)