import sys
sys.stdin = open('b_17825.txt', 'r')

def solve(idx, score):
    global result
    if idx == 9:
        result = max(result, score)
    else:
        idx += 1
        go_point = dice[idx] - 1
        for i in range(4):
            now_p = horse[i]
            if now_p >= 0:
                nxt_lst = go_map[now_p]
                nxt_p = nxt_lst[go_point]
                visit[now_p] = 0
                if nxt_p > 31:
                    horse[i] = -1
                    solve(idx, score)
                    horse[i] = now_p

                else:
                    if visit[nxt_p] == 0:
                        visit[nxt_p] = 1
                        horse[i] = nxt_p
                        solve(idx, score + point_map[nxt_p])
                        visit[nxt_p] = 0
                        horse[i] = now_p
                visit[now_p] = 1


dice = list(map(int, input().split()))
one_way = [i*2 for i in range(20)]
center = [13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 40]
go_map = [[i+j for j in range(1, 6)]for i in range(33)]
visit = [0] * 32
# 파란원 시작
go_map[5] = [20, 21, 22, 28, 29]
go_map[10] = [23, 24, 28, 29, 30]
go_map[15] = [25, 26, 27, 28, 29]
# 중앙길
go_map[20] = [21, 22, 28, 29, 30]
go_map[21] = [22, 28, 29, 30, 31]
go_map[22] = [28, 29, 30, 31, 32]
go_map[23] = [24, 28, 29, 30, 31]
go_map[24] = [28, 29, 30, 31, 32]
# 마지막길
go_map[16] = [17, 18, 19, 31, 32]
go_map[17] = [18, 19, 31, 32, 33]
go_map[18] = [19, 31, 32, 33, 34]
go_map[19] = [31, 32, 33, 34, 35]


point_map = one_way + center
horse = [0] * 4
result = 0
solve(-1, 0)
print(result)