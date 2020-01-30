import sys
sys.stdin = open('b_2580.txt', 'r')

def check(y, x, num):
    for i in range(9):
        if total_map[y][i] == num:
            return False
        if total_map[i][x] == num:
            return False
    cy = (y // 3) * 3
    cx = x // 3


total_map = [list(map(int, input().split())) for _ in range(9)]
y_set = list()
x_set = list()
s_set = list()

for y in range(9):
    tmp_x = set()
    tmp_y = set(total_map[y])
    for x in range(9):
        tmp_x.add(total_map[x][y])
    y_set.append(tmp_y)
    x_set.append(tmp_x)

