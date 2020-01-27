import sys
sys.stdin = open('b_17780.txt')

def isInbox(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True

def changeDirection(d):
    if d in (0, 1):
        return 1-d
    else:
        return 5-d

def changeDict(lst, y, x):
    for ii in lst:
        chess_dic[ii][0], chess_dic[ii][1] = y, x
    return

def solve(idx, b_cnt):
    global result
    y, x, d = chess_dic[idx]
    yy = y + dydx[d][0]
    xx = x + dydx[d][1]
    if isInbox(yy, xx):
        obj = chess_map[y][x]
        if total_map[yy][xx] == 0:
            chess_map[yy][xx] += obj
            if len(chess_map[yy][xx]) >= 4:
                result = 2
                return
            chess_map[y][x] = []
            changeDict(obj, yy, xx)
            return
        elif total_map[yy][xx] == 1:
            obj.reverse()
            chess_map[yy][xx] += obj
            if len(chess_map[yy][xx]) >= 4:
                result = 2
                return
            chess_map[y][x] = []
            changeDict(obj, yy, xx)
            return
        else:
            if b_cnt == 0:
                chess_dic[idx] = [y, x, changeDirection(d)]
                solve(idx, 1)
            else:
                return
    else:
        if b_cnt == 0:
            chess_dic[idx] = [y, x, changeDirection(d)]
            solve(idx, 1)
        else:
            return


dydx = [(0, 1), (0, -1), (-1, 0), (1, 0)]
N, K = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
chess_map = [[list() for _ in range(N)] for __ in range(N)]
chess_dic = dict()
for i in range(K):
    y, x, d = map(int, input().split())
    y -= 1
    x -= 1
    d -= 1
    chess_dic.update({i: [y, x, d]})
    chess_map[y][x] = [i]

result = -1
for kk in range(1, 1001):
    for idx in range(K):
        y, x, d = chess_dic[idx]
        if chess_map[y][x][0] == idx:
            solve(idx, 0)
        if result > 0:
            break
    if result > 0:
        result = kk
        break
print(result)