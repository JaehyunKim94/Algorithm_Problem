import sys
sys.stdin = open('b_2580.txt', 'r')

def getNum(ay, ax):
    num_set = {i+1 for i in range(9)}
    fy = (ay // 3) * 3
    ty = fy + 3
    fx = (ax // 3) * 3
    tx = fx + 3
    dif_set = set()
    for y in range(9):
        for x in range(9):
            if y == ay:
                dif_set.add(total_map[y][x])
            if x == ax:
                dif_set.add(total_map[y][x])
            if fy <= y < ty and fx <= x < tx:
                dif_set.add(total_map[y][x])
    num_set -= dif_set
    return list(num_set)

total_map = [list(map(int, input().split())) for _ in range(9)]
zero = set()
for y in range(9):
    for x in range(9):
        if total_map[y][x] == 0:
            num_lst = getNum(y, x)
            if len(num_lst) == 1:
                total_map[y][x] = num_lst[0]
            else:
                zero.add((y, x))
while zero:
    tmp_zero = set()
    for y, x in zero:
        num_lst = getNum(y, x)
        if len(num_lst) == 1:
            total_map[y][x] = num_lst[0]
        else:
            tmp_zero.add((y, x))
    zero = tmp_zero

for y in range(9):
    for x in range(9):
        print(total_map[y][x], end=' ')
    print()