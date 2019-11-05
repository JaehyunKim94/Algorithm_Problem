import sys
sys.stdin = open('1961.txt', 'r')


def ninty():
    new_map = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            new_map[y][x] = str(total_map[N-1-x][y])
        new_map[y] = ''.join(new_map[y])
    return sum([], new_map)


def oneei():
    new_map = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            new_map[N-1-y][x] = str(total_map[y][N-1-x])

    for y in range(N):
        new_map[y] = ''.join(new_map[y])
    return sum([], new_map)


def twose():
    new_map = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            new_map[y][x] = str(total_map[x][N-1-y])
        new_map[y] = ''.join(new_map[y])
    return sum([], new_map)


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    total_map = []
    for _ in range(N):
        new_lst = list(map(int, input().split()))
        total_map.append(new_lst)

    a = ninty()
    b = oneei()
    c = twose()

    print('#{}'.format(testcase), end=' ')
    print()
    for i in range(N):
        print(a[i], end=' ')
        print(b[i], end=' ')
        print(c[i])