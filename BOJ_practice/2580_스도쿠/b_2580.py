import sys
sys.stdin = open('b_2580.txt', 'r')

def solve(idx):
    global flag
    if flag:
        if idx == zero_cnt:
            flag = False
        else:
            can_set = {i for i in range(10)}
            y, x = zero[idx]
            s = (y//3) * 3 + (x//3)
            diff = y_set[y] | s_set[s] | x_set[x]
            can_set -= diff
            for num in can_set:
                if flag:
                    y_set[y].add(num)
                    s_set[s].add(num)
                    x_set[x].add(num)
                    total_map[y][x] = num
                    solve(idx+1)
                    y_set[y].remove(num)
                    s_set[s].remove(num)
                    x_set[x].remove(num)


total_map = [list(map(int, input().split())) for _ in range(9)]
y_set = list()
x_set = list()
s_set = list()
zero = list()
zero_cnt = 0
for y in range(9):
    tmp_x = set()
    tmp_y = set(total_map[y])
    for x in range(9):
        if total_map[y][x] == 0:
            zero_cnt += 1
            zero.append((y, x))
        tmp_x.add(total_map[x][y])
        if y%3 == 0 and x%3 == 0:
            tmp_s = set()
            for i in range(3):
                for j in range(3):
                    tmp_s.add(total_map[y+i][x+j])
            s_set.append(tmp_s)
    y_set.append(tmp_y)
    x_set.append(tmp_x)
flag = True
solve(0)

for y in range(9):
    for x in range(9):
        print(total_map[y][x], end=' ')
    print()
