import sys
sys.stdin = open('b_1260.txt', 'r')


def bfs(k):
    que = [k]
    visit = [0] * (N+1)
    res = ''
    while que:
        t = que.pop(0)
        res += str(t) + ' '
        visit[t] = 1
        for i in range(N+1):
            if total_map[t][i] == 1:
                if (visit[i] == 0) and  (i not in que):
                    que.append(i)
    return res


def dfs(k):
    global a_res
    a_res += str(k) + ' '
    visited[k] = 1
    for i in range(N+1):
        if total_map[k][i] == 1 and visited[i] == 0:
            dfs(i)
    return


N, M, V = map(int, input().split())
total_map = [[0] * (N+1) for _ in range(N+1)]
node_lst = [list(map(int, input().split())) for _ in range(M)]
for node in node_lst:
    total_map[node[0]][node[1]] = 1
    total_map[node[1]][node[0]] = 1

visited = [0] * (N+1)

a_res = ''
dfs(V)
print(a_res)
print(bfs(V))