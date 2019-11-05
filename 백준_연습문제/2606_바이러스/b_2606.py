import sys
sys.stdin = open('b_2606.txt', 'r')


def dfs(k):
    global cnt
    cnt += 1
    visited[k] = 1
    for i in range(N+1):
        if total_map[k][i] == 1:
            if visited[i] == 0:
                dfs(i)


N = int(input())
total_map = [[0] * (N+1) for _ in range(N+1)]
M = int(input())
node_lst = [list(map(int, input().split())) for _ in range(M)]
cnt = -1
for node in node_lst:
    total_map[node[0]][node[1]] = 1
    total_map[node[1]][node[0]] = 1
visited = [0] * (N+1)
dfs(1)
print(cnt)