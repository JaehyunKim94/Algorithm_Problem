import sys
sys.stdin = open('b_2206.txt', 'r', )

def isInbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False

def BFS(loop_set, count):
    new_set = set()


N, M = map(int, input().split())
total_map = [input() for _ in range(N)]
visit = [[0]*M for _ in range(N)]
visit[0][0] = 1
loop_set = set()
loop_set.add((0, 0, 1, visit))
BFS(loop_set, 1)