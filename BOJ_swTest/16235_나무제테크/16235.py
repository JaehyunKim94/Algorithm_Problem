import sys
sys.stdin = open('16235.txt', 'r')


# def is_inbox(y, x):
#     if 0 <= y < N and 0 <= x < N:
#         return True
#     return False

# 봄에서 여름, 겨울 리스트 만들었더니 13%
# is_inbox 안쓰니 37%
# sort 지워도 37%
# 죽은나무 지우는걸 한번에 하니 통과


N, M, K = map(int, input().split())
new_energy = [list(map(int, input().split())) for _ in range(N)]
e_map = [[5] * N for _ in range(N)]
total_map = [[0] * N for _ in range(N)]
result = M
for _ in range(M):
    y, x, z = map(int, input().split())
    x -= 1
    y -= 1
    if total_map[y][x] == 0:
        total_map[y][x] = [z]
    else:
        total_map[y][x].append(z)
        total_map[y][x].sort()

dif = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
for k in range(K):
    # 봄
    die = []
    bun = []
    for y in range(N):
        for x in range(N):
            if total_map[y][x] != 0:
                r = len(total_map[y][x])
                for i in range(r):
                    age = total_map[y][x][i]
                    if e_map[y][x] >= age:
                        total_map[y][x][i] += 1
                        e_map[y][x] -= age
                        if (age+1) % 5 == 0:
                            bun.append((y, x))
                    else:
                        die_tree = [y, x, total_map[y][x][i:]]
                        die.append(die_tree)
                        total_map[y][x] = total_map[y][x][:i]
                        break
    # 여름
    for tree in die:
        y, x, age_lst = tree[0], tree[1], tree[2]
        for age in age_lst:
            result -= 1
            e_map[y][x] += age//2

    # 가을
    for tree in bun:
        y, x = tree[0], tree[1]
        for d in dif:
            yy = y + d[0]
            xx = x + d[1]
            if 0 <= yy < N and 0 <= xx < N:
                result += 1
                if total_map[yy][xx] != 0:
                    total_map[yy][xx].insert(0, 1)
                else:
                    total_map[yy][xx] = [1]

    for y in range(N):
        for x in range(N):
            e_map[y][x] += new_energy[y][x]

print(result)