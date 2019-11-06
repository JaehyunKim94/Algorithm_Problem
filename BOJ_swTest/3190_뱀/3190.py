import sys
sys.stdin = open('3190.txt', 'r')


def change_dir(d, order):
    if d in (0, 1):
        if order == 'L':
            return d + 2
        else:
            return 3 - d
    else:
        if order == 'L':
            return 3 - d
        else:
            return d - 2


def solve():
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    t = 0 # 시간
    snake = [(0, 0)] # 몸통
    y, x = 0, 0 # 머리
    d = 3
    while True:
        t += 1
        y += dir[d][0]
        x += dir[d][1]
        if len(time_lst) > 0 and t == time_lst[0]:
            order = order_lst.pop(0)
            time_lst.pop(0)
            d = change_dir(d, order)

        if 0 <= y < N and 0 <= x < N:
            if (y, x) in snake:
                break
            else:
                if total_map[y][x] == 9:
                    total_map[y][x] = 0
                else:
                    snake.pop(0)
                snake.append((y, x))
        else:
            break
    print(t)


N = int(input())
total_map = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    total_map[y-1][x-1] = 9
L = int(input())
time_lst = [0] * L
order_lst = [0] * L
for i in range(L):
    time, order = input().split()
    time_lst[i] = int(time)
    order_lst[i] = order
time_lst.sort()
solve()