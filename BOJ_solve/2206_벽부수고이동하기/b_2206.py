import sys
sys.stdin = open('b_2206.txt', 'r', )

def isInbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False

def BFS(loop_set):
    global ck, bomb_visit, visit
    new_set = set()
    for y, x, bomb in loop_set:
        if y == N-1 and x == M-1:
            ck = True
            return
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            yy = y + dy
            xx = x + dx
            if isInbox(yy, xx):
                if bomb:
                    if total_map[yy][xx] == '0' and not visit[yy][xx]:
                        visit[yy][xx] = 1
                        new_set.add((yy, xx, bomb))
                    elif total_map[yy][xx] == '1' and not bomb_visit[yy][xx]:
                        bomb_visit[yy][xx] = 1
                        new_set.add((yy, xx, 0))
                else:
                    if total_map[yy][xx] == '0' and not bomb_visit[yy][xx]:
                        bomb_visit[yy][xx] = 1
                        new_set.add((yy, xx, 0))
    return new_set

N, M = map(int, input().split())
result = -1
total_map = [input() for _ in range(N)]
visit = [[0]*M for _ in range(N)]
visit[0][0] = 1
bomb_visit = [[0]*M for _ in range(N)]
bomb_visit[0][0] = 1
loop_set = set()
loop_set.add((0, 0, 1))
count = 0
ck = False
while loop_set:
    count += 1
    new_loop = BFS(loop_set)
    if ck:
        result = count
        break
    loop_set = new_loop
print(result)