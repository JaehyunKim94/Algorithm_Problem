import sys

sys.stdin = open('6109.txt', 'r')


def is_wall(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False


def find_pk(S):
    if S == 'up':
        return 0
    if S == 'down':
        return 1
    if S == 'left':
        return 2
    if S == 'right':
        return 3


def game():
    for y in range(N):
        for x in range(N):
            if total_map[y][x] != 0:
                if is_wall(y, x + 1):
                    if total_map[y][x] == total_map[y][x+1]:
                        total_map[y][x] += total_map[y][x+1]
                        total_map[y][x+1] = 0


def make_new():
    new_map = []
    for y in range(N):
        ins_lst = []
        cnt = 0
        for x in range(N):
            if total_map[y][x] == 0:
                cnt += 1
            else:
                ins_lst.append(total_map[y][x])
        for __ in range(cnt):
            ins_lst.append(0)
        new_map.append(ins_lst)
    return new_map


def turn_map(pk):
    fixed_map = [[0 for _ in range(N)] for __ in range(N)]
    if pk == 0:
        for y in range(N):
            for x in range(N):
                fixed_map[y][x] = total_map[x][N-1-y]

    if pk == 1:
        for y in range(N):
            for x in range(N):
                fixed_map[y][x] = total_map[N-1-x][y]

    if pk == 2:
        fixed_map = total_map

    if pk == 3:
        for y in range(N):
            for x in range(N):
                fixed_map[y][x] = total_map[y][N-1-x]

    return fixed_map


def remap():
    global pk
    if pk == 0:
        pk = 1
    elif pk == 1:
        pk = 0


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

TC = int(input())
for testcase in range(1, TC + 1):
    lst_a = list(input().split())
    N = int(lst_a[0])
    S = lst_a[1]
    pk = find_pk(S)
    total_map = []
    for _ in range(N):
        new_lst = list(map(int, input().split()))
        total_map.append(new_lst)

    total_map = turn_map(pk)
    total_map = make_new()
    game()
    remap()
    total_map = make_new()
    total_map = turn_map(pk)

    print('#{}'.format(testcase))
    for i in range(N):
        for j in range(N):
            print(total_map[i][j], end=' ')
        print()
