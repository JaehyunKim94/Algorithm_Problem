import sys
sys.stdin = open('16235.txt', 'r')

dydx = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1)]
N, M, K = map(int, input().split())
new_energy = [list(map(int, input().split())) for _ in range(N)]
energy_map = [[5] * N for _ in range(N)]
tree_map = [[[] for _ in range(N)] for _ in range(N)]
ck = set()
cnt = 0
for _ in range(M):
    y, x, age = map(int, input().split())
    y -= 1
    x -= 1
    tree_map[y][x] = [age]
    ck.add((y, x))
    cnt += 1

for kk in range(K):
    bunsik = []
    for y, x in ck:
        die_energy = 0
        new_tree = []
        for age in tree_map[y][x]:
            if age <= energy_map[y][x]:
                new_tree.append(age+1)
                energy_map[y][x] -= age
                if (age+1) % 5 == 0:
                    bunsik.append((y, x))
            else:
                die_energy += age//2
                cnt -= 1
        tree_map[y][x] = new_tree
        energy_map[y][x] += die_energy

    for y, x in bunsik:
        for dy, dx in dydx:
            yy = y + dy
            xx = x + dx
            if 0 <= xx < N and 0 <= yy < N:
                tree_map[yy][xx].append(1)
                cnt += 1
    tmp_ck = set()
    for y in range(N):
        for x in range(N):
            if len(tree_map[y][x]) > 0:
                tree_map[y][x].sort()
                tmp_ck.add((y, x))
            energy_map[y][x] += new_energy[y][x]
    ck = tmp_ck
print(cnt)