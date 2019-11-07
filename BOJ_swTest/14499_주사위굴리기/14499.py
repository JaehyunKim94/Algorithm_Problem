import sys
sys.stdin = open('14499.txt' ,'r')


def solve(dice, ord):
    # 동 서 북 남
    dir = [(3, 1, 0, 5, 4, 2), (2, 1, 5, 0, 4, 3), (1, 5, 2, 3, 0, 4), (4, 0, 2, 3, 5, 1)]
    d = dir[ord]
    new_dice = [0] * 6
    for i in range(6):
        new_dice[i] = dice[d[i]]
    return new_dice


N, M, y, x, K = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
order_lst = list(map(int, input().split()))
# 위 앞 동 서 뒤 아래
dice = [0] * 6
move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
for order in order_lst:
    order -= 1
    mov = move[order]
    yy = y + mov[0]
    xx = x + mov[1]
    if 0 <= yy < N and 0 <= xx < M:
        dice = solve(dice, order)
        if total_map[yy][xx] == 0:
            total_map[yy][xx] = dice[5]
        else:
            dice[5] = total_map[yy][xx]
            total_map[yy][xx] = 0
        y, x = yy, xx
        print(dice[0])

