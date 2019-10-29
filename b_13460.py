import sys
sys.stdin = open('b_13460.txt', 'r')


def move(q, i):
    global ck
    global hole
    dif = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    d = dif[i]
    r_y, r_x, b_y, b_x = q[0], q[1], q[2], q[3]
    while total_map[r_y][r_x] != '#':
        r_y += d[0]
        r_x += d[1]
        if (r_y, r_x) == hole:
            ck += 1
            break

    while total_map[b_y][b_x] != '#':
        b_y += d[0]
        b_x += d[1]
        if (b_y, b_x) == hole:
            ck -= 2
            break

    if ck != 0:
        return '1'

    r_y -= d[0]
    r_x -= d[1]
    b_y -= d[0]
    b_x -= d[1]
    if r_y == b_y and r_x == b_x:
        if i in (0, 1):
            if q[1] > q[3]:
                b_x -= 1
            else:
                r_x -= 1
        elif i in (2, 3):
            if q[0] > q[2]:
                b_y -= 1
            else:
                r_y -= 1
    res = (r_y, r_x, b_y, b_x, i)
    return res


def solve(red, blue):
    global ck
    global result
    r_y, r_x = red[0], red[1]
    b_y, b_x = blue[0], blue[1]
    que = [(r_y, r_x, b_y, b_x, -1)]
    for t in range(1, 11):
        r = len(que)
        for _ in range(r):
            q = que.pop(0)
            for i in range(4):
                if i != q[4]:
                    new = move(q, i)
                    if len(new) > 1:
                        que.append(new)
        if ck < 0:
            result = -1
            return
        elif ck > 0:
            result = t
            return
    result = -1


N, M = map(int, input().split())
total_map = [[0]*M for _ in range(N)]
wall_lst = []
for y in range(N):
    new_lst = input()
    for x in range(M):
        if new_lst[x] == 'R':
            red = (y, x)
        elif new_lst[x] == 'B':
            blue = (y, x)
        elif new_lst[x] == 'O':
            hole = (y, x)
        total_map[y][x] = new_lst[x]
result = 0
ck = 0
solve(red, blue)
print(result)