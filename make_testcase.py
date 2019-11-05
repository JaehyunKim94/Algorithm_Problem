import sys
import random

sys.stdout = open('test3.txt', 'w')

T = random.randint(10, 10)
print(T)
for t in range(T):
    N = random.randint(5, 20)
    M = random.randint(5, 20)
    C = random.randint(1, 1000)
    print(N, M, C)
    board = [[0] * M for _ in range(N)]
    minerals = random.randint(20, 20)
    for _ in range(minerals):
        r = random.randint(0, N - 1)
        c = random.randint(0, M - 1)
        yang = random.randint(10, 200)
        board[r][c] = yang
    r = random.randint(0, N - 1)
    c = random.randint(0, M - 1)
    board[r][c] = 1
    for r in range(N):
        for c in range(M):
            print(board[r][c], end=' ')
        print()